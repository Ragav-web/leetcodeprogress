class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack:
                    return False
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack