'''
Optimal Solution: If there is no such prefix which is common in strs we simply return res = ""
Now we check for every character of 1st string in strs. We are taking 1st string because if the 1st string has the maximum length among all the string
our for loop will after checking for longest common prefix for it's character.
Now we check for every string in strs, if the first character of second element doesn't match with the first character of first element
then we simply return the result. Otherwise we keep checking for every character that matches to the every character of give string and add them to result.
Finally we return the result
'''


def leetcode14(strs):
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            print(s[i])
            if i == len(s) or s[i] != strs[0][i]:
                print(res)
        res += strs[0][i]
    print(res)


def main():
    strs = ["flower", "flow", "flight"]
    leetcode14(strs)


if __name__ == "__main__":
    main()
