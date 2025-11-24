import os

from src.utils.commons import get_aoc_code_path, import_input

def create_aoc_structure(year: int, day: int) -> None:

    # Create directories for code and tests
    code_path = get_aoc_code_path(year, day)    
    os.makedirs(code_path, exist_ok=True)

    # Create empty code and test files if they don't exist
    code_file = code_path / f"aoc_{year}_{day:02d}.py"
    test_file = code_path / f"test_aoc_{year}_{day:02d}.py"
    if not code_file.exists():
        with open(code_file, 'w') as cf:
            cf.write(f"""# Advent of Code {year} - Day {day:02d} solution\n\n
                     def solve_part_1(input : str) -> int:\n    return 0\n\n
                     def solve_part_2(input : str) -> int:\n    return 0\n\n
                     if __name__ == \"__main__\":\n    pass\n""")
    if not test_file.exists():
        with open(test_file, 'w') as tf:
            tf.write(f"""# Tests for Advent of Code {year} - Day {day:02d}\n
                     from src.utils.commons import import_input
                     from src.aoc_{year}.aoc_{year}_{day:02d}.aoc_{year}_{day:02d} import solve_part_1, solve_part_2\n\n

                     YEAR = {year}
                     DAY = {day}\n\n

                     def test_part_1_example():
                        assert solve_part_1(example) == 0

                    def test_part_2_example():
                        assert solve_part_2(example) == 0

                    def test_part_1_input():
                        input = import_input(year=YEAR, day=DAY)

                        result = solve_part_1(input)
                        print(f"Part 1 result: {{result}}")
                        assert result == 0

                    def test_part_2_input():
                        input = import_input(year=YEAR, day=DAY)

                        result = solve_part_2(input)
                        print(f"Part 2 result: {{result}}")
                        assert result == 0

                     """)
    
    # Fethch input data from web
    import_input(year, day)

    print(code_path)

if __name__ == "__main__":
    DAY = 6
    YEAR = 2024
    create_aoc_structure(YEAR, DAY)