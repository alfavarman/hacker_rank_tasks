arr1 = [0,1,2,4,6,5,3]


def findMedian(arr) -> int:
    # Write your code here
    arr.sort()
    index = (len(arr) / 2)
    index = int(index)
    return index


print(findMedian(arr1))

