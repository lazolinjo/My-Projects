def pilin(number): #paran ili neparan
    while number != 1:
        if number % 2 == 0: #Ako je broj paran
            print('Broj je paran')
            
        elif number % 2 == 1: #Ako je broj neparan
            print('Broj je neparan')

        break


print('Molim Vas, unesite broj')

try:
    num = int(input()) #dodaje korisnicki input
    pilin(num)
except ValueError: #Ako dobijete gresku
    print('Molim Vas koristite samo cele brojeve')