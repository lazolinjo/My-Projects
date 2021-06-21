def decider(number):
    while number != 1:
        if number % 2 == 0: #If even
            print('Number is even')
            
        elif number % 2 == 1: #If odd
            print('Number is odd')

        break

print('Please enter a number')

try:
    num = int(input()) #dodaje korisnicki input
    decider(num)
except ValueError: #Ako dobijete gresku
    print('Molim Vas koristite samo cele brojeve')


