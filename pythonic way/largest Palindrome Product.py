# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers.


def is_palindrome(number):
    string_number =str(number)
    reversed_number = string_number[::-1]

    return string_number == reversed_number

def largest_palindrome_product(num_digit):
    largest_palindrome = 0

    start = (10**num_digit)-1
    stop = 10**(num_digit-1)

    for i in range(start,stop-1,-1):
        if largest_palindrome>= i*start:
            break
        
        for j in range(start,stop-1,-1):
            if largest_palindrome>= j*start:
                break
            if is_palindrome(i*j):
                largest_palindrome = i*j

    return f'This is the largist palindrom product {largest_palindrome}'


print(largest_palindrome_product(int(input("Enter the number of digits :"))))
# That cost me a cigarette. ooff 