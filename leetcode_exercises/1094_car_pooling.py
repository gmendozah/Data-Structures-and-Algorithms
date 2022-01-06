from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        q = []
        for n, start, end in trips:
            q.append((start, n))
            q.append((end, -n))
        total = 0
        for location, number in sorted(q):
            total += number
            if total > capacity:
                return False
        return True


s = Solution()
print(s.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4) == False)
