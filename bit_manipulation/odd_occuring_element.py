"""
A program to find the element, which is repeated odd number of times.
"""
import doctest
from typing import List

def get_odd_occurrences(collections: List[int]) -> int:
    """
    -------
    Time complexity: O(n)
    n is the number of elements in the array. 
    --------
    Space complexity: O(1)
    --------
    Test 
    >>> get_odd_occurrences([1, 1, 2, 2, 4, 4, 4, 5, 5, 8, 8, 9, 9, 9, 9])
    4
    """
    res = 0
    for i in collections:
        res^=i
    return res


if __name__ == "__main__":
    doctest.testmod()
    print("All tests passed successfully!")
