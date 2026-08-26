class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "{" or char == "(" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False

                if char == "}" and stack.pop(-1) != "{":
                    return False
                if char == ")" and stack.pop(-1) != "(":
                    return False
                if char == "]" and stack.pop(-1) != "[":
                    return False

        return not stack