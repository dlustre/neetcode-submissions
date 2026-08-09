class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through s

        # for each open bracket, store in a stack

        # for each close bracket, check if the top of the stack corresponds. return False if not.

        # return True if everything is iterated

        stack = deque()

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if char == ')' and top != '(':
                    return False
                
                if char == '}' and top != '{':
                    return False
                
                if char == ']' and top != '[':
                    return False
                
        return not stack