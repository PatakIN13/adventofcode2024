from collections import Counter


def calculate_similarity_score_from_file(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    right_counts = Counter(right_list)

    similarity_score = sum(num * right_counts[num] for num in left_list)
    return similarity_score


file_path = 'input.txt'
result = calculate_similarity_score_from_file(file_path)
print(f"Similarity score: {result}")
