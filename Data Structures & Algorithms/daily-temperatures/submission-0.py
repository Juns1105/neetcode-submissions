class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = []

        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                output[stack[-1]] = i - stack[-1]
                stack.pop()
                # output[i] = stack[-1]
                # stack.pop()

            stack.append(i)

        return output