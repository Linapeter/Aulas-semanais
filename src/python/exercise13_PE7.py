from python.exercise5_PE3 import largest_prime


def prime_in_position(position: int) -> int:
    """Returns the prime factor in position of choice

    Args:
        position (int): position of the factor prime

    Returns:
        int: factor prime
    """
    counter = 1
    index = 1
    some_number_prime = largest_prime(index)  # 2

    while counter <= position:
        index += 1
        possible_next = largest_prime(index)

        if possible_next > some_number_prime:
            counter += 1
            some_number_prime = possible_next

    return some_number_prime
