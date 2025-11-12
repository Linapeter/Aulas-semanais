from exercises.exercise31 import grid_routes

def test_exercises31() -> None:
    assert 20 == grid_routes(3)
    assert 6 == grid_routes(2)
    assert 137_846_528_820 == grid_routes(20)