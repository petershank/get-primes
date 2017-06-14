#! /usr/bin/python

def isPrime():
    while True:
        try:
            number = int(input("Enter an integer greater than 1: "))
            
            for num in range(number + 1):
                if num > 1:
                    for i in range(2, num):
                        if (num%i) == 0:
                            break
                        else:
                            print('' + str(num) + ' is prime')
            break
        except ValueError:
            print('invalid input\n')
isPrime()
