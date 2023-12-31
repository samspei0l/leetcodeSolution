'''
Brute Force Solution. Here we take two array postive and negative and
add values which are positive in positive array and negative in negative array
after that we run a for loop to add back those element in array arr // 2 length
but we can see there is pattern that positive array will be in even indexes and
negative array will be in odd indexes.
'''


def leetcode2149(arr):
    positive = []
    negative = []
    for i in range(len(arr)):
        if arr[i] < 0:
            negative.append(arr[i])
        else:
            positive.append(arr[i])
    for i in range(len(arr) // 2):
        arr[2 * i] = positive[i]
        arr[2 * i + 1] = negative[i]
    print(arr)


'''
For Optimal Solution: In above solution we did two pass but here we will solve
it in one pass. To do that we know that positive element will be at even
indexes and negative element will be at odd indexes. We can start our positive
index at 0 and negative indexes at 1. If the element is negative we add it to
negative array and increase the negativeIndex by 2 and similarly if we have
positive element we add it to positive array and increase positive index by 2.
'''


def leetcode2149Opt(arr):
    n = len(arr)
    posIndex, negIndex = 0, 1
    ans = [0] * n
    for i in range(n):
        if arr[i] < 0:
            ans[negIndex] = arr[i]
            negIndex += 2
        else:
            ans[posIndex] = arr[i]
            posIndex += 2
    print(arr)


'''
There is another variety for this question.
Where an array has more positive than negative numbers or vice-versa
for example arr[2,3,-1,-2,4,5]. Here as we can see there are more positive
numbers than negative numbers and we have to the same operation on the array
were we will write the array in positive negative form and add remaining values
at the end.
'''


def leetcode2149Variety(arr):
    positive = []
    negative = []
    for i in range(len(arr)):
        if arr[i] < 0:
            negative.append(arr[i])
        else:
            positive.append(arr[i])

    if len(positive) > len(negative):
        for i in range(len(negative)):
            arr[2*i] = positive[i]
            arr[2*i+1] = negative[i]
        index = len(negative) * 2
        for i in range(len(negative), len(positive)):
            arr[index] = positive[i]
            index += 1
    else:
        for i in range(len(positive)):
            arr[2*i] = positive[i]
            arr[2*i+1] = negative[i]
        index = len(positive)
        for i in range(len(positive), len(negative)):
            arr[index] = negative[i]
            index += 1

    print(arr)


def main():
    arr = [-1, 2, 3, 4, -3, 1]
    # leetcode2149(arr)
    # leetcode2149Opt(arr)
    leetcode2149Variety(arr)


if __name__ == "__main__":
    main()
