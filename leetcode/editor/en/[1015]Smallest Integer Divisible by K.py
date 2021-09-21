# Given a positive integer K, you need find the smallest positive integer N such
#  that N is divisible by K, and N only contains the digit 1. 
# 
#  Return the length of N. If there is no such N, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1. 
# 
#  Example 2: 
# 
#  
# Input: 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2. 
# 
#  Example 3: 
# 
#  
# Input: 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3. 
# 
#  
# 
#  Note: 
# 
#  
#  1 <= K <= 10^5 
#  Related Topics Math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K%2==0 or K%5==0: return -1
        num = 1
        for l in range(1, K+1):
            if num % K == 0: return l
            num = num *10 +1
        return -1
        
# leetcode submit region end(Prohibit modification and deletion)
