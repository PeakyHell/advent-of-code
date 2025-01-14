from day2_p1 import get_reports, is_valid

def count_safe_reports_with_tolerance(file_path):
    reports = get_reports(file_path)
    count = 0

    for report in reports:
        if is_valid(report):
            count += 1
        else:
            for i in range(0, len(report)):
                temp = list(report)
                del temp[i]
                if is_valid(temp):
                    count += 1
                    break
    return count

print(count_safe_reports_with_tolerance("./2024/day2/day2.txt"))
