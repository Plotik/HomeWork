wall =[
    [3, 1, 2],
    [6]
]
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
    else:
        pass
total = len(wall) - max_value
if max_value != 0 and total != 0:
    print("Наименьшее количество пересечений кирпичей:", len(wall)-max_value)
else:
    print("Пересечений кирпичей нет")