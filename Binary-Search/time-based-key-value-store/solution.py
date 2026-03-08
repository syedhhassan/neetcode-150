class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.map[key]:
            return ""

        val = self.map[key]
        result = ""
        l, r = 0, len(val) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val, mid_time = val[mid]
            if mid_time <= timestamp:
                result = mid_val
                l = mid + 1
            else:
                r = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)