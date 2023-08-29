'''
In this question we have an array of integers and we have to find
next permutation of the given array of integers. For eg.
arr[1,2,3] next permuation is arr[1,3,2]
Brute Force Solution: First we will generate all the subarray from given
array and then we will do linear search to find the given array and
then we will print the array next to give array. If the given array is
itself last in generated list of subarray then we print the first generated
subarray.
Optimal Solution: To solve this problem with most optimal solution is to
find the longer prefix match then find the value in array which is greater
than the prefix match but closest to smallest one. After that we place back
the array in reverse sorted way.
'''


def leetcode31Optimal(arr):
    n = len(arr)
    index = -1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            index = i
            break
    if (index == -1):
        arr.reverse()
        print(arr)
    for i in range(n-1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break

    arr[index+1:] = reversed(arr[index+1:])
    print(arr)


def main():
    arr = [1, 2, 3]
    leetcode31Optimal(arr)


if __name__ == "__main__":
    main()
