#Que.08:
#Create a Python function that takes two lists as input and returns True if they have at least one common element, False otherwise

def common(list1,list2):
    set1=set(list1)
    set2=set(list2)
    return bool(set1.intersection(set2))

list1=[1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10,1]
print("list1:",list1)
print("list2:",list2)
print("is any common element?",common(list1,list2))