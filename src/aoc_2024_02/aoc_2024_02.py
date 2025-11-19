class Report:
    def __init__(self, input : str):
        string_list = input.split(" ")
        self.report = [int(s) for s in string_list]

    def is_safe(self) -> bool:
        differences = [x - y for x, y in zip(self.report, self.report[1:])]

        if all(abs(x) <= 3 for x in differences):
            if any([all(x < 0 for x in differences), all(x > 0 for x in differences)]):
                return True

        return False

def main(input : str) -> int:
    safe_reports = 0

    for line in input.splitlines():
        report = Report(line)
        if report.is_safe():
            safe_reports += 1

    print(safe_reports)

    return safe_reports

if __name__ == "__main__":
    main("1 2 3 4 5")