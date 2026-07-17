class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pth_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for c in s:
            if c in '({[':
                stack.append(c)

            else:
                if not stack:
                    return False
                if stack[-1] == pth_dict[c]:
                    stack.pop()
                else:
                    return False
                
        return not stack

            