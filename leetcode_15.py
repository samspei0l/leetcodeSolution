'''
Brute Force:
    First, we will declare a set data structure as we want unique triplets.
    Then we will use the first loop(say i) that will run from 0 to n-1.
    Inside it, there will be the second loop(say j) that will run from i+1 to n-1.
    Then there will be the third loop(say k) that runs from j+1 to n-1.
    Now, inside these 3 nested loops, we will check the sum i.e. arr[i]+arr[j]+arr[k], and if it is equal to the target i.e. 0 we will sort this triplet and insert it in the set data structure.
    Finally, we will return the list of triplets stored in the set data structure.
'''


def leetcode15Brute(nums):
    n = len(nums)
    res = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans = [nums[i], nums[j], nums[k]]
                    ans.sort()
                    res.add(tuple(ans))
    temp = [list(item) for item in res]
    print(temp)


'''
Better Solution:
    First, we will declare a set data structure as we want unique triplets.
    Then we will use the first loop(say i) that will run from 0 to n-1.
    Inside it, there will be the second loop(say j) that will run from i+1 to n-1.
    Before the second loop, we will declare another HashSet to store the array elements as we intend to search for the third element using this HashSet.
    Inside the second loop, we will calculate the value of the third element i.e. -(arr[i]+arr[j]).
    If the third element exists in the HashSet, we will sort these 3 values i.e. arr[i], arr[j], and the third element, and insert it in the set data structure declared in step 1.
    After that, we will insert the j-th element i.e. arr[j] in the HashSet as we only want to insert those array elements that are in between indices i and j.
    Finally, we will return a list of triplets stored in the set data structure.
'''


def leetcode15Better(nums):
    mpp = set()
    n = len(nums)
    for i in range(n):
        hashset = set()
        for j in range(i+1, n):
            k = - (nums[i]+nums[j])
            if k in hashset:
                temp = [nums[i], nums[j], k]
                temp.sort()
                mpp.add(tuple(temp))
            hashset.add(nums[j])
    ans = list(mpp)
    print(ans)


'''
Optimal Solution:
    First, we will sort the entire array.
    We will use a loop(say i) that will run from 0 to n-1. This i will represent the fixed pointer. In each iteration, this value will be fixed for all different values of the rest of the 2 pointers. Inside the loop, we will first check if the current and the previous element is the same and if it is we will do nothing and continue to the next value of i.
    After that, there will be 2 moving pointers i.e. j(starts from i+1) and k(starts from the last index). The pointer j will move forward and the pointer k will move backward until they cross each other while the value of i will be fixed.
        Now we will check the sum i.e. arr[i]+arr[j]+arr[k].
        If the sum is greater, then we need lesser elements and so we will decrease the value of k(i.e. k–). 
        If the sum is lesser than the target, we need a bigger value and so we will increase the value of j (i.e. j++). 
        If the sum is equal to the target, we will simply insert the triplet i.e. arr[i], arr[j], arr[k] into our answer and move the pointers j and k skipping the duplicate elements(i.e. by checking the adjacent elements while moving the pointers).
    Finally, we will have a list of unique triplets.
'''


def leetcode15Optimal(nums):
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = n - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
    print(ans)


def main():
    nums = [-2, 0, 1, 1, 2]
    # leetcode15Brute(nums)
    # leetcode15Better(nums)
    leetcode15Optimal(nums)


if __name__ == "__main__":
    main()
