import numpy as np


class WordSearch:
    def __init__(self, input : str):
        self.character_array : list[list[str]] = []
        self.horizontal_lines : list[str] = []

        for index, line in enumerate(input.splitlines()):
            self.horizontal_lines.append(line)
            self.character_array.append([])
            [self.character_array[index].append(x) for x in line]

        self.vertical_lines = ["".join(x) for x in list(zip(*self.character_array, strict=True))]

    def calculate_diagonals(self) -> list[str]:
        lines_list1, lines_list2 = [], []

        m_total = len(self.horizontal_lines)
        n_total = len(self.vertical_lines)
        lines_total = m_total + n_total -1

        for t in range (0, lines_total):
            line1, line2 = "", ""
            for n in range(max(0,t-m_total+1), min(t+1,n_total)):
                m = t - n
                line1 += self.character_array[m][n]
                line2 += self.character_array[m][n_total-n-1]

            lines_list1.append(line1)
            lines_list2.append(line2)

        return lines_list1 + lines_list2

    def countsubmartixes(self) -> int:
        count = 0
        array = np.array(self.character_array)

        positions = np.argwhere(array == 'A')
        subarrays = [array[i-1:i+2,j-1:j+2] for i, j in positions if (i > 0 and (i < array.shape[0]-1) and j > 0 and  j < (array.shape[1]-1))]

        key = np.array([["M","","M"],["","A",""],["S", "", "S"]])
        mask = np.isin(key, "")

        masked_subarrays = [np.where(mask, "", subarray) for subarray in subarrays]

        count = sum([1 for subarray in masked_subarrays if np.array_equal(subarray,key)])

        for i in range(1,4):
            key = np.rot90(key, k=i)
            count += sum([1 for subarray in masked_subarrays if np.array_equal(subarray,key)])

        return count

def countinlines(lines : list[str], key : str):
    reversed_key = key[::-1]
    return sum([line.count(key) + line.count(reversed_key) for line in lines])

def part1(input_str : str) -> int:
    input = WordSearch(input_str)
    key = "XMAS"
    diagonals = input.calculate_diagonals()

    return countinlines(input.horizontal_lines + input.vertical_lines + diagonals, key)

def part2(input_str : str) -> int:
    input = WordSearch(input_str)

    count = input.countsubmartixes()

    return count

if __name__ == "__main__":
    pass