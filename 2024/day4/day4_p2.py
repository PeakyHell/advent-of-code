from day4_p1 import get_file_content, file_content_to_matrix

def three_by_three_matrix_to_string(matrix, row_index, col_index):
    str = ""
    for i in range(3):
        for j in range(3):
            str += matrix[row_index + i][col_index + j]
        str += "\n"
    return str.strip("\n")


def string_match_pattern(string, pattern):
    for i in range(len(string)):
        if pattern[i] == '.':
            continue
        elif pattern[i] != string[i]:
            return False
    return True


def string_match_multiple_patterns(string, patterns):
    for pattern in patterns:
        if string_match_pattern(string, pattern):
            return True
    return False


def count_x_mas_occurences_in_file(file_path):
    patterns = [ "M.S\n.A.\nM.S", "M.M\n.A.\nS.S", "S.M\n.A.\nS.M", "S.S\n.A.\nM.M"]

    matrix = file_content_to_matrix(file_path)

    count = 0

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, rows - 2):
        for j in range (0, cols - 2):
            string = three_by_three_matrix_to_string(matrix, i, j)
            if string_match_multiple_patterns(string, patterns):
                count += 1
    return count

print(count_x_mas_occurences_in_file("./2024/day4/day4.txt"))