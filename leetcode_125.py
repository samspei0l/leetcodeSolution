def leetcode125(s):
    n = len(s)
<<<<<<< HEAD
    s.lower()

=======
    reverse = s[::-1]
    s = s.replace(",", "")
    s = s.replace(":","")
    print(s)
    print(reverse.lower())
    if (s.lower() == reverse.lower()):
        print("True")
    else: print("False")
>>>>>>> b7c13ef57b3d25cbc776e8d40d64aa1a2d506a9f

def main():
    s = "A man, a plan, a canal: Panama"
    leetcode125(s)

<<<<<<< HEAD

if __name__ == "__main__":
    main()
=======
if __name__ == "__main__":
    main()
>>>>>>> b7c13ef57b3d25cbc776e8d40d64aa1a2d506a9f
