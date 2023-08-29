'''
Brute Force Solution: Here we iterate through the array of size n x m.
If there is an element which is zero then we mark the row and col of that
element as -1 and keep iterating through the array. Once we are done
iterating then we completed to mark the row and col we iterate once more
inside the array of size n x m and make every -1 to 0.
'''


def markRow(matrix, n, m, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


def markCol(matrix, n, m, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


def leetcode73(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == - 1:
                matrix[i][j] = 0
    print(matrix)


'''
Better Solution: Here we take two new array row and col respectively.
We iterate through array of size n x m and then we mark the row[i] and col[i]
with 1 of every element which is equal to zero. Once the marking is done we
again iterate through array of size n x m and make those 1 to zero. Here we are
using two extra array to store and mark row and col respectively.
'''


def leetcode73Better(matrix, n, m):
    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0
    print(matrix)


'''
Optimal Solution:
'''


def leetcode73Optimal(matrix, n, m):
    col0 = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    print(matrix)


def main():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    n = len(matrix)
    m = len(matrix[0])
    leetcode73Optimal(matrix, n, m)


if __name__ == "__main__":
    main()
