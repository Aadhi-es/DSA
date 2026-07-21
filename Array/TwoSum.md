# Two Sum

## Pattern
Hash Map

## Brute Force
Nested loops
O(n²)

## Optimized
Hash Map
O(n)

## Mistake I made

Initially I created the dictionary before the loop.
That allowed using the current element.

Correct approach:
Check first, then store.

## What I learned

The hash map should contain only previously seen elements.
First store the current value and subtract , find if the remaining is present 
