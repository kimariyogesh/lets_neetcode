class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()','')
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')
        # return s==''

        # stack
        stack = []
        check = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in check:
                if stack and stack[-1] == check[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False