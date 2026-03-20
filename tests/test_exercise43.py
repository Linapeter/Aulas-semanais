from exercises.exercise43_PE21 import sum_of_amicable_pairs


def test_exercise43() -> None:
    assert 31_626 == sum_of_amicable_pairs(
        10_000
    ), "Failed test with function that uses multiples primes."
