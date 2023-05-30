#!/usr/bin/python3
def fizzbuzz():
    "A function that prints 1 to 100"
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{:d}".format(i), end=' ')