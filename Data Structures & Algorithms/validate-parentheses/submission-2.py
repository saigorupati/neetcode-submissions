class Solution:
    def isValid(self, s: str) -> bool:
        brack = {"}" : "{", "]": "[", ")" : "("}
        stack = []
        for i in range(len(s)):
            if s[i] in brack:
                print(s[i])
                print(stack)
                if stack and stack[-1] == brack[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False

        