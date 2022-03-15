class Solution:
    def isValid(self, s: str) -> bool:
        c = (')', '}', ']')
        if len(s)%2 ==1:
            return False
        stack = []
        for i in s:
            if i in c:
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                elif i == ']' and stack[-1] != '[':
                    return False
                elif i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

