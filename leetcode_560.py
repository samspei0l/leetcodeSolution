'''
<<<<<<< HEAD
The Brute Force Solution and Better Solution are kind of similar.
In Brute Force Solution we generate the subarray from i -> j. So
generally we use two for loop to generate the subarray and one for
loop to find the sum of it. So TC - O(N*N*N). For Better Solution we
just removed the last for loop and we generate the sum as well as the
subarray in second for loop. This gives us the TC- O(N*N). 
'''
'''
For Optimal Solution: We use a method called prefix sum of array. In
prefix sum of array we find the sum of array and then we look for the
previous sum of array i.e if S = 6 and K = 2 then the remaining sum of
the sub array will be S - K i.e (6 - 2).

'''
def leetcode560Optimal(nums,k):
    mpp = {}
    prefixSum = 0
    count = 0
    mpp[0] = 1
    for i in range(len(nums)):
        prefixSum += nums[i]
        remove = prefixSum - k
        count += mpp[remove]
        mpp[prefixSum] += 1
    return count

def main():
    nums = [1,1,1]
    k = 2
    leetcode560Optimal(nums,k)


if __name__ == "__main__":
    main()
=======
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
>>>>>>> d40a5915dff0e953e2dc57abb14e94030ce412b8
