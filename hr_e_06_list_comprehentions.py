# List Comprehensions
# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
#
# Example
#
#
#
#
# All permutations of  are:
# .
#
# Print an array of the elements that do not sum to .
#
#
# Input Format
#
# Four integers  and , each on a separate line.
#
# Constraints
#
# Print the list in lexicographic increasing order.
#
# Sample Input 0
#
# 1
# 1
# 1
# 2
# Sample Output 0
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0
#
# Each variable  and  will have values of  or . All permutations of lists in the form .
# Remove all arrays that sum to  to leave only the valid permutations.

if __name__ == '__main__':
    x, y, z, n = (int(input()) for _ in range(4))

    print([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n])
