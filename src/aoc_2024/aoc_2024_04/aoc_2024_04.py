class WordSearch:
    def __init__(self, input : str):
        self.character_array : list[list[str]] = []
        self.horizontal_lines : list[str] = []
        self.vertical_lines: list[str] = []

        for index, line in enumerate(input.splitlines()):
            self.horizontal_lines.append(line)
            self.character_array.append([])
            [self.character_array[index].append(x) for x in line]

        self.vertical_lines = ["".join(x) for x in list(zip(*self.character_array, strict=True))]

    def calculate_diagonal(self) -> list[str]:
        lines_list1 : list[str] = []
        lines_list2 : list[str] = []

        m_total = len(self.horizontal_lines)
        n_total = len(self.vertical_lines)
        lines_total = m_total + n_total -1
        print(f"rows: {m_total}, columns {n_total}, lines total {lines_total}")

        for t in range (0, lines_total):
            line1 = ""
            line2 = ""
            for n in range(0, n_total):
                for m in range(0, m_total):
                    if n + m == t:
                        line1 += self.character_array[m][n]
                        line2 += self.character_array[m][n_total-n-1]

            lines_list1.append(line1)
            lines_list2.append(line2)

        return lines_list1 + lines_list2


def countinlines(lines : list[str], key : str):
    reversed_key = key[::-1]
    return sum([line.count(key) + line.count(reversed_key) for line in lines])

def main(input_str : str) -> int:
    input = WordSearch(input_str)
    key = "XMAS"
    diagonals = input.calculate_diagonal()
    count = countinlines(input.horizontal_lines + input.vertical_lines + diagonals, key)

    return count

if __name__ == "__main__":
    count = main("XMAS\nSAMX\n..MM\n.A.A\nS..S\n....")
    print(f'Total count: {count}')