from functools import reduce
from typing import List, TypeVar
T = TypeVar("T")
def remove_duplicates(items: List[T]) -> List[T]:
    """
    Returns a new list with duplicates removed, preserving the order
    of first occurrences.
    """
    return reduce(
        lambda acc, x: acc if x in acc else acc + [x],
        items,
        [],
    )
# Tests
def run_tests():
    test_cases = [
        # (input, expected_output, description)
        ([1, 2, 3, 2, 4, 1, 5], [1, 2, 3, 4, 5],   "mixed duplicates"),
        ([1, 1, 1],              [1],                "all duplicates"),
        ([],                     [],                 "empty list"),
        ([42],                   [42],               "single element"),
        ([3, 1, 2, 1, 3],        [3, 1, 2],          "duplicates at start and end"),
        (["a", "b", "a", "c"],   ["a", "b", "c"],    "string elements"),
    ]
    passed = 0
    failed = 0
    for items, expected, description in test_cases:
        original = list(items)        # check immutability
        result   = remove_duplicates(items)

        ok_result    = result   == expected
        ok_immutable = items    == original

        if ok_result and ok_immutable:
            print(f"  PASS  {description}")
            passed += 1
        else:
            print(f"  FAIL  {description}")
            if not ok_result:
                print(f"got {result}, expected {expected}")
            if not ok_immutable:
                print(f" input was mutated: {items} (was {original})")
            failed += 1

    print(f"\n{passed} passed, {failed} failed")
if __name__ == "__main__":
    run_tests()
