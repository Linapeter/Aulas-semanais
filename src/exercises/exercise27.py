# Project Euler

# Problem 13
# Large Sum

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def large_sum(box:str) -> int:
    numbers = list(map(int, box.split()))
    sum_numbers = str(sum(numbers))
    return int(sum_numbers[0:10])