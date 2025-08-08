# append ();
# concatenate (given a series of lists, combine all items in all lists into one flattened list);
# filter (given a predicate and a list, return the list of all items for which predicate(item) is True);
# length (given a list, return the total number of items within it);
# map (given a function and a list, return the list of the results of applying function(item) on all items);
# foldl (given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left);
# foldr (given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right);
# reverse (given a list, return a list with all the original items, but in reversed order).
# Note, the ordering in which arguments are passed to the fold functions (foldl, foldr) is significant.

from typing import Any, Callable

class ListOps():

    def __init__(self, objects: list[Any])  -> None:
        """Definition of items from class: list and length of list
        """
        self.objects = objects

    def get(self) -> list[Any]:
        return self.objects

    def __repr__(self) -> str:
        return f"List = {self.objects}"

    def append(self,*new_objects: list[Any]) -> list[Any]:
        """given two lists, add all items in the second list to the end of the first list
        """
        for lst in new_objects:
            self.objects += lst
        return self.objects

    def concat(self,series_of_list: list[list[Any]]) -> list[Any]:
        """given a series of lists, combine all items in all lists into one flattened list
        """
        for item in series_of_list:
            self.objects += item
        return self.objects

    def filter(self,condition: Callable[[Any],bool])-> list[Any]:
        """given a predicate and a list, return the list of all items for which predicate(item) is True
        """
        return [item for item in self.objects if condition(item)]

    def length(self, list_len:list[Any]) -> int:
        """given a list, return the total number of items within it
        """
        return len(list_len)

    def map(self,function_map: Callable[[Any],Any]) -> list[Any]:
        """given a function and a list, return the list of the results of applying function(item) on all items
        """
        return [function_map(mapped) for mapped in self.objects]

    def foldl(self, function_fold: Callable[[Any,int],Any], acc: int) -> list[Any]: # left to right
        """given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left
        """
        return [function_fold(item,acc) for item in self.objects]

    def foldr(self, function_fold: Callable[[Any,int],Any], acc: int) -> list[Any]: # right to left
        """given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right
        """
        return [function_fold(item,acc) for item in reversed(self.objects)]

    def reverse(self) -> list[Any]:
        """given a list, return a list with all the original items, but in reversed order
        """
        return [reversed(self.objects)]
