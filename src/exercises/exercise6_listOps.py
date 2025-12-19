# https://exercism.org/tracks/python/exercises/list-ops

from typing import Any, Callable

list_kind = list[Any] | list[list[Any]] | Any


class ListOps:

    def __init__(self, objects: list[Any]) -> None:
        """Definition of items from class: list and length of list"""
        self.objects = objects

    def get(self) -> list[Any]:
        return self.objects

    def __repr__(self) -> str:
        return f"List = {self.objects}"

    def append(self, *new_objects: list[Any]) -> list[Any]:
        """given two lists, add all items in the second list to the end of the first list"""
        for lst in new_objects:
            self.objects += lst
        return self.objects

    def concat(self, series_of_list: list[list[Any]]) -> list[Any]:
        """given a series of lists, combine all items in all lists into one flattened list"""
        for item in series_of_list:
            self.objects += item
        return self.objects

    def filter(
        self, condition: Callable[[Any], bool], list_filter: list[Any]
    ) -> list[Any]:
        """given a predicate and a list, return the list of all items for which predicate(item) is True"""
        return [item for item in list_filter if condition(item)]

    def length(self, list_len: list[Any]) -> int:
        """given a list, return the total number of items within it"""
        return len(list_len)

    def map(self, function_map: Callable[[Any], Any], list_map: list[Any]) -> list[Any]:
        """given a function and a list, return the list of the results of applying function(item) on all items"""
        return [function_map(mapped) for mapped in list_map]

    def foldl(
        self,
        function_fold: Callable[[Any, Any], Any],
        l_list: list_kind,
        acc: int,
    ) -> int:  # left to right
        """given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left"""
        for item in l_list:
            acc = function_fold(acc, item)
        return acc

    def foldr(
        self, function_fold: Callable[[Any, Any], Any], r_list: list_kind, acc: int | str
    ) -> int | str:  # right to left
        """given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right"""
        for item in reversed(r_list):
            acc = function_fold(acc, item)
        return acc

    def reverse(self, reverse_lists: list_kind) -> list_kind:
        """given a list, return a list with all the original items, but in reversed order"""
        return list(reversed(reverse_lists))
