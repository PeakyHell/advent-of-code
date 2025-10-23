def count_floors(file_path):
    result = 0

    with open(file_path) as f:
        file = f.read()
        lines = file.splitlines()
        for line in lines:
            for i in range(0, len(line)):
                match line[i]:
                    case "(":
                        result += 1
                    case ")":
                        result -= 1
                if (result == -1):
                    return i+1
    return result

print(count_floors("day1.txt"))
