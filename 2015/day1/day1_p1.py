def count_floors(file_path):
    result = 0

    with open(file_path) as f:
        file = f.read()
        lines = file.splitlines()
        for line in lines:
            for char in line:
                match char:
                    case "(":
                        result += 1
                    case ")":
                        result -= 1
    return result

print(count_floors("day1.txt"))
