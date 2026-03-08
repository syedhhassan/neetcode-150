class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        bananas = float("inf")
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            curr = 0
            for pile in piles:
                curr += -(-pile // mid)
            if curr <= h:
                bananas = min(bananas, mid)
                high = mid - 1
            else:
                low = mid + 1

        return bananas
            