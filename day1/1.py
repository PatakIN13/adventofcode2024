def calculate_total_distance_from_file(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    return total_distance

file_path = './input.txt'
result = calculate_total_distance_from_file(file_path)
print(f"Total distance: {result}")
