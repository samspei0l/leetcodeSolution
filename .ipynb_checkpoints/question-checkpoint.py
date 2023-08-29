def maxConsecutiveOnes(arr1):
    counter = 0
    maxi = 0
    for i in range(len(arr1)):
        if arr1[i] == 1:
            counter += 1
            maxi = max(maxi,counter)
        else: counter = 0
    print(maxi)

def findNumberAppearOnce(arr1):
    for i in range(len(arr1)):
        num = arr1[i]
        count = 0
        for j in range(len(arr1)):
            if arr1[j] == num:
                count +=1
        if (count == 1): print(num)

def findNumberAppearOnceXOR(arr1):
    xor = 0
    for i in range(len(arr1)):
        xor = xor ^ arr1[i]
    print(xor)

def twoSum(arr1,target):
    n = len(arr1)
    left = 0
    right = n-1
    while(left<right):
        sum = arr1[left] + arr1[right]
        if sum == target:
            print("yes")
        elif sum < target:
            left += 1
        else: right -= 1
    print("NO")

def longestSubArray(arr1):
    length = 0
    n = len(arr1)
    k = 3
    for i in range(n):
        for j in range(1,n):
            sum = 0
            for k in range(i,j):
                sum += arr1[k]
            if sum == k: length = max(length,j-i+1)
        print(length)

#Better Solution
def sortColor(arr1):
    n = len(arr1)
    countRed = 0
    countWhite = 0
    countBlue = 0
    for i in range(len(arr1)):
        if arr1[i] == 0:
            countRed += 1
            i += 1
        elif arr1[i] == 1:
            countWhite += 1
            i += 1
        elif arr1[i] == 2:
            countBlue += 1
            i += 1
    for i in range(countRed):
        arr1[i] = 0
    for i in range(countRed,countRed+countWhite):
        arr1[i] = 1
    for i in range(countRed+countWhite,n):
        arr1[i] = 2
    print(arr1)

#Optimal Solution
def sortColors(arr1):
    n = len(arr1)
    low, mid, high = 0, 0, n-1
    while(mid <= high):
        if arr1[mid] == 0:
            arr1[low], arr1[mid] = arr1[mid], arr1[low]
            low += 1
            mid += 1
        elif arr1[mid] == 1:
            mid += 1
        elif arr1[mid] == 2:
            arr1[mid], arr1[high] = arr1[high],arr1[mid]
            high -= 1
    print(arr1)

def main():
    arr1 = [2,0,2,1,1,0]
    #maxConsecutiveOnes(arr1)
    #target = 14
    #findNumberAppearOnceXOR(arr1)
    #twoSum(arr1,target)
    #longestSubArray(arr1)
    sortColors(arr1)
    


if __name__ == "__main__":
    main()
