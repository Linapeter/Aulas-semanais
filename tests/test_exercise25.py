from python.exercise25_PE12 import len_div_triangle, len_div_triangle_number

def test_exercise25() -> None:
    assert 28 == len_div_triangle(5)
    assert 76_576_500 == len_div_triangle(500)

def test_exercise_25() -> None:
    assert 28 == len_div_triangle_number(5)
    assert 76_576_500 == len_div_triangle_number(500)