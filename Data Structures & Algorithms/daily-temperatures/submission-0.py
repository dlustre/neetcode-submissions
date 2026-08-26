class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # push the value and index to stack
        # so we can set the result when we backtrack
        # [(30, 0)]

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            currentTemp = temperatures[i]

            while stack and stack[-1][0] < currentTemp:
                _, previousIndex = stack.pop(-1)
                res[previousIndex] = i - previousIndex

            stack.append((currentTemp, i))

        return res