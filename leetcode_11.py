
'''
Optimal Solution: Using two pointer method.
The two-pointer technique starts with the widest container and moves the pointers inward based on the comparison of
heights. Increasing the width of the container can only lead to a larger area if the height of the new boundary is
greater. By moving the pointers towards the center, we explore containers with the potential for greater areas.
'''
def leetcode11(height):
    left, right = 0, len(height) - 1
    maxArea = 0

    while left < right:
        currentArea = min(height[left], height[right]) * (right - left)
        maxArea = max(maxArea, currentArea)

        if height[left] < height[right]:
            left += 1
        else: right -= 1
    print(maxArea)
def main():
    height = [1,8,6,2,5,4,8,3,7]
    leetcode11(height)

if __name__ == "__main__":
    main()