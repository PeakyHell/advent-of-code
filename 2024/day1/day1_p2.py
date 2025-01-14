from day1_p1 import get_columns

def occurences_in_right(value, right_col):
    occurence = 0
    for i in right_col:
        if i == value:
            occurence += 1

    return occurence

def similarity(file_path):
    left_col, right_col = get_columns(file_path)
    left_col.sort()
    occurences = {}

    for value in left_col:
        if not value in occurences:
            occurences[value] = occurences_in_right(value, right_col)

    similarity_value = 0

    for key in occurences.keys():
        similarity_value += key * occurences.get(key)

    return similarity_value

print(similarity("./2024/day1/day1_p1.txt"))