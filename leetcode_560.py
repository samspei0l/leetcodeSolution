def leetcode560(nums, k):
    count = 0
    ans = []
    for i in range(len(nums)):
        sum_subarray = 0
        for j in range(i, len(nums)):
            ans.append(nums[i:j+1])
            sum_subarray = sum(nums[i:j+1])
            if sum_subarray == k:
                count += 1
    print(count)
    print(ans)


def main():
    nums = [-1, -1, 1]
    k = 0
    leetcode560(nums, k)


if __name__ == "__main__":
    main()
