# Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

#This code will run but its too slow for large numbers

# def smallestMultiple(number):
#     j=1

#     while(True):
#         print(j)
#         for i in range(1,number+1):
#             if j%i != 0:#
#                 j+=1
#                 break
#             elif i==number: #=2
#                 return j
            

# print(smallestMultiple(int(input("Enter the period numbers "))))
            
        
#Now i understand why we need the discret math but thy fucking doctors dont teach us how we can use it
#inside programing solution Those pepole will destroy the young people 

#REGARDLESS WHAT I SAY WEE NEED TO USE PRIME FACTORIZATION TO SOLVE THIS PROBLEM OK 
#Numerator and denominator


# def primeFactorization(number):
#     tree = []
#     numerator = number
#     denominator = 2
#     while(True):
#         if numerator%denominator == 0:
#             tree.append(denominator)
#             numerator/=denominator
#             denominator=2
#         else:
#             if denominator<numerator:
#                 denominator+=1
#             else:
#                 return tree

# def smallestMultiple(number):
#     primeFctorizationTree=[]
#     for i in range(1,number+1):
#         primeFctorizationTree.append(primeFactorization(i))
#     redused=[]
#     redused+=primeFctorizationTree[0]
#     for i in range(1,len(primeFctorizationTree)):
#         for j in range(len(primeFctorizationTree[i])):
#             if primeFctorizationTree[i][j] in redused:
#                 redused.append(primeFctorizationTree[i][j])
#             else:
#                 redused.append(primeFctorizationTree[i][j])
#     print(redused)
            
# smallestMultiple(9)


#What the fuck i douing why this python

#Its pythonic way : i love this lang 
import math
from functools import reduce
def smallestMultiple(number):
    return reduce(math.lcm,range(1,number+1)) 
print(f'Boom That what i need the paythonic Way {smallestMultiple(int(input("Enter the fucking period of numbers  so boring: ")))}')