#Que.04:
#Write a Python program to count Vowels in a Given Word.

def cvowels(word):
    vowels={'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for char in word:
        if char.lower()in vowels:
            vowel_count+=1
    return vowel_count

word=input("enter word:")
print("number of vowels:",cvowels(word))