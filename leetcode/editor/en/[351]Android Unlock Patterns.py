#Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys. 
#
# 
#
# Rules for a valid pattern: 
#
# 
# Each pattern must connect at least m keys and at most n keys. 
# All the keys must be distinct. 
# If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed. 
# The order of keys used matters. 
# 
#
# 
#
# 
# 
#
# 
#
# Explanation: 
#
# 
#| 1 | 2 | 3 |
#| 4 | 5 | 6 |
#| 7 | 8 | 9 | 
#
# Invalid move: 4 - 1 - 3 - 6 
#Line 1 - 3 passes through key 2 which had not been selected in the pattern. 
#
# Invalid move: 4 - 1 - 9 - 2 
#Line 1 - 9 passes through key 5 which had not been selected in the pattern. 
#
# Valid move: 2 - 4 - 1 - 3 - 6 
#Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern 
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2 
#Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern. 
#
# 
#
# Example: 
#
# 
# 
#Input: m = 1, n = 1
#Output: 9
# 
# 
# Related Topics Dynamic Programming Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        jumps = [[0] * 10 for _ in range(10)]
        jumps[1][7] = jumps[7][1] = 4
        jumps[1][3] = jumps[3][1] = 2
        jumps[1][9] = jumps[9][1] = 5
        jumps[2][8] = jumps[8][2] = 5
        jumps[3][9] = jumps[9][3] = 6
        jumps[3][7] = jumps[7][3] = 5
        jumps[4][6] = jumps[6][4] = 5
        jumps[7][9] = jumps[9][7] = 8

        ans = 0
        visited = [False] * 10
        ans += self.helper(jumps, m, n, 1, 1, visited, 0) * 4
        ans += self.helper(jumps, m, n, 2, 1, visited, 0) * 4
        ans += self.helper(jumps, m, n, 5, 1, visited, 0)

        return ans

    def helper(self, jumps, m, n, cur, l, visited, res):
        if l > n: return res
        if l >= m: res += 1
        visited[cur] = True
        for nxt in range(1, 10):
            if visited[nxt]: continue
            if jumps[cur][nxt] == 0 or visited[jumps[cur][nxt]]:
                res = self.helper(jumps, m, n, nxt, l + 1, visited, res)
                # print(cur, nxt, res)
        visited[cur] = False
        return res
#leetcode submit region end(Prohibit modification and deletion)
