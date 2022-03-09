from typing import List

def find_missing_number(collections: List[int]) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    """
    missing_number = 0
    cmp = 0
    for x, n in enumerate(collections):
        missing_number ^= n 
        cmp^=x
    cmp^=(len(collections))
    return missing_number^cmp


if __name__ == "__main__":
    assert find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert find_missing_number([11, 5, 4, 9, 7, 10, 8, 1, 2, 3, 0])
    assert find_missing_number([3, 0, 1])
    print("All tests passed successfully!")
