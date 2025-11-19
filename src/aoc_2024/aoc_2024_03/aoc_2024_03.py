import pathlib
import re
import numpy as np

def main(input : str) -> int:

    pattern1 = "mul\(\d{1,3},\d{1,3}\)"
    pattern2 = "do\(\)"
    pattern3 = "don't\(\)"
    pattern = pattern1 + "|" + pattern2 + "|" + pattern3
    results : list[str] = re.findall(pattern, input)

    array_of_strings = []

    do_multiply = True
    for value in results:
        if value == "do()":
            do_multiply = True
        elif value == "don't()":
            do_multiply = False
        elif do_multiply:
            array_of_strings.append(value[4:-1].split(","))

    array = np.array(array_of_strings).astype(np.int_)

    return sum(np.prod(array,1))

if __name__ == "__main__":
    print(main("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))

    file_name = "input.txt"
    script_dir = pathlib.Path(__file__).parent

    with open(script_dir / "input.txt", 'r', encoding='utf-8') as file:
        data_string = file.read()

    print(main(data_string))