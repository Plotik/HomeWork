data = [7, 3, 2, 5, 5, 7, 1, 2, 6]
print(data)
data_lenght = len(data)
for counter in range(data_lenght):
    for idx in range(1, data_lenght - counter):
        prev = data[idx - 1]
        curr = data[idx]
        if prev > curr:
            data[idx], data[idx - 1] = prev, curr
print(data)