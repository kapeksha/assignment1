#Que:03 
#Write a Python program to find the common elements between two lists.

def element(list1,list2):
    set1=set(list1)
    set2=set(list2)

    c_elements=set1.intersection(set2)
    return c_elements

list1=[1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

c_elements=element(list1,list2)
print("common elements are:",c_elements)