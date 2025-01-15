def get_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def file_content_to_matrix(file_path):
    content = get_file_content(file_path)
    matrix = content.split("\n")
    for i in range(0, len(matrix)):
        matrix[i] = list(matrix[i])
    return matrix


def count_in_line(line):
    count = 0
    for i in range(0, len(line) - 3):
        if line[i:i+4] == "XMAS" or line[i:i+4] == "SAMX":
            count += 1
    return count


def search_in_line(matrix, index):
    line = matrix[index]
    return count_in_line(line)


def search_in_column(matrix, index):
    line = ""
    for i in range (0, len(matrix)):
        line += matrix[i][index]

    return count_in_line(line)


def search_in_left_right_diagonal(matrix, line_index, col_index):
    line = ""
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, min(rows - line_index, cols - col_index)):
        line += matrix[line_index + i][col_index + i]

    return count_in_line(line)


def search_in_right_left_diagonal(matrix, line_index, col_index):
    line = ""
    rows = len(matrix)

    for i in range(0, min(rows - line_index, col_index + 1)):
        line += matrix[line_index + i][col_index - i]

    return count_in_line(line)


def count_occurences_in_file(file_path):
    matrix = file_content_to_matrix(file_path)
    count = 0

    rows = len(matrix)
    cols = len(matrix[0])

    for line in matrix:
        line = "".join(line)
        count += count_in_line(line)

    for i in range(cols):
        count += search_in_column(matrix, i)

    for i in range(cols):
        count += search_in_left_right_diagonal(matrix, 0, i)
        count += search_in_right_left_diagonal(matrix, 0, i)
    
    for i in range (1, rows):
        count += search_in_left_right_diagonal(matrix, i, 0)
        count += search_in_right_left_diagonal(matrix, i, cols - 1)
    
    return count

print(count_occurences_in_file("./2024/day4/day4.txt"))
