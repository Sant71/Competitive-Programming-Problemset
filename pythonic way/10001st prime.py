# Problem 7: 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the nth prime number?

def isPrime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i ==0:
            return False
    return True

print(isPrime(7))

def nthprime(n)->int:
    thPrime=0
    number=1
    while(True):
        if isPrime(number):
            thPrime+=1
            if thPrime == n :
                return number
        number+=1
print(nthprime(int(input("Enter the nthPrime:"))))