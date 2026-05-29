class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceToOrigin(x, y):
            return x ** 2 + y ** 2

        heap = []
        for x, y in points:
            distance = distanceToOrigin(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (-distance, x, y))
            else:
                heapq.heappushpop(heap, (-distance, x, y))
        return [[x, y] for d, x, y in heap]