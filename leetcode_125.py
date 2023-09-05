'''
Optimal Solution: We can use two method One is to use inbult python function to check
the string is alphanumeric or not and then compairing the lower case of normal string and
it's reverse. If they are equal for every character then they are palindrome if not they are not
palindrome. Another method is to use Two Pointer method. Before doing that we need to check if the given string is alphaNumeric or not.
To check the string is alphaNumeric we can use python ord() function. To start our two pointer approach, we will use
left and right pointer pointing at 0 and len(string) - 1. if the lower case of both left and right pointer character is not equal then return False else return True.
Increase the left by 1 and decrease the right by -1. Once left crosses the right we can know the given string is palindrome or not
'''


def leetcode125(self, s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not self.alphaNums(s[left]):
            left += 1
        while right > left and not self.alphaNums(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            print("False")
        left += 1
        right -= 1
        print("True")


def alphaNums(self, c):
    return (
        (ord("A") <= ord(c) <= ord("Z")) or
        (ord("a") <= ord(c) <= ord("z")) or
        (ord("0") <= ord(c) <= ord("9"))
    )


class Solution:
    def main(self):
        s = "A man, a plan, a canal: Panama"
        leetcode125(self, s)

    if __name__ == "__main__":
        main()
