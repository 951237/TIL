from random import *

words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)
letters = ""

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end = " ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("succeed")
        break

    letter = input("Input letter > ")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("correct")
    else:
        print("wrong")
        