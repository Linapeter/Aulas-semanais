# Exercise 3
# The prime factors of 1395 are 5,7 and 29
# What is the largest prime factor of the number 600851475143?


def largest_prime(number: int) -> int:
    """A function that returns the largest prime factor until the number of your choice"""
    largest_factor: int = 0
    counter: int = 2

    while counter * counter <= number:
        if number % counter == 0:
            number //= counter
            largest_factor = counter
        else:
            counter += 1
    if number > largest_factor:
        largest_factor = number
    return largest_factor