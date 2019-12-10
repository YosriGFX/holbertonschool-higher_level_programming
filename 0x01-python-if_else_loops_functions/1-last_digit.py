#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
numbers = number
if numbers < 0:
    numbers = number * -1
    sign = -1
digt = numbers % 10
while digt % 10 > 9:
    digt = digt % 10
digt = digt * sign
if digt > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, digt))
elif digt == 0:
    print("Last digit of {} is {} and is 0".format(number, digt))
else:
    print(end="\0""Last digit of {} is {} and is ".format(number, digt))
    print("less than 6 and not 0")
