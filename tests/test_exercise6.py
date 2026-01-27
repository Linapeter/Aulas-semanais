from python.exercise6_listOps import ListOps


def test_append_empty_lists() -> None:
    assert ListOps([]).append([]) == []


def test_append_list_to_empty_list() -> None:
    assert ListOps([]).append([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_append_empty_list_to_list() -> None:
    assert ListOps([]).append([1, 2, 3, 4], []) == [1, 2, 3, 4]


def test_append_non_empty_lists() -> None:
    assert ListOps([]).append([1, 2], [2, 3, 4]) == [1, 2, 2, 3, 4]


def test_concat_empty_list() -> None:
    assert ListOps([]).concat([]) == []


def test_concat_list_of_lists() -> None:
    assert ListOps([]).concat([[1, 2], [3], [], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]


def test_concat_list_of_nested_lists() -> None:
    assert ListOps([]).concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]]) == [
        [1],
        [2],
        [3],
        [],
        [4, 5, 6],
    ]


def test_filter_empty_list() -> None:
    assert ListOps([]).filter(lambda x: x % 2 == 1, []) == []


def test_filter_non_empty_list() -> None:
    assert ListOps([]).filter(lambda x: x % 2 == 1, [1, 2, 3, 5]) == [1, 3, 5]


def test_length_empty_list() -> None:
    assert ListOps([]).length([]) == 0


def test_length_non_empty_list() -> None:
    assert ListOps([]).length([1, 2, 3, 4]) == 4


def test_map_empty_list() -> None:
    assert ListOps([]).map(lambda x: x + 1, []) == []


def test_map_non_empty_list() -> None:
    assert ListOps([]).map(lambda x: x + 1, [1, 3, 5, 7]) == [2, 4, 6, 8]


def test_foldl_empty_list() -> None:
    assert ListOps([]).foldl(lambda acc, el: el * acc, [], 2) == 2


def test_foldl_direction_independent_function_applied_to_non_empty_list() -> None:
    assert ListOps([]).foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5) == 15


def test_foldl_direction_dependent_function_applied_to_non_empty_list() -> None:
    assert ListOps([]).foldl(lambda acc, el: el / acc, [1, 2, 3, 4], 24) == 64


def test_foldr_empty_list() -> None:
    assert ListOps([]).foldr(lambda acc, el: el * acc, [], 2) == 2


def test_foldr_direction_independent_function_applied_to_non_empty_list() -> None:
    assert ListOps([]).foldr(lambda acc, el: el + acc, [1, 2, 3, 4], 5) == 15


def test_foldr_direction_dependent_function_applied_to_non_empty_list() -> None:
    assert ListOps([]).foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24) == 9


def test_reverse_empty_list() -> None:
    assert ListOps([]).reverse([]) == []


def test_reverse_non_empty_list() -> None:
    assert ListOps([]).reverse([1, 3, 5, 7]) == [7, 5, 3, 1]


def test_reverse_list_of_lists_is_not_flattened() -> None:
    assert ListOps([]).reverse([[1, 2], [3], [], [4, 5, 6]]) == [
        [4, 5, 6],
        [],
        [3],
        [1, 2],
    ]


def test_foldr_foldr_add_string() -> None:
    assert (
        ListOps([]).foldr(
            lambda acc, el: el + acc, ["e", "x", "e", "r", "c", "i", "s", "m"], "!"
        )
        == "exercism!"
    )


def test_reverse_reverse_mixed_types() -> None:
    assert ListOps([]).reverse(["xyz", 4.0, "cat", 1]) == [1, "cat", 4.0, "xyz"]
