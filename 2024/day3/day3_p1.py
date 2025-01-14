import re

def get_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_list_of_regex(content, regex):
    return re.findall(regex, content)

def clean_file_content(file_path):
    content = get_file(file_path)
    
    lst = get_list_of_regex(content, r"mul\(\d{1,3},\d{1,3}\)")

    sum = 0
    
    for mul in lst:
        mul = mul.strip("mul()").split(",")
        sum += int(mul[0]) * int(mul[1])
    
    return sum


print(clean_file_content("./2024/day3/day3.txt"))