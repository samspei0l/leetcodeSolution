# Leetcode 121 Best Time to Buy ans Sell Stock

# Brute Force Solution
'''
In this question we take first element in array as our minimum buying
price because we have to buy before selling. We initialize our profit
= 0. Now iterating from i+1 i.e 2nd element in array till n i.e the
length of array. cost is a variable that shows the cost to buy the
stock. profit is variable that shows the profit we generated by
buying and selling then we update our mini price to buy stock to
new mini where we take minimum of previous mini and the new price at index i
TC - O(N) because we checking for maximum profit throughout the array. SC - O(1)
we are not using any extra space.
'''


def leetcode121Brute(arr):
    mini = arr[0]
    profit = 0
    for i in range(1, len(arr)):
        cost = arr[i] - mini
        profit = max(profit, cost)
        mini = min(mini, arr[i])
    print(profit)

# Solution using Two Pointer Method:


'''
Here in this method we take two pointers left and right
we initialize left and right to 0 and 1. Then we use while
loop until the right < len(arr). Now we check if prices[left]
< prices[right] if yes then profit = prices[right] - prices[left]
maxProfit = max(maxProfit, profit) i.e max of previous maxProfit and new profit
if no then we make left = right and increase right by 1.
'''


def leetcode121TwoPointer(arr):
    left, right = 0, 1
    maxProfit = 0
    while right < len(arr):
        if arr[left] < arr[right]:
            profit = arr[right] - arr[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1
    print(maxProfit)


def main():
    arr = [7, 1, 5, 3, 6, 4]
    # leetcode121Brute(arr)
    leetcode121TwoPointer(arr)


if __name__ == "__main__":
    main()
