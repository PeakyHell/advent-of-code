from day3_p1 import get_file, get_list_of_regex

def calculate_muls_sum_with_conditions(file_path):
    content = get_file(file_path)
    lst = get_list_of_regex(content, r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    do = True
    sum = 0

    for i in lst:
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False
        elif do:
            mul = i.strip("mul()").split(",")
            sum += int(mul[0]) * int(mul[1])
        else:
            continue
    return sum


print(calculate_muls_sum_with_conditions("./2024/day3/day3.txt"))