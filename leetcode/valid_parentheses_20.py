class Solution:
    def isValid(self, s: str) -> bool:
        # stack solution
        #58 ms
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            #every key is the closing parenthesis
            if c in closeToOpen:
                #if last element in stack is the opening parenthesis
                if stack or stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
        #44ms
        # while "()" in s or "{}" in s or '[]' in s:
        #     s = s.replace("()", "").replace('{}', "").replace('[]', "")
        # return s == ''