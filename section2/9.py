#Que.09
#Write a Python program that reads text file, counts frequency of each character,
#stores counts in dictionary where keys are characters and values are frequencies.

def frequency(filename):
    char_frequency={}
    with open(filename,'r')as file:
        data=file.read()

        for char in data:
            char_frequency[char]=char_frequency.get(char,0)+1
    return char_frequency

filename='sample.txt'
char_frequency=frequency(filename)
print("character frequency:",char_frequency)