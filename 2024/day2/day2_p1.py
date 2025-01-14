def get_reports(file_path):
    with open(file_path, 'r') as f:
        file = f.read()
        reports = file.splitlines()
        for i in range(0, len(reports)):
            reports[i] = reports[i].split(" ")

    for i in range(0, len(reports)):
        for j in range(0, len(reports[i])):
            reports[i][j] = int(reports[i][j])

    return reports


def is_valid(report):

    increasing = report[0] - report[1] < 0

    # Ensure all increasing or all decreasing
    for i in range(0, len(report) - 1):
        if increasing:
            if report[i] > report[i + 1]:
                return False
            
        if not increasing:
            if report[i] < report[i + 1]:
                return False

    # Ensure levels differing
    for i in range(0, len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if 1 <= diff <= 3:
            continue
        else:
            return False

    return True

def count_safe_reports(file_path):

    reports = get_reports(file_path)
    count = 0

    for report in reports:
        if is_valid(report):
            count += 1
    return count


print(count_safe_reports("./2024/day2/day2_p1.txt"))