'''
Optimal Solution: We can solve these question by two ways. One way is to use division operator.
As per the rules we can't use division operator so we look at another way of solving this problem.
We will use prefix and postfix method to solve this problem. We will first calculate the prefix of
given elements in array which is product of prefix and value at nums[i]. The prefix will be calculated
from the 0 to len(nums). Similarly we calculate postfix which is the product of postfix and value of nums
starting from n - i - 1 index. at last we can append the value to our result.
'''


def leetcode238(nums):
    n = len(nums)
    ans = [1] * n
    pre = 1
    post = 1
    for i in range(n):
        ans[i] *= pre
        pre = pre * nums[i]
        ans[n - i-1] *= post
        post = post * nums[n-i-1]
    print(ans)


def main():
    nums = [1, 2, 3, 4]
    leetcode238(nums)


if __name__ == "__main__":
    main()
