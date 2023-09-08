def leetcode704(nums, target):
    n = len(nums)
    start, end = 0, n - 1
    mid = (start+end) // 2
    if target > nums[mid]:
        mid = ((mid+1)+end) // 2
    else:
        mid = (start+(mid+1)) // 2


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    leetcode704(nums, target)


if __name__ == "__main__":
    main()
