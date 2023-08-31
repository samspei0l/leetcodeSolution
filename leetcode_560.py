'''
Brute Force Solution and Better Solution: In this problem we generate
all the subarray from the given array and then we add those subarray
to get the sum and if the sum == k then we increase our count by 1 i.e
if there are two subarray whose sum == k then the count will be 2.
'''


def leetcode560BruteBetter(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        prefixSum = 0
        for j in range(n):
            prefixSum += nums[i:j+1]
            if prefixSum == k:
                count += 1
    return count


'''
Optimal Solution: For Optimal Solution we use a technique called prefixSum.
This technique states that if the sum of all the elements in array is S and
the sum of given k no of elements ending at last index of array is k then the
remaining sum of the element will be S - K.
'''


def leetcode560Optimal(nums, k):
    count = 0
    prefixSum = 0
    d = {0: 1}
    for num in nums:
        prefixSum += num
        if prefixSum - k in d:
            count = count + d[prefixSum - k]
        if prefixSum not in d:
            d[prefixSum] = 1
        else:
            d[prefixSum] = d[prefixSum] + 1
    print(count)


def main():
    nums = [-1, -1, 1]
    k = 0
    leetcode560Optimal(nums, k)


if __name__ == "__main__":
    main()
