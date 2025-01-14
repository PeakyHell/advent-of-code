def get_columns(file_path):
    left_locations = []
    right_locations = []

    with open(file_path, 'r') as f:
        file = f.read()
        lines = file.splitlines()
        for line in lines:
            ids = line.split("   ")
            left_locations.append(int(ids[0]))
            right_locations.append(int(ids[1]))

    return left_locations, right_locations

def total_distance(file_path):
    left_locations, right_locations = get_columns(file_path)
    distances = []

    left_locations.sort()
    right_locations.sort()
    
    for i in range(0, len(left_locations)):
        left = left_locations[i]
        right = right_locations[i]

        distances.append(max(left, right) - min(left, right))

    total_sum = 0
    for d in distances:
        total_sum += d
    
    return total_sum

print(total_distance("./2024/day1/day1_p1.txt"))