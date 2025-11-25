import os
import textwrap

from src.utils.commons import get_aoc_code_path, import_input

def create_aoc_structure(year: int, day: int) -> None:

    # Create directories for code and tests
    code_path = get_aoc_code_path(year, day)    
    os.makedirs(code_path, exist_ok=True)

    # Define file paths
    code_file = code_path / f"aoc_{year}_{day:02d}.py"
    test_file = code_path / f"test_aoc_{year}_{day:02d}.py"
    
    # Create empty code and test files if they don't exist
    if not code_file.exists():
        code_content = textwrap.dedent(f"""
            # Advent of Code {year} - Day {day:02d} solution
            
            def solve_part_1(input : str) -> int:
                # Add your Part 1 solution logic here
                return 0
            
            def solve_part_2(input : str) -> int:
                # Add your Part 2 solution logic here
                return 0
            
            if __name__ == "__main__":
                pass
            """)

        with open(code_file, 'w') as cf:
            cf.write(code_content.lstrip('\n'))
    if not test_file.exists():
        test_content = textwrap.dedent(f"""
            # Tests for Advent of Code {year} - Day {day:02d}
            from src.utils.commons import import_input
            from src.aoc_{year}.aoc_{year}_{day:02d}.aoc_{year}_{day:02d} import solve_part_1, solve_part_2
            
            YEAR = {year}
            DAY = {day}
            
            # Placeholder for example input data (must be defined in your actual test runner context)
            example = "Example data for testing" 

            def test_part_1_example():
                # Change 0 to the expected answer
                assert solve_part_1(example) == 0

            def test_part_2_example():
                # Change 0 to the expected answer
                assert solve_part_2(example) == 0

            def test_part_1_input():
                input = import_input(year=YEAR, day=DAY)

                result = solve_part_1(input)
                print(f"Part 1 result: {{result}}")
                # Change 0 to the expected answer when ready
                assert result == 0 

            def test_part_2_input():
                input = import_input(year=YEAR, day=DAY)

                result = solve_part_2(input)
                print(f"Part 2 result: {{result}}")
                # Change 0 to the expected answer when ready
                assert result == 0

            """)
        with open(test_file, 'w') as tf:
            tf.write(test_content.lstrip('\n'))
    
    # Fethch input data from web
    import_input(year, day)

    print(code_path)

if __name__ == "__main__":
    DAY = 6
    YEAR = 2024
    create_aoc_structure(YEAR, DAY)