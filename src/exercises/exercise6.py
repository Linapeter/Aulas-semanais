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

        Args:
            length (int): length of list
        """
        self.objects = objects

    def get(self) -> list[Any]:
        return self.objects

    def __repr__(self) -> str:
        return f"List = {self.objects}"

    def append(self,new_objects: list[Any]) -> list[Any]:
        self.objects += new_objects
        return self.objects

    def concat(self,serie_of_list: list[list[Any]]) -> list[Any]:
        for item in serie_of_list:
            self.objects += item
        return self.objects

    def filter(self,condition: Callable[[Any],bool])-> list[Any]:
        return [item for item in self.objects if condition(item)]

    def length(self, list_len:list[Any]) -> int:
        return len(list_len)

    def map(self,function_map: Callable[[Any],Any]) -> list[Any]:
        return [function_map(mapped) for mapped in self.objects]

    def foldl(self, function_fold: Callable[[Any,int],Any], acc: int) -> list[Any]: # left to right
        return [function_fold(item,acc) for item in self.objects]

    def foldr(self, function_fold: Callable[[Any,int],Any], acc: int) -> list[Any]: # right to left
        return [function_fold(item,acc) for item in reversed(self.objects)]

    def reverse(self) -> list[Any]:
        return [reversed(self.objects)]

# Tests

def condition(number_cond: int) -> bool:
    if number_cond > 5:
        return True
    return False                # Não precisa de else
l1 = [3,4,5,6,7,8]
list1 = ListOps(l1)
print(list1.filter(condition))
print(list1.get())

def substract1(number_ex:int)-> int:
    return number_ex - 1
print(list1.map(substract1))

def substract(x:int,y:int)-> Any:
    return x-y

