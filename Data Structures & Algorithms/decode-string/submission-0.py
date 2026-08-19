class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            
            elif c == "[":
                stack.append((curr, num))
                curr = ""
                num = 0
            elif c == "]":
                prev, repeat = stack.pop()
                curr = prev + repeat * curr
            
            else:
                curr += c
        return curr