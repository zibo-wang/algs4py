"""Binary Search

"""

from typing import List


class BinarySearch:
    def __init__(self) -> None:
        pass

    def index_of(self, a: List[int], key: int) -> int:
        """Returns the index of the specified key in the specified array.

        Args:
            a: a the array of integers, must be sorted in ascending order
            key:  key the search key
        Returns:
            int: index of key in array a if present; -1 otherwise
        """

        lo: int = 0
        hi: int = len(a) - 1
        while lo <= hi:
            # Key is in a[lo..hi] or not present.
            mid: int = lo + (hi - lo) // 2
            if key < a[mid]:
                hi = mid - 1
            elif key > a[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

    @DeprecationWarning
    def rank(self, key: int, a: List[int]) -> int:
        """Returns the number of keys in the array that are smaller than key.

        Args:
            key: the search key
            a: the array of integers, must be sorted in ascending order
        Returns:
            int: the number of keys in the array that are smaller than key
        """
        return self.index_of(a, key)
