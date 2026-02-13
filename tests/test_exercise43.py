from python.exercise43_PE21 import amicable, amicable_pairs

def test_exercise43() -> None:
    assert 31_626 == amicable_pairs(10_000), "Failed test with function that uses multiples primes."
    assert 31_626 == amicable(10_000), "Failed the test that uses brute force."