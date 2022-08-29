if __name__ == '__main__':
    import sys

    list_with_names: list = []
    list_with_scores: list = []
    list_with_sorted_scores: list = []

    for _ in range(int(input())):
        name: str = input()
        score = float(input())
        list_with_names.append(name)
        list_with_scores.append(score)

    num_grades: int = len(list_with_scores)

    for number in list_with_scores:
        list_with_sorted_scores.append(number)

    list_with_sorted_scores.sort()


    def find_smallest(list_with_sorted_scores: list) -> float:
        smallest_score: int = sys.maxsize
        for score in list_with_sorted_scores:
            if score < smallest_score:
                smallest_score = score
        return smallest_score


    smallest_score: float = find_smallest(list_with_sorted_scores)

    for score in list_with_sorted_scores:
        if score == smallest_score:
            list_with_sorted_scores.remove(smallest_score)

    second_smallest: float = find_smallest(list_with_sorted_scores)

    list_with_positions: list = []
    list_with_sorted_names: list = []

    index = 0
    while index < len(list_with_scores):
        if list_with_scores[index] == second_smallest:
            list_with_positions.append(index)
        index += 1

    if len(list_with_positions) == 1:
        print(list_with_names[list_with_positions[0]])

    elif len(list_with_positions) > 1:
        for value in list_with_positions:
            list_with_sorted_names.append(list_with_names[value])

    list_with_sorted_names.sort()
    for name in list_with_sorted_names:
        print(name)

