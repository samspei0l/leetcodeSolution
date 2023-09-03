from collections import defaultdict

'''
Optimal Solution: There are two approaches to this problem.
One is to sort the word add it to to map as key. Then compare other words
in sorted form with that key if the match add them as value to that particular key.
Another approach is using ASCII value of each character in word and then compare it
with other characters of the other word. e.g: eat has 1e, 1a and 1t. If any other element
in the array of strings has same no of character then they are anagram. Simply add them to
a list and once added move to the next word.
'''


def leetcode49(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    print(res.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    leetcode49(strs)


if __name__ == "__main__":
    main()
