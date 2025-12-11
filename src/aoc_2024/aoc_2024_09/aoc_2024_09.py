# Advent of Code 2024 - Day 09 solution

from enum import Enum


class IndexType(Enum):
    FILE = "file"
    EMPTY = "empty"

    def __repr__(self):
        return self.value

class IndexEntry:
    def __init__(self, memory_start : int, file_size : int, type: IndexType = IndexType.FILE, file_index : int | None = None):
        self.memory_start = memory_start
        self.type = type 
        self.file_size = file_size
        self.file_index = file_index

    def __repr__(self):
        return f"(start={self.memory_start}, size={self.file_size}, {self.type}{f', file_id={self.file_index}' if self.file_index is not None else ''}) \n"
   

class Filesystem:
    def __init__(self, diskmap : str):
        self.diskmap = diskmap.strip()
        self.filesystem = []
        self.size = sum(int(x) for x in self.diskmap)
        self.file_index : list[IndexEntry] = []
        self.empty_index : list[IndexEntry] = []

    def index_from_diskmap(self):
        is_file = True
        file_index : int = 0
        memory_pos : int = 0
        for size in self.diskmap:
            if is_file:
                self.file_index.append(IndexEntry(memory_pos, int(size), IndexType.FILE, file_index))
                memory_pos += int(size)
                file_index += 1
            else:
                if int(size) > 0:
                    self.empty_index.append(IndexEntry(memory_pos, int(size), IndexType.EMPTY))
                    memory_pos += int(size)
            is_file = not is_file

    def cleanup_and_sort(self):
        self.file_index = [f for f in self.file_index if f.file_size > 0]
        self.file_index.sort(key=lambda entry: entry.memory_start)

        self.empty_index = [e for e in self.empty_index if e.file_size > 0]
        self.empty_index.sort(key=lambda entry: entry.memory_start)

    def compact_index_part2(self):
        for file in self.file_index[::-1]:
            suitable = next((e for e in self.empty_index 
                             if e.memory_start < file.memory_start 
                             and e.file_size >= file.file_size
                             and e.file_size > 0), None)
            if suitable:
                self.move_whole_file(file, suitable)

    def move_whole_file(self, file: IndexEntry, empty: IndexEntry):
        # Move file to this empty space
        old_start = file.memory_start
        file.memory_start = empty.memory_start

        # Create new empty space in place of a moved file
        self.empty_index.append(IndexEntry(old_start, file.file_size, IndexType.EMPTY))

        # Update used empty space - mark as deleted instead of removing
        if empty.file_size == file.file_size:
            empty.file_size = 0  # Mark as deleted (O(1) instead of O(n))
        else:
            empty.memory_start += file.file_size
            empty.file_size -= file.file_size

    def move_part_file(self, file: IndexEntry, empty: IndexEntry):
        # Create file in empty space
        self.file_index.append(IndexEntry(empty.memory_start, empty.file_size, IndexType.FILE, file.file_index))    

        # Reduce size of original file
        file.file_size -= empty.file_size

        # Create new empty space in place of a moved part
        self.empty_index.append(IndexEntry(file.memory_start + empty.file_size, empty.file_size, IndexType.EMPTY))

        # Mark empty space as deleted
        empty.file_size = 0

    def compact_index_part1(self):
        for file in self.file_index[::-1]:
            remaining_size = file.file_size
            for empty in self.empty_index:
                # Skip deleted entries and entries past this file
                if empty.file_size == 0 or empty.memory_start > file.memory_start:
                    continue
                
                if remaining_size == 0:
                    break 
                
                # Store the size BEFORE move_part_file changes it
                empty_size = empty.file_size
                
                if empty_size >= remaining_size:
                    self.move_whole_file(file, empty)
                    break
                else:
                    self.move_part_file(file, empty)
                    remaining_size -= empty_size
                    
    def checksum_from_index(self):
        checksum = 0
        for file in [f for f in self.file_index if f.file_size > 0]:  # Skip deleted entries
            checksum += file.file_index*sum(range(file.memory_start, file.memory_start+file.file_size))
        return checksum

    def build_from_diskmap(self):
        file = True
        file_number : int = 0
        for value in self.diskmap:
            if file:
                self.filesystem.extend([file_number]*int(value))
                file_number += 1
            else:
                self.filesystem.extend(["."]*int(value))
            file = not file

    def compact_and_checksum_part1(self) -> int:
        checksum = 0
        left = 0
        right = len(self.filesystem) -1

        while left <= right:
            if self.filesystem[left] != ".":
                checksum += self.filesystem[left] * left
                left += 1
            else:
                while right >= left and self.filesystem[right] == ".":
                    right -= 1
                
                if right > left:
                    checksum += left * int(self.filesystem[right])
                    left += 1
                    right -=1

        return checksum
    
    def compact_part2(self):
        """Compact filesystem by moving whole files only (right to left)"""
        filesystem = self.filesystem  # Local reference (faster)
        
        # Get list of files (id, start, end) by scanning right to left
        files = []
        i = len(filesystem) - 1
        while i >= 0:
            if filesystem[i] != ".":
                file_id = filesystem[i]
                file_end = i
                while i >= 0 and filesystem[i] == file_id:
                    i -= 1
                file_start = i + 1
                files.append((file_id, file_start, file_end))
            else:
                i -= 1
        
        # Try to move each file (they're already in reverse order)
        for file_id, file_start, file_end in files:
            file_size = file_end - file_start + 1
            
            # Find first gap large enough (left to right)
            i = 0
            while i < file_start:
                if filesystem[i] == ".":
                    gap_start = i
                    while i < file_start and filesystem[i] == ".":
                        i += 1
                    gap_size = i - gap_start
                    
                    # If gap is large enough, move the file
                    if gap_size >= file_size:
                        # Move file to gap
                        filesystem[gap_start:gap_start+file_size] = [file_id] * file_size
                        # Clear original position
                        filesystem[file_start:file_end+1] = ["."] * file_size
                        break
                else:
                    i += 1

def checksum_part2(filesystem: list[int | str]) -> int:
    checksum = 0
    for index, file in enumerate(filesystem):
        if file != ".":
            checksum += index * file
    return checksum

def solve_part_1(input : str) -> int:
    filesystem = Filesystem(input)
    filesystem.build_from_diskmap()
    checksum = filesystem.compact_and_checksum_part1()
    return checksum

def solve_part_1_indexing(input : str) -> int:
    filesystem = Filesystem(input)

    filesystem.index_from_diskmap()
    filesystem.compact_index_part1()  

    checksum = filesystem.checksum_from_index()
    return checksum

def solve_part_2(input : str) -> int:
    filesystem = Filesystem(input)
    filesystem.build_from_diskmap()
    print(filesystem.filesystem)
    filesystem.compact_part2()
    print(filesystem.filesystem)
    checksum = checksum_part2(filesystem.filesystem)
    return checksum

def solve_part_2_indexing(input : str) -> int:
    filesystem = Filesystem(input)

    filesystem.index_from_diskmap()
    filesystem.compact_index_part2()

    filesystem.cleanup_and_sort()
    checksum = filesystem.checksum_from_index()

    return checksum

if __name__ == "__main__":
    pass
