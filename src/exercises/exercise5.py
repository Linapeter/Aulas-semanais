# Exercise 3
# The prime factors of 1395 are 5,7 and 29
# What is the largest prime factor of the number 600851475143?

def prime_factors(limit:int):
    result = []
    for i in (2,limit):
        if i%i==0 is False:
            result.append(j)
    return result
prime_factors(1395)