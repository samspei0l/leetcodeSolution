def leetcode347(nums, k):
    n = len(nums)
    ans = []
    for i in range(1, n):
        count = 1
        if nums[i] == nums[i - 1]:
            count += 1
            i += 1
        if count > k:
            print(nums[i])


def leetcode347Better(nums, k):
    n = len(nums)
    hashmap = set()
    for i in range(n):
        count = 1
        if nums[i] in hashmap:
            count += 1
        hashmap.add(nums[i])
        if count >= k:
            print(hashmap)


'''
Optimal Solution: Using Bucket Sort.
In this problem we are using bucket sort. eg. if the given array is [1,1,1,2,2,3]
then we define another list of array where we have key and value pair. The key will
be the count of the no of occurrence of same element in array and it's value will be
the all the element that occurs for that count number. e.g In given array 1 occurs 3 times
then at index 3 (i(count)) we will insert 1 and at index 2(i(count)) we insert 2 and at
index 1(i(count)) we insert 3. After that we check for the most frequent elements from last of 
our result array and we keep decreasing it by 1 and append the values located at index having more count.
'''


def leetcode347Optimal(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k:
            print(res)


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # leetcode347(nums, k)
    # leetcode347Better(nums, k)
    leetcode347Optimal(nums, k)


if __name__ == "__main__":
    main()
