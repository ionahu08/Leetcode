class Solution:
    def maxDepth(self, s: str) -> int:
        ans = [0]
        self.dfs(0, s, 0, ans)
        return ans[0]

    def dfs(self, idx, s, l, ans):
        # print(idx, ans[0])
        if idx == len(s):
            return 

        if s[idx] not in ("(", ")"):
            self.dfs(idx+1, s, l, ans)
        elif s[idx] == "(":
            ans[0] = max(ans[0], l+1)
            self.dfs(idx+1, s, l+1, ans)
        elif s[idx] == ")":
            self.dfs(idx+1, s, l-1, ans)

        