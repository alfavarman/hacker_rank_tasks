list1 = [[11, 2, 4],
         [4, 5, 6],
         [10, 8, -12]]


def diagonalDifference(arr):
    # elements to add:
    elemens_range = len(arr)
    max_index = elemens_range - 1
    a = 0
    b = 0
    for i in range(elemens_range):
        a += arr[i][i]
        b += arr[i][max_index-i]
    # a = arr[0][0]+arr[1][1]+arr[2][2]
    # b = arr[0][2]+arr[1][1]+arr[2][0]
    result = abs(a-b)
    return result


print(diagonalDifference(list1))
