class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        notFound = list()
        result = [0] * len(temperatures)

        for tempIdx, tempVal in enumerate(temperatures):
            if len(notFound) == 0:
                notFound.append(tempIdx)
                continue

            pastIdx = notFound.pop()
            pastVal = temperatures[pastIdx]

            if pastVal >= tempVal:
                notFound.append(pastIdx)
            
            while pastVal < tempVal:
                result[pastIdx] = tempIdx - pastIdx

                if len(notFound) > 0:
                    pastIdx = notFound.pop()
                    pastVal = temperatures[pastIdx]
                else:
                    break
            
            if len(notFound) > 0:
                notFound.append(pastIdx)
                
            notFound.append(tempIdx)
                
            

        return result