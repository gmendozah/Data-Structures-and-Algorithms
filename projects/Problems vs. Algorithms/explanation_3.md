# Problem 3: Rearrange Array Digits
To solve this problem I implemented mergesort and reversed the process (from larger to smaller) this process takes O( n log n) time complexity and after sorting the array I implement two loops one to go through digits with even indices and the other to go through digits with odd indices both loops add O(n/2) + O(n/2) time complexity.
We end up with O(n log n) + O(n/2) + O(n/2) + which can be just simplified as O(n log n).

## Space Time Complexity

**Time → O(n log n)**, because we use merge sort.

**Space → O(1)**, we just have number_1 and number_2 return values.