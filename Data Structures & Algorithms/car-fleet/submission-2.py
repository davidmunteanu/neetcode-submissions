class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        carStats = sorted(zip(position, speed), key=lambda x: x[0])
        fleets = 1

        prev = carStats.pop()
        prevTime = (target - prev[0]) / prev[1]

        while carStats:
            crnt = carStats.pop()
            crntTime = (target - crnt[0]) / crnt[1]

            if crntTime > prevTime:
                fleets += 1
                prevTime = crntTime

        return fleets