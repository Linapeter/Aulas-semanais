# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindromic(digits:int) -> int:
    max_number = int(str(9) * digits)                #99
    min_number = int(str(1) + str(0)*(digits-1))     #10
    palindromic_number = 0
    for i in range(max_number,min_number-1,-1):        # de 10 a 99
        for j in range(i,min_number-1,-1):
            candidate = i*j
            if str(candidate)[::-1] == str(candidate):

                if candidate > palindromic_number:
                    palindromic_number = candidate
    return palindromic_number

print(palindromic(3))