def breaks_solution(wall):
    distance_matrix = {}
    for wall_raw in wall:
        distance = 0
        for brick_lenght in wall_raw[:-1]:
            distance += brick_lenght
            if distance not in distance_matrix:
                distance_matrix[distance] = 1
            else:
                distance_matrix[distance] += 1
    max_value = 0
    for elem in distance_matrix:
        if distance_matrix[elem] > max_value:
            max_value = distance_matrix[elem]
    total = len(wall) - max_value

    if total != 0 and max_value != 0:
        return total
    else:
        return 0

wall = [
    [1, 2, 2, 1],
    [3, 1, 2],
    [1, 3, 2],
    [2, 4],
    [3, 1, 2],
    [1, 3, 1, 1],
]

