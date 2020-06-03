# Problem 1: Square Root of an Integer

To calculate the floored root of a number, it is clear the square root of that number will lie in the range [1, number]. But. Instead of checking each number on this range, the idea is to use binary search in order to efficiently find the floor square root of the number in O( log n) time complexity.

## Time Space Complexity

**Time → O(log n)**, because we use binary search to search for the square root. 

**Space → O(1)**, we return a single value, the square floored root of the number.