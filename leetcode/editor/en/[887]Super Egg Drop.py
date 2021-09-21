# You are given K eggs, and you have access to a building with N floors from 1 t
# o N. 
# 
#  Each egg is identical in function, and if an egg breaks, you cannot drop it a
# gain. 
# 
#  You know that there exists a floor F with 0 <= F <= N such that any egg dropp
# ed at a floor higher than F will break, and any egg dropped at or below floor F 
# will not break. 
# 
#  Each move, you may take an egg (if you have an unbroken one) and drop it from
#  any floor X (with 1 <= X <= N). 
# 
#  Your goal is to know with certainty what the value of F is. 
# 
#  What is the minimum number of moves that you need to know with certainty what
#  F is, regardless of the initial value of F? 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty th
# at F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: K = 2, N = 6
# Output: 3
#  
# 
#  
#  Example 3: 
# 
#  
# Input: K = 3, N = 14
# Output: 4
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= K <= 100 
#  1 <= N <= 10000 
#  
#  
#  
#  
#  Related Topics Math Binary Search Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        def f(x):
            ans = 0
            r = 1
            for i in range(1, K + 1):
                r *= x - i + 1
                r //= i
                ans += r
                if ans >= N: break
            return ans

        low = 1
        high = N
        while low <= high:
            mid = (low + high) // 2
            if f(mid) < N:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def superEggDrop2(self, K, N): # TLE
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0] * (N+1) for _ in range(K+1)]
        for j in range(1, N+1): dp[1][j] = j
        for i in range(2, K+1):
            for j in range(1, N+1):
                dp[i][j] = j
                left = 1
                right = j
                while left <= right:
                    mid = (left + right)//2
                    if dp[i-1][mid-1] < dp[i][j-mid]:
                        left = mid +1
                    else: right = mid -1
                dp[i][j] = min(dp[i][j], max(dp[i-1][left-1], dp[i][j-left])+1)
        return dp[K][N]

        
# leetcode submit region end(Prohibit modification and deletion)
