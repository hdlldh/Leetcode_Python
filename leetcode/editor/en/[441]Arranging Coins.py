# You have a total of n coins that you want to form in a staircase shape, where 
# every k-th row must have exactly k coins. 
#  
#  Given n, find the total number of full staircase rows that can be formed. 
# 
#  n is a non-negative integer and fits within the range of a 32-bit signed inte
# ger. 
# 
#  Example 1:
#  
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
#  
#  
# 
#  Example 2:
#  
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
#  
#  Related Topics Math Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
