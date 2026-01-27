# https://www.youtube.com/watch?v=JXUvxgGXVD4

# c < a + b --> o c é menor que a soma dos outros dois, então c é menor que soma/2

# c > b > a --> a+b+c = soma -> soma//3 é menor que c (ex: 3,4,5 : (soma = 12), (soma/3 = 12/3 = 4) e 4 < 5)

# a + b + c = soma --> a = soma - b - c


def pythagorean_triplet_sum(sum_abc: int) -> int:
    """This function finds a Pythagorean triplet that has the sum of its sides equal to the given value.

    Args:
        sum_abc (int): the sum of the sides wanted

    Returns:
        int: the product of the pythagorean triplet found
    """
    result = 0

    if sum_abc <= 1:
        raise ValueError("sum abc cannot be less or equal one")

    for c in range(sum_abc // 3, sum_abc // 2):
        for b in range(int(sum_abc ** (1 / 2)), c):
            a = sum_abc - b - c
            if a * a + b * b == c * c and a + b + c == sum_abc:
                result = a * b * c
                break

    return result
