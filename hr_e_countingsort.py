
arr = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79]
arr_size = len(arr)
list_indexies = range(0, arr_size)

def countingSort(arr):
    # Write your code here
    arr_size = len(arr)
    list_indexies = range(0, arr_size)
    result = [0]*100
    for i in list_indexies:
        index_to_insert = arr[i]
        value_to_insert = (result[arr[i]]+1)
        result[index_to_insert] += 1
    return result

print(result)
