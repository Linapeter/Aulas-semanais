## 2420 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# vai de numero em numero até o 10,
# pega o largest prime que é divisivel pelo numero e vai multiplicando em um acc
# e para cada etapa, se o acc for divisivel pelo numero visitado, nem precisa add no acc

#plot: para todo numero visitado que não for divisivel pelo acc, append na lista dos multiplos que depois vao ser multiplicados

from functools import reduce

from exercises.exercise5 import largest_prime


def evenly_divisible(limit: int) -> int:
    """Find the smallest positive number that is evenly divisible by all of the numbers from 1 to limit.

    Args:
        limit (int): limit number to check divisibility

    Returns:
        list[int]: smallest number that is evenly divisible by all numbers from 1 to limit
    """
    multiples:list[int] = []
    acc: int = 1
    for i in range(1, limit+1):
        if acc % i != 0:
            lp = largest_prime(i)
            multiples.append(lp)
            acc = reduce(lambda x, y: x * y, multiples)

    return acc
