#Que:02
#Write Python program to count frequency of each element in list.

def count(list):
    frequeny={}
    for element in list:
        if element in frequeny:
            frequeny[element]+=1
        else:
            frequeny[element]=1
    for key, value in frequeny.items():
        print(f"{key}:{value}")

list=[1, 2, 3, 4, 1, 2, 1, 3, 2]
print("Frequency of each element in the list:")
count(list)
