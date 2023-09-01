'''
Optimal Solution: We sort the given array using lambda key function.
We take a list ans and initialize it out first element of array.
Then we define for loop to look for start and end in intervals[1:]
Our previous end will be the end stored in ans i.e ans[-1][1]
If our current start <= previousEnd i.e lastEnd, then we take max of lastEnd and current end.
else we append both start and end to list of ans. 
Finally we return the ans
'''


def leetcode56Optimal(intervals):
    n = len(intervals)
    intervals.sort(key=lambda i: i[0])
    # print(intervals)
    ans = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = ans[-1][1]

        if start <= lastEnd:
            ans[-1][1] = max(lastEnd, end)
        else:
            ans.append([start, end])
    print(ans)


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    leetcode56Optimal(intervals)


if __name__ == "__main__":
    main()
