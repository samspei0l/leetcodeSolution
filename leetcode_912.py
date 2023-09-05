'''
Optimal Solution: The question says to solve the question in O(nlog(n)) time.
And we know there are various sorting algorithms that take O(nlog(n)) time.
Here we will use mergeSort sorting algorithm.
The concecpt of mergeSort sorting algorithm is divide and conquer approach.
Divide the array in two equal parts(not exactly equal parts).
This is a recursive divison we divide until we have one single element each.
After we have divided we start merging them back to their original node which is
smaller. Keep doing the same approach until we have sorted the array.
'''


def merge(nums, L, MID, R):
    left, right = nums[L:MID+1], nums[MID+1:R+1]
    i, j, k = L, 0, 0
    while j < len(left) and k < len(right):
        if left[j] < right[k]:
            nums[i] = left[j]
            j += 1
        else:
            nums[i] = right[k]
            k += 1
        i += 1
    while j < len(left):
        nums[i] = left[j]
        j += 1
        i += 1
    while k < len(right):
        nums[i] = right[k]
        k += 1
        i += 1


def leetcode912(nums, l, r):
    if l == r:
        return nums

    mid = (l + r) // 2
    leetcode912(nums, l, mid)
    leetcode912(nums, mid+1, r)
    merge(nums, l, mid, r)
    print(nums)
# print(leetcode912(nums, 0, len(nums)- 1))


def main():
    nums = [5, 1, 1, 2, 0, 0]
    leetcode912(nums, 0, len(nums)-1)


if __name__ == "__main__":
    main()
