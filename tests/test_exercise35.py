from python.exercise35_PE17 import counting, counting_until

def test_exercises35() -> None:
    assert 23 == counting(342), "Broke in counting letters, first assert"
    assert 20 == counting(115), "Broke in counting letters, second assert"
    assert 19 == counting_until(5), "Broke in counting letters until the number 5, third assert"
    assert 21_124 == counting_until(1_000), "Broke in counting letters until the number 1.000, fourth assert"