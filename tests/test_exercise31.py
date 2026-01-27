from python.exercise31_PE15 import grid_routes


def test_exercises31() -> None:
    assert 20 == grid_routes(3), "Broke first assert"
    assert 6 == grid_routes(2), "Broke second assert"
    assert 137_846_528_820 == grid_routes(20), "Broke third assert"