#Que.10:
#Write a program to address following scenario-Given an integer list nums, return true if any 
#value appears at least twice in list, and return false if every element is distinct.

def duplicate(nums):
    unique_elements=set()

    for num in nums:
        if num in unique_elements:
            return True
        else:
            unique_elements.add(num)
    return False

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4, 5, 1]

print("num1 have duplicates??",duplicate(nums1))
print("num2 have duplicates??",duplicate(nums2))