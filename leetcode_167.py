def leetcode167Optimal(nums, target):
    n = len(nums)
    i, j = 0, n - 1
    while i < j:
        if nums[i] + nums[j] == target:
            print(i+1, j+1)
        if nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1


def main():
    nums = [2, 7, 11, 15]
    target = 9
    leetcode167Optimal(nums, target)


if __name__ == "__main__":
    main()
