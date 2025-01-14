def total_distance(file_path):
    left_locations = []
    right_locations = []
    distances = []

    with open(file_path, 'r') as f:
        file = f.read()
        lines = file.splitlines()
        for line in lines:
            ids = line.split("   ")
            left_locations.append(int(ids[0]))
            right_locations.append(int(ids[1]))

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

print(total_distance("./2024/txt_files/day1.txt"))