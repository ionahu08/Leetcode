class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        temp = 0 
        for i in range(len(s)):
            if s[i] == "(":
                temp += 1
                ans = max(temp, ans)
            elif s[i] == ")":
                temp -= 1
        return ans
                
        