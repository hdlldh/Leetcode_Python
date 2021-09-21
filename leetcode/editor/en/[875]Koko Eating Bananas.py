#Koko loves to eat bananas. There are N piles of bananas, the i-th pile has pile
#s[i] bananas. The guards have gone and will come back in H hours. 
#
# Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses
# some pile of bananas, and eats K bananas from that pile. If the pile has less t
#han K bananas, she eats all of them instead, and won't eat any more bananas duri
#ng this hour. 
#
# Koko likes to eat slowly, but still wants to finish eating all the bananas bef
#ore the guards come back. 
#
# Return the minimum integer K such that she can eat all the bananas within H ho
#urs. 
#
# 
#
# 
# 
#
# 
# Example 1: 
#
# 
#Input: piles = [3,6,7,11], H = 8
#Output: 4
# 
#
# 
# Example 2: 
#
# 
#Input: piles = [30,11,23,4,20], H = 5
#Output: 30
# 
#
# 
# Example 3: 
#
# 
#Input: piles = [30,11,23,4,20], H = 6
#Output: 23
# 
#
# 
#
# Note: 
#
# 
# 1 <= piles.length <= 10^4 
# piles.length <= H <= 10^9 
# 1 <= piles[i] <= 10^9 
# 
# 
# 
# 
# Related Topics Binary Search




#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        low =1
        high = max(piles)

        def possible(p):
            ans = 0
            for pile in piles: ans += (pile-1)//p + 1
            return ans<=H

        while low<=high:
            mid = low + (high-low)//2
            if possible(mid): high = mid -1
            else: low = mid +1
        return low
        
#leetcode submit region end(Prohibit modification and deletion)
