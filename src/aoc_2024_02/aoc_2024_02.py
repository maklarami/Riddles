class Report:
    def __init__(self, input):
        self.report : list[int] = []

        if isinstance(input, str):
            string_list = input.split(" ")
            self.report = [int(s) for s in string_list]

        elif isinstance(input, list):
            if all(isinstance(i, int) for i in input):
                self.report = input
            else:
                raise TypeError("List input must contain only integers.")

        else:
            raise TypeError("Input must be a string or a list of integers.")

        self.differences : list[int] = []
        self.difference_is_allowed : list[bool] = []
        self.step_is_increasing : list[bool] = []
        self.step_is_decreasing : list[bool] = []
        self.calculate_differences()

    def calculate_differences(self):

        self.differences = [y - x for x, y in zip(self.report[:-1], self.report[1:])]

        for difference in self.differences:
            self.difference_is_allowed.append(abs(difference) <= 3)
            self.step_is_increasing.append(difference > 0)
            self.step_is_decreasing.append(difference < 0)

        return True

    def direction_change(self) -> int | bool:
        """Return index of position after which the direction change occours"""
        index = 0

        if self.differences[index] == 0:
                return index

        for x, y in zip(self.differences, self.differences[1:]):
            index += 1
            if y == 0:
                return index
            elif (x > 0 and y > 0) or (x < 0 and y < 0):
                continue
            else:
                return index

        return False

    def is_safe(self) -> bool:

        if all(self.difference_is_allowed):
            if any([all(self.step_is_increasing), all(self.step_is_decreasing)]):
                return True

        return False

def check_after_index_removal(input: Report, index : int) -> bool:
    new_input = input.report[:]
    new_input.pop(index)
    new_report = Report(new_input)

    if new_report.is_safe():
        return True

    return False

def is_safe_with_dampener(input : Report) -> bool:
    error_index : int | bool = False

    if input.difference_is_allowed.count(False):
        error_index = input.difference_is_allowed.index(False)
    else:
        error_index = input.direction_change()

    if type(error_index) == type(2):
        if check_after_index_removal(input, error_index):
            return True
        elif check_after_index_removal(input, error_index +1):
            return True
        elif error_index == 0:
            return False
        elif check_after_index_removal(input, error_index -1):
            return True

    return False

def main(input : str, use_dampener : bool) -> int:
    safe_reports = 0
    results : list[int] = []

    for line in input.splitlines():
        report = Report(line)
        if report.is_safe():
            safe_reports += 1
            results.append(1)
        elif use_dampener:
            if is_safe_with_dampener(report):
                safe_reports += 1
                results.append(2)
            else:
                results.append(0)

    return safe_reports

if __name__ == "__main__":
    main("71 69 70 71 72 75", True)
