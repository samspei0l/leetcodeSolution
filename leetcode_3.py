'''
Optimal Solution: We use slinding window approach for this problem.
We first declare a set to add all the continous substring.
We start from first character in string and check if that is in our set or not
If not then we add it to set if yes then we remove the left character from the set
and generate new substring of the same length by adding the right character of string.
Once we have traversed through all character in string we calcuate the length of longest
substring without repeating characters.
'''


def leetcode3(s):
    n = len(s)
    hashset = set()
    l = 0
    res = 0
    for r in range(n):
        while s[r] in hashset:
            hashset.remove(s[l])
            l += 1
        hashset.add(s[r])
        res = max(res, r - l + 1)
    print(res)


def main():
    s = "abcabcbb"
    leetcode3(s)


if __name__ == "__main__":
    main()
