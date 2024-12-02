file = open("day2.txt")
num_of_safe_reports = 0

def check_order(report: list) -> bool:
    inc_sorted = sorted(report)
    dec_sorted = sorted(report, reverse=True)
    return report == inc_sorted or report == dec_sorted

def check_variation(report: list) -> bool:
    try:
        for i in range(len(report) - 1):
            cur_diff = abs(int(report[i]) - int(report[i + 1]))
            if cur_diff < 1 or cur_diff > 3:
                return False
        return True
    except ValueError:
        return False
    
def check_with_one_removal(report: list) -> bool:
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if check_order(new_report) and check_variation(new_report):
            return True
    return False

while True:
    report = file.readline().strip("\n").split(" ")
    if not report or report == [""]:
        break
    try:
        report = [int(x) for x in report if x]
        is_uniform_variation = check_variation(report)
        is_uniform_order = check_order(report)
        is_safe_with_removal = check_with_one_removal(report)
        if (is_uniform_variation and is_uniform_order) or is_safe_with_removal:
            num_of_safe_reports += 1
    except ValueError:
        print(f"Skipping invalid report: {report}")

print(num_of_safe_reports)



file.close()
