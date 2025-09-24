from functools import reduce

def box_largest_products_of(
    box: str,
    digits: int,
) -> int:
    """This function find the greatest product of (digits) consecutive numbers in the box of numbers as a string

    Args:
        box (str): a box of numbers as a string
        digits (int): number of digits

    Returns:
        int: the greatest product of (digits) consecutive numbers in the box
    """
    interable = 1
    product = 1

    for index in range(0, len(box) - digits + 1):
        adjecent_numbers = box[index : index + digits]
        product = reduce(lambda x, y: x * y, map(int, adjecent_numbers))

        if product > interable:
            interable = product

    return interable
