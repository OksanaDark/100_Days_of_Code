#def prime_checker(number, count=0):
#    for i in range(number, 0, -1):
#        new_number = number / i
#        decimal_part = new_number % 1
#        if decimal_part == 0:
#            count += 1

#    if count == 2:
#        print("it's a prime number.")
#    else:
#        print("it's not a prime number.")


#n = int(input("check this number: "))
#prime_checker(number=n)

def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime")
    else:
        print("Not prime")





n = int(input("check this number: "))
prime_checker(number=n)
