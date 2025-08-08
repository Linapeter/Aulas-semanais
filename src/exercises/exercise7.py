# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindromic(digits:int) -> int:
    """Returns the largest palindrome made from the product of two ()-digit numbers

    Args:
        digits (int): number of digits of the numbers of product

    Returns:
        int: the largest palindrome number
    """
    palindromic_number = 0
    interval = range(10**digits,10**(digits-1),-1)
    for first_number in interval:
        for second_number in interval:
            candidate = first_number*second_number
            if str(candidate)[::-1] == str(candidate):

                if candidate > palindromic_number:
                    palindromic_number = candidate
    return palindromic_number
