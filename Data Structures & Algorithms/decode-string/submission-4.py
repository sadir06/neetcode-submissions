class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stack.append(cur)
                nums.append(k)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = stack.pop()
                num = nums.pop()
                cur += temp*num
            else:
                cur += c
        return cur
