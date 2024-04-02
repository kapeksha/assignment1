#Que.06:
#Create a Python function that takes two dictionaries as input and merges them into a single dictionary.
#If there are any common keys, the values should be added together.

def mergedictionaries(dict1, dict2):
    mergeddict = {}
    for key, value in dict1.items():
        mergeddict[key] = value
    for key, value in dict2.items():
        if key in mergeddict:
            mergeddict[key] += value
        else:
            mergeddict[key] = value

    return mergeddict

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
mergeddict = mergedictionaries(dict1, dict2)
print("Merged dictionary:", mergeddict)
