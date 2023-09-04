def leetcode125(s):
    n = len(s)
    reverse = s[::-1]
    s = s.replace(",", "")
    s = s.replace(":","")
    print(s)
    print(reverse.lower())
    if (s.lower() == reverse.lower()):
        print("True")
    else: print("False")

def main():
    s = "A man, a plan, a canal: Panama"
    leetcode125(s)

if __name__ == "__main__":
    main()