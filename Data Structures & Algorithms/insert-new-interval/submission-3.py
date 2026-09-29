class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = len(intervals) - 1

        while intervals and i >= 0 and intervals[i][0] > newInterval[0]:
            # print(intervals[i], "greater than", newInterval)
            i -= 1

        intervals.insert(i + 1, newInterval)

        result = []

        # print(intervals)
        for interval in intervals:
            # print(result)
            if not result:
                result.append(interval)
                continue
            
            if interval[0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
            else:                
                result.append(interval)

        return result