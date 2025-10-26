from typing import List
import sys

def insertion_sort_desc(arr: List[int]) -> List[int]:
    """Sort a list in-place in monotonically decreasing order using insertion sort.

    Args:
        arr: List of integers.
    Returns:
        The same list object, sorted in decreasing order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def _parse_input(args: List[str]) -> List[int]:
    """Parse numbers either from argv or stdin."""
    if len(args) > 1:
        tokens = " ".join(args[1:]).split()
    else:
        data = sys.stdin.read().strip()
        if not data:
            # default demo
            tokens = ["8", "3", "1", "7", "0", "10", "2"]
        else:
            tokens = data.split()
    try:
        return [int(t) for t in tokens]
    except ValueError:
        raise SystemExit("Error: Please provide only integers (e.g., 10 3 7 1 2).")

if __name__ == "__main__":
    nums = _parse_input(sys.argv)
    print("Original:", nums)
    insertion_sort_desc(nums)
    print("Sorted (decreasing):", nums)
