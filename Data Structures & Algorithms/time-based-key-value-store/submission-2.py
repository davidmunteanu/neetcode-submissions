class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeMap[key]: return ""

        emos = self.timeMap[key]
        left, right = 0, len(emos) - 1
        candidateIdx = -1

        while left <= right:
            mid = (left + right) // 2

            if emos[mid][0] > timestamp:
                right = mid -1  
            elif emos[mid][0] < timestamp:
                candidateIdx = max(candidateIdx, mid)
                left = mid + 1
            else:
                return emos[mid][1]

        return emos[candidateIdx][1] if candidateIdx != -1 else ""
        
