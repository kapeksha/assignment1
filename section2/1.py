#Que:01
# Write python program to find second largest number in integer list.


def max(numbers):
    if len(numbers)<2:
        return "List should have least 2 numbers"
    larg=max=float('-inf')
    for num in numbers:
        if num>larg:
            max=larg
            larg=num
        elif num>max and num!=max:
            max=num

    return max

numbers=[10,5,2,9,56,98]
print("secand largest number:",max(numbers))