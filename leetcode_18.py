def leetcode18Brute(nums, target):
    n = len(nums)
    ans = []
    distinc = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        distinc.add(tuple(temp))
    ans = [list(item) for item in distinc]
    print(ans)


def leetcode18Better(nums, target):
    n = len(nums)
    ans = []
    distinct = set()
    for i in range(n):
        for j in range(i+1, n):
            hashset = set()
            for k in range(j+1, n):
                third = target - (nums[i] + nums[j] + nums[k])
                # sum = nums[i] + nums[j] + nums[k] + third
                if third in hashset:
                    temp = [nums[i], nums[j], nums[k], third]
                    # print(temp)
                    temp.sort()
                    distinct.add(tuple(temp))
                hashset.add(nums[k])
    ans = list(distinct)
    print(ans)


def leetcode18Optimal(nums, target):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1
            while k < l:
                sum = nums[i] + nums[j] + nums[k] + nums[l]
                if sum < target:
                    k += 1
                elif sum > target:
                    l -= 1
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l - 1]:
                        l -= 1
    print(ans)


def main():
    nums = [2, 2, 2, 2, 2]
    target = 8
    # leetcode18Brute(nums, target)
    # leetcode18Better(nums, target)
    leetcode18Optimal(nums, target)


if __name__ == "__main__":
    main()
