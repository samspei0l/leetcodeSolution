'''
Optimal Solution: This problem uses sliding windows technique.
We create a substring of characters from given strings then we check the count
of occurrence of the characters in string ans store them in hashMap. For eg.
string s = "ABABBA". We start from 1st character and we add it to our hashMap
with the no of occurence of it then we shift our right pointer by 1 to create a
new substring of "AB" and store the count of occurence of each character in our hashMap.
This is done for all the character in our hashMap. To find the character that need to be
changed to create a longest repeating character string we subtract the max of count of character
in our hashMap with the length of the window use to create that substring, if that is < k (no of time updation of character can be done)
we count our length by updating it by 1.
'''


def leetcode424(s, k):
    n = len(s)
    l = 0
    count = {}
    res = 0
    for r in range(n):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    print(res)


def leetcode424Another(s, k):
    n = len(s)
    count = {}
    res = 0
    left = 0
    maxFreq = 0
    for right in range(n):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxFreq = max(maxFreq, count[s[right]])

        while (right - left + 1) - maxFreq > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    print(res)


def main():
    s = "ABAB"
    k = 2
    leetcode424Another(s, k)


if __name__ == "__main__":
    main()
