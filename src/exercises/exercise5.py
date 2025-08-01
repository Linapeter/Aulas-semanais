# Exercise 3
# The prime factors of 1395 are 5,7 and 29
# What is the largest prime factor of the number 600851475143?

def largest_prime(number:int) -> int:
    """A function that returns the largest prime factor until the number of your choice
    """
    largest_factor:int = 0
    counter: int = 2
    clone_number: int = number

    while counter**2 < clone_number:
        if (clone_number % counter == 0):
            clone_number = clone_number // counter
            largest_factor = counter
        else:
            counter += 1
    if (clone_number > largest_factor):
        largest_factor = clone_number
    return largest_factor

print(largest_prime(1395))
print(largest_prime(600_851_475_143))
