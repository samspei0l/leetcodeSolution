'''
Brute Force Approach: TC - O(N*N) and SC - O(1) 
    We will run a loop that will select the elements of the array one by one.
    Now, for each element, we will run another loop and count its occurrence in the given array.
    If any element occurs more than the floor of (N/2), we will simply return it.
'''


def leetcode169Brute(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
    if count > n // 2:
        print(nums[i])


'''
Better Solution: TC - O(Nlogn) + O(N) SC - O(N) 
    Use a hashmap and store as (key, value) pairs. (Can also use frequency array based on the size of nums) 
    Here the key will be the element of the array and the value will be the number of times it occurs. 
    Traverse the array and update the value of the key. Simultaneously check if the value is greater than the floor of N/2. 
        If yes, return the key 
        Else iterate forward.
'''


def leetcode169Better(nums):
    n = len(nums)
    mpp = {}
    count = 0
    for key, value in enumerate(nums):
        mpp[key] = value
    for i in range(n):
        if i in mpp:
            count += 1
    if count > n // 2:
        print(nums[i])


'''
Optimal Solution: TC - O(N) SC - O(1)
    Initialize 2 variables:
    Count –  for tracking the count of element
    Element – for which element we are counting
    Traverse through the given array.
        If Count is 0 then store the current element of the array as Element.
        If the current element and Element are the same increase the Count by 1.
        If they are different decrease the Count by 1.
    The integer present in Element should be the result we are expecting
'''


def leetcode169Optimal(nums):
    count, element = 0, 0
    for num in nums:
        if count == 0:
            element = num
        count += (1 if num == element else -1)
    print(element)


def main():
    nums = [1, 2]
    # leetcode169Brute(nums)
    # leetcode169Better(nums)
    leetcode169Optimal(nums)


if __name__ == "__main__":
    main()
