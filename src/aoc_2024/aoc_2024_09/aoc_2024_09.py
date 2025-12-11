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
        self.index : list[IndexEntry] = []
        print(f"Initialized filesystem with size {self.size} from diskmap {self.diskmap}")

    def index_from_diskmap(self):
        is_file = True
        file_index : int = 0
        memory_pos : int = 0
        for size in self.diskmap:
            if is_file:
                self.index.append(IndexEntry(memory_pos, int(size), IndexType.FILE, file_index))
                memory_pos += int(size)
                file_index += 1
            else:
                if int(size) > 0:
                    self.index.append(IndexEntry(memory_pos, int(size), IndexType.EMPTY))
                    memory_pos += int(size)
            is_file = not is_file

    def sort_index(self):
        self.index.sort(key=lambda entry: entry.memory_start)

    def compact_index_part2(self):
        for file in [f for f in self.index[::-1] if f.type == IndexType.FILE]:
            empty_spaces = [e for e in self.index if e.type == IndexType.EMPTY and e.memory_start <= file.memory_start]
            for empty in empty_spaces:
                if empty.file_size >= file.file_size:
                    self.move_whole_file(file, empty)
                    break

    def move_whole_file(self, file: IndexEntry, empty: IndexEntry):
        # Move file to this empty space
        old_start = file.memory_start
        file.memory_start = empty.memory_start
        # Update used empty space
        if empty.file_size == file.file_size:
            self.index.remove(empty)
        else:
            empty.memory_start += file.file_size
            empty.file_size -= file.file_size
        print(f"Moved file {file.file_index} from {old_start} to {file.memory_start}")

        # Create new empty space in place of a moved file
        self.index.append(IndexEntry(old_start, file.file_size, IndexType.EMPTY))

    def move_part_file(self, file: IndexEntry, empty: IndexEntry):
        # Fill empty space with part of the file
        empty.type = IndexType.FILE
        empty.file_index = file.file_index

        # Reduce size of original file
        file.file_size -= empty.file_size

        # Create new empty space in place of a moved part
        self.index.append(IndexEntry(file.memory_start + empty.file_size, empty.file_size, IndexType.EMPTY))

        pass

    def compact_index_part1(self):
        for file in [f for f in self.index[::-1] if f.type == IndexType.FILE]:
            empty_spaces = [e for e in self.index if e.type == IndexType.EMPTY and e.memory_start < file.memory_start]
            remaining_size = file.file_size
            for empty in empty_spaces:
                # Check if we can fit the whole file into this empty space
                if empty.file_size >= remaining_size:
                    self.move_whole_file(file, empty)
                    break
                else:
                    self.move_part_file(file, empty)
                    remaining_size -= empty.file_size

                if remaining_size == 0:
                    break    
        
    def checksum_from_index(self):
        checksum = 0
        for file in [f for f in self.index if f.type == IndexType.FILE]:
            checksum += file.file_index*sum(range(file.memory_start, file.memory_start+file.file_size))
        print(f"Checksum from index: {checksum}")
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
        for i, value in enumerate(self.filesystem):
            if value == ".":
                while True:
                    new = self.filesystem.pop(-1)
                    if len(self.filesystem) <= i:
                        break
                    if new != ".":
                        #self.filesystem[i] = new
                        checksum += i * int(new)
                        break
                    
            else:
                checksum += i * int(value)
        print(self.filesystem)
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

    filesystem.index_from_diskmap()
    filesystem.compact_index_part2()

    checksum = filesystem.checksum_from_index()

    return checksum

if __name__ == "__main__":
    example = "2333133121414131402" 
    solve_part_2(example)
