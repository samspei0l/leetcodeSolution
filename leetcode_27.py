'''
Optimal Solution: The question simply says if the number at given index != val then remove that
from the array and keep the remaining element of the array and count the no of remaining element
We define k for the no of elements != val. We iterate through every element in nums to check either
it's equal to val or not. If not then we add those value to nums[k] i.e we generate the same array with value
which are not equal to val and we keep increasing k by 1. Finally we return the no of occurence of k.
'''


def leetcode27(nums, val):
    n = len(nums)
    k = 0
    for i in range(n):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    print(k)


def main():
    nums = [3, 2, 2, 3]
    val = 3
    leetcode27(nums, val)


if __name__ == "__main__":
    main()
