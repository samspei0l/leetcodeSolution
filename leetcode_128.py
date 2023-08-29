'''
Leetcode 128
Given an unsorted array of integers nums, return the
length of the longest consecutive elements sequence
'''


def linearSearch(arr, num):
    n = len(arr)
    for i in range(n):
        if arr[i] == num:
            return True
    return False


'''
Brute Force Solution: The brute force solution for this problem will require
to create an extra function called linear search to search linearly in array
if the next consecutive number exits or it.
We define our current longest consecutive length be 1, then we iterate through
the size of array and set our element to arr[i] and count to 1. After that
we run a while loop for linearSearch until it's false from arr to element+1 i.e
next element increased by 1, and we increase our counter by 1 if the condition
is true then we take max of longest and count and print the longest.
TC - O(N*N) and SC - O(1)
'''


def leetcode128(arr):
    longest = 1
    for i in range(len(arr)):
        element = arr[i]
        count = 1
        while linearSearch(arr, element+1):
            element += 1
            count += 1
        longest = max(longest, count)
    print(longest)


'''
Better Solution: For better solution we first sort the array. We take
our longest sequence length to be 1, our counter be 0 and last_smallest_element
be min(arr) - 1. Then we run a for loop for the length of array and we check
if the current element at i - 1 is last_smallest_element if yes
then we increase our counter by 1 and last_smallest_element will be new arr[i].
If not then we just make our counter to 1 and the last_smallest_element
to arr[i]. Then we take max of longest and counter and print longest
'''


def leetcode128Better(arr):
    longest = 1
    counter = 0
    arr.sort()
    last_small_element = min(arr)-1
    for i in range(len(arr)):
        if arr[i] - 1 == last_small_element:
            counter += 1
            last_small_element = arr[i]
        elif last_small_element != arr[i]:
            counter = 1
            last_small_element = arr[i]

        longest = max(longest, counter)
    print(longest)


'''
Optimal Solution: For optimal solution we use set data structure.
We first add all the element from array to a set data structure. Once done
we check if previous element of current iteration in set exists or not
if it exits then we move to next iteration in set and if it doesn't exits
then we change our counter to 1 and the element will be the value at the
iteration once we have our element we run while loop to check if element + 1
i.e next element increase by 1 is in set or not. If yes then we move to next
element by adding 1 to it and increase our counter by 1. After that we take max
of longest and count and print longest.
'''


def leetcode128Optimal(arr):
    n = len(arr)
    ans = set()
    longest = 1
    for i in range(n):
        ans.add(arr[i])
    for it in ans:
        if it - 1 not in ans:
            count = 1
            element = it
            while element+1 in ans:
                element += 1
                count += 1
            longest = max(longest, count)
    print(longest)


def main():
    arr = [100, 4, 200, 1, 3, 2]
    leetcode128Optimal(arr)


if __name__ == "__main__":
    main()
