import time
import random
import sys

print("Choice level\n")
print("1.easy\n2.medium\n3.hard\n4.ultra mode\n")
x = int(input(": "))
#level 1
if x == 1:
    print("you have got 5 seconds")
    y = 5
    while y > 0:
        print(y-1)
        y-=1
        time.sleep(1)
    print("Come on!!!")
    while True:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(str(num1) + "+" + str(num2) + "?\n")
        answer_ri = num1+num2
        answer = int(input("asnwer: "))
        if answer == answer_ri:
            print("yes!")
        else:
            print("Error!")
#level 2
if x == 2:
    print("you have 5 seconds")
    y = 5
    while y > 0:
        print(y-1)
        y-=1
        time.sleep(1)
    print("Come on!!!")
    while True:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        print(str(num1) + "+" + str(num2) + "?\n")
        answer_ri = num1+num2
        answer = int(input("asnwer: "))
        if answer == answer_ri:
            print("yes!")
        else:
            print("Error!")
#level3
if x == 3:
    print("you have 5 seconds")
    y = 5
    while y > 0:
        print(y-1)
        y-=1
        time.sleep(1)
    print("Come on!!!")
    while True:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)
        print(str(num1) + "+" + str(num2) + "?\n")
        answer_ri = num1+num2
        answer = int(input("asnwer: "))
        if answer == answer_ri:
            print("yes!")
        else:
            print("Error!")
#level4
if x == 4:
    print("you have 5 seconds")
    y = 5
    while y > 0:
        print(y-1)
        y-=1
        time.sleep(1)
    print("Come on!!!")
    while True:
        num1 = random.randint(1000,10000)
        num2 = random.randint(1000,10000)
        print(str(num1) + "*" + str(num2) + "?\n")
        answer_ri = num1*num2
        answer = int(input("asnwer: "))
        if answer == answer_ri:
            print("yes!")
        else:
            print("Error!")
