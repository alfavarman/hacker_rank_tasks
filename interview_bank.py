egzaminy = [
    {"karol": 5, "john": 3, "adam": 4},
    {"adam": 4, "karol": 2},
    {"jacek": 2},
]
dict_1 = egzaminy[0]
dict_2 = egzaminy[1]
dict_3 = egzaminy[2]


def merged_dict(dict1: dict, dict2: dict, dict3: dict) -> dict:
    merged_d = {**dict1, **dict2, **dict3}
    for key, value in merged_d.items():
        if key in dict1 and key in dict2 and key in dict3:
            merged_d[key] = (value + dict1[key] + dict2[key]) / 3
        if key in dict1 and key in dict2:
            merged_d[key] = (value + dict1[key]) / 2
        if key not in dict1 and key in dict2 and key in dict3:
            merged_d[key] = (value + dict1[key]) / 2
    return merged_d


averages_score_dict = merged_dict(dict_1, dict_2, dict_3)
sorted_list_of_averages = sorted(averages_score_dict.values(), reverse=True)
students_average_high_low = []
for value1 in sorted_list_of_averages:
    for name, values in averages_score_dict.items():
        if value1 == values:
            students_average_high_low.append(name)

print(students_average_high_low)
