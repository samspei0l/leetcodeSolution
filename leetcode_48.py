'''
Brute Force Solution: We create an array of size n x n.
We iterate through array for i -> n and for j -> n.
we perform an operation ans[j][n-i-1] = matrix[i][j] and return the ans
'''


def leetcode48(matrix, n):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[j][n - i - 1] = matrix[i][j]
    print(ans)


'''
Optimal Solution: We Transponse the given matrix i.e changing row to col and
col to row. After transponse we just reverse the matrix and return the matrix
'''


def leetcode48Optimal(matrix, n):
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    print(matrix)


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = len(matrix)
    leetcode48Optimal(matrix, n)


if __name__ == "__main__":
    main()
