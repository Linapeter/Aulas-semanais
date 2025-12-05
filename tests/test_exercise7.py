from exercises.exercise7_PE4 import largest_palindromic

def test_exercise7() -> None:
    assert 906_609 == largest_palindromic(3)
    assert 9_009 == largest_palindromic(2)