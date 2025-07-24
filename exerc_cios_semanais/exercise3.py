# Exercise 1: Fibonnaci Sequence Sum of even-valued terms

def sum_even_fibonacci(limit):
    fn1,fn2 = 1, 2
    even_terms = 0

    while fn2 < limit:
        if fn2%2 == 0:
            even_terms += fn2
        fn3 = fn1 + fn2
        fn1 = fn2
        fn2 = fn3

    return even_terms