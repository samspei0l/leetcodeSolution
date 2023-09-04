'''
Brute Force Solution:
    We will run a loop that will select the elements of the array one by one.
    Now, for each unique element, we will run another loop and count its occurrence in the given array.
    If any element occurs more than the floor of (N/3), we will include it in our answer. 
    While traversing if we find any element that is already included in our answer, we will just skip it.
'''


from collections import Counter


def leetcode229Brute(nums):
    n = len(nums)
    ans = []
    for i in range(n):
        if len(ans) == 0 or ans[0] != nums[i]:
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            if count > n // 3:
                ans.append(nums[i])
        if len(ans) == 2:
            break
    print(ans)


'''
Better Approach:
    Use a hashmap and store the elements as <key, value> pairs. (Can also use frequency array based on the size of nums).
    Here the key will be the element of the array and the value will be the number of times it occurs. 
    Traverse the whole array and update the occurrence of each element. 
    After that, check the map if the value for any element is greater than the floor of N/3. 
        If yes, include it in the list. 
        Else iterate forward.
    Finally, return the list.

'''


def leetcode229Better2(nums):
    mpp = {}
    n = len(nums)
    for i in range(n):
        mpp += mpp[nums[i]]
    print(mpp)


def leetcode229Better(nums):
    mpp = Counter(nums)
    n = len(nums)
    count = 0
    for i, count in mpp.items():
        if count > n // 3:
            print(i)


'''
Optimal Solution:
Initialize 4 variables:
cnt1 & cnt2 –  for tracking the counts of elements
el1 & el2 – for storing the majority of elements.
Traverse through the given array.

    If cnt1 is 0 and the current element is not el2 then store the current element of the array as el1 along with increasing the cnt1 value by 1.
    If cnt2 is 0 and the current element is not el1 then store the current element of the array as el2 along with increasing the cnt2 value by 1.
    If the current element and el1 are the same increase the cnt1 by 1.
    If the current element and el2 are the same increase the cnt2 by 1.
    Other than all the above cases: decrease cnt1 and cnt2 by 1.

The integers present in el1 & el2 should be the result we are expecting. So, using another loop, we will manually check their counts if they are greater than the floor(N/3).
'''


def leetcode229Optimal(nums):
    element1 = 0
    element2 = 0
    count1 = 0
    count2 = 0
    ans = []
    for i in range(len(nums)):
        if count1 == 0 and nums[i] != element2:
            element1 = nums[i]
            count1 = 1
        elif count2 == 0 and nums[i] != element1:
            count2 = 1
            element2 = nums[i]
        elif element1 == nums[i]:
            count1 += 1
        elif element2 == nums[i]:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

        if count1 > len(nums) // 3:
            ans.append(element1)
        if count2 > len(nums) // 3:
            ans.append(element2)
    print(ans)


def leetcode229Optimal2(nums):
    unique = set(nums)
    n = len(nums)
    res = []
    for element in unique:
        if nums.count(element) > n // 3:
            res.append(element)
    print(res)


def main():
    nums = [3, 2, 3]
    # leetcode229Brute(nums)
    # leetcode229Better2(nums)
    # leetcode229Optimal(nums)
    leetcode229Optimal2(nums)


if __name__ == "__main__":
    main()
