'''
This question has only one solution
We can see we have to print the matrix in spiral form.
We can take row[0] as top col[0] as left, matrix[row-1] as bottom and
matrix[col-1] as right. We are performing the operatin in left -> right then
top -> bottom then right -> left then bottom -> top to form spiral form.
We do this operation until top <= bottom and left <= right. Once we conver the
first spiral operation i.e left -> right , top -> bottom, right -> left and
bottom -> top. We move our top by 1 if top <= bottom and we move our left by 1
if left <= right. We decrease our bottom and right by 1.
'''


def leetcode54(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = []
    top = 0
    left = 0
    right = n - 1
    bottom = m - 1
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
    print(ans)


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    leetcode54(matrix)


if __name__ == "__main__":
    main()
