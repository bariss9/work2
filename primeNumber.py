def isPrime(num):
    if(num < 0 or num == 1 ):
        print(f"{num} is not a prime number")
        return False
    counter = 0
    x = 2
    while(x != num):
        if(num % x == 0):
            counter = 1
            break
        x += 1
    if(counter == 0):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")    
isPrime(1)
isPrime(2)
isPrime(23)
isPrime(25)
isPrime(-4)