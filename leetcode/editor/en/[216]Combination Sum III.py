#
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers. 
#
# Note: 
#
# 
# All numbers will be positive integers. 
# The solution set must not contain duplicate combinations. 
# 
#
# Example 1: 
#
# 
#Input: k = 3, n = 7
#Output: [[1,2,4]]
# 
#
# Example 2: 
#
# 
#Input: k = 3, n = 9
#Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# Related Topics Array Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(k, n, 1, [], ans)
        return ans

    def dfs(self, k, n, start, out, ans):
        if k==0:
            if n==0: ans.append(out[:])
            return
        for i in range(start, 10):
            if i>n: break
            out.append(i)
            self.dfs(k-1, n-i, i+1, out, ans)
            out.pop()
        
#leetcode submit region end(Prohibit modification and deletion)
