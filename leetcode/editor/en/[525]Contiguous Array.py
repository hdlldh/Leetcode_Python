#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
#
#
# Example 1: 
# 
#Input: [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# 
# 
#
# Example 2: 
# 
#Input: [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# 
# 
#
# Note:
#The length of the given binary array will not exceed 50,000.
# Related Topics Hash Table



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum = 0
        mem = {0:-1}
        ans = 0
        for i, num in enumerate(nums):
            presum += 1 if num == 1 else -1
            if presum not in mem:
                mem[presum] = i
            else:
                ans = max(ans, i-mem[presum])
        return ans
#leetcode submit region end(Prohibit modification and deletion)
