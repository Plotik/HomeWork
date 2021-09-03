def get_uniq(data, keys):
    uniq = []
    result = []

    for dataset in data:
        for key, values in dataset.items():
            if key in keys:
                if dataset[key] not in uniq:
                    uniq.append(dataset[key])
                    if dataset not in result:
                        result.append(dataset)
    return result


data = [
    {"Имя": "Маша", "Фамилия": "Иванова", "Возраст": 27},
    {"Имя": "Маша", "Фамилия": "Иванова", "Возраст": 28},
    {"Имя": "Маша", "Фамилия": "Петрова", "Возраст": 27},
    {"Имя": "Маша", "Фамилия": "Сидорова", "Возраст": 27},
]
keys = ["Имя", "Фамилия"]

for norm_view in get_uniq(data, keys):
    print(norm_view)