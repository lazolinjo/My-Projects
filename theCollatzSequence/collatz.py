
def collatz(number):
    while number != 1:
        if number % 2 == 0: #If number is even
            number = number // 2
            print(number)

        elif number % 2 == 1: #If number is odd
            number = number * 3 + 1
            print(number)

print("please enter a number:")

try:
    num = int(input()) #adds user input
    collatz(num)
except ValueError: #if you get ValueError because of floating point numbers
    print('Please use whole numbers only.')


'''This is a collatz Sequence
A sequence that always ends up at 1 no matter which number you pick or how long it takes'''