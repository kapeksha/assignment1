#Que.05:
#Write a program that accepts a sentence and calculate the number of letters and digits.

def count_letters_digits(sentence):
    numletters = numdigits = 0
    for char in sentence:
        if char.isalpha():
            numletters += 1
        elif char.isdigit():
            numdigits += 1

    return numletters, numdigits

sentence = input("Enter a sentence: ")
letters, digits = count_letters_digits(sentence)
print("Number of letters:", letters)
print("Number of digits:", digits)
