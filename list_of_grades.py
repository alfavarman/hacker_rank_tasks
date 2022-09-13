gradeslist = list((range(1, 101)))
new = [73, 67, 38, 33]


def gradingStudents(grades):
    def round_to_nearest_5(i):
        numb = round(i / 5) * 5
        return numb

    result = []
    for i in grades:
        if i % 10 == 7 or i % 10 == 6 or i % 10 == 2 or i % 10 == 1 or i < 38:
            result.append(i)
        else:
            result.append(round_to_nearest_5(i))
    return result


print(gradingStudents(new))
