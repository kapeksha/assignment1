#Que.07:
#Create a Python function that takes a dictionary as input and returns a new dictionary with keys as values and values as keys (assuming values are unique).

def values(inputdict):
    swappeddict = {}

    for key, value in inputdict.items():
        swappeddict[value] = key

    return swappeddict


inputdict = {'a': 1, 'b': 2, 'c': 3}
swappeddict = values(inputdict)
print("Original dictionary:", inputdict)
print("Swapped dictionary:", swappeddict)
