# Problem 6: Sum square difference
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.


#ok Mby that is easy lets make a list of natural numbers from 1 to n

def sumSquareDifference(n):
    natural_numbers = list(range(1,n+1))
    #i here abut reduse method i will learn how i can use it i need just the pythonic way 
    # reduce() function (from functools) applies a function cumulatively to an iterable,
    #  reducing it to a single value. It’s handy for concise tasks like summing,
    #  multiplying (factorial), finding max/min, concatenating strings or flattening lists.
    #  Use it for simple one-line reductions,
    #  avoid it for complex logic (loops are clearer) or when intermediate results are needed.
    #ok i found somthing useful about reduse()
    from functools import reduce
    # result = reduce(function, iterable, initializer=None)
    #I love euler he thech me a lot of pytohnic way
    return abs(reduce(lambda acc,next:next**2+acc,natural_numbers,0)-(sum(natural_numbers)**2))


print(sumSquareDifference(int(input('Enter the range of your natural number :'))))