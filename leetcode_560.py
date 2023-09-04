'''
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