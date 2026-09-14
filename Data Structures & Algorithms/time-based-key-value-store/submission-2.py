class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.arr:
            return ""
        array = self.arr[key]
        i, j = 0, len(array)
        while i < j:
            mid = i + (j-i)//2
            if array[mid][0] <= timestamp:
                i = mid + 1
            else:
                j = mid
        if i == 0:
            return ""
        return array[i-1][1]