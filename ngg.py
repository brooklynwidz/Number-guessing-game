import random

number = random.randint(0,101)
print(number)

guess_no = 0
while guess_no < 5:
    inputno = int(input("Enter your guess number: "))
    if inputno > number:
        print("too high")
    elif inputno < number:
        print("too low")
    else:
        print("correct")
        break
    guess_no+=1
