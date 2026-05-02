# Part 1 — Remove Duplicates (Functional Programming)

## Approach
The function uses functools.reduce to build a new list from left to right.
For each element:
- If it is already in the result, it is skipped
- Otherwise, it is added to the result
This preserves the original order while removing duplicates.
# key points 
- Pure function 
- Input list is not modified
- Uses immutability
  
## Time Complexity
O(n²) due to the membership check for each element.

## How to Run
python part1.py
