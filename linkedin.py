# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
#
# #Desired output
# [('Apples', 5, 1.50),
# ('Oranges', 3, 2.25),
# ('Bananas', 4, 0.89)]


def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)


print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

