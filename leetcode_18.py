'''
Brute Force: Running for loops for every i , j, k and l.
If theri sum == target then store them in temp and sort the temp
Add the values of temp in set DS for distinct item.
append the items in set to ans of type list. 
TC - O(N^4) ans SC - O(1)
'''


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


'''
Better Solution: We declear a set DS and a list ans. 
Run for loops for i and j and k.
Decleare another set to be used after j. 
We know if we do target - nums[i] + nums[j] + nums[k] we will get the fourth element.
If fourth element is in hashset then add nums[i], nums[j], nums[k], fourth in temp.
Sort the temp and add the values in distinct set DS. If fourth not in hashset then
add the value nums[k] to hashset. At last append the items of distinct to list of ans.
TC - O(N^3*logM) SC- O(2 * No of quadruples)+ O(N)
'''


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


'''
Optimal Solution: Two Pointer Approach
Here we fix i and j and we move k and l throught the array. 
First we will sort the array.
Then we will run a loop for i and check if i != 0 and previous element != to current element.
Similarly we will run a loop for j and check if j > i+1 or not and if previous element at j == current element at j
We define our k as j + 1 because it will start from the index after j and l as len(array) - 1 as it will start at the end of array.
While k < l: We find the sum of all the array i.e nums[i], nums[j], nums[k] and nums[l]
If the given sum is > target we decrease our l. If the sum < target we increase our k.
If the sum == target then we add the values to temp. and increase our k and decrease our l for next iteration.
At last we check while k < l and previous element of k is equal to current element of k then we increase k by 1
and Similarly we check while k < l and previous element of l is equal to current element of l then we decrease l by 1.
At last we append the values of temp in list of ans and return the ans. 
TC - O(N^3) and SC - O(no of quadruples)
'''


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
