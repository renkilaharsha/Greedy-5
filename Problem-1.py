#Approach
# For every string and ? wave only if it matches the True else false. For * we have two aoptions we have choose any number of times
# if we have choosen it will match with current element [i][j-1] or [i-1][j] no choose case


#Complexities
#Time O(n*m)
#Space O(n*m)




class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    if (p[j - 1] == s[i - 1]) or (p[j - 1] == "?"):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False

        return dp[m][n]
