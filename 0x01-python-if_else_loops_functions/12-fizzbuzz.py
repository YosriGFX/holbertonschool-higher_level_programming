#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if (a % 5 == 0) and (a % 3 == 0):
            print(end="FizzBuzz ")
        elif a % 5 == 0:
            print(end="Buzz ")
        elif a % 3 == 0:
            print(end="Fuzz ")
        else:
            print(end="{} ".format(a))
