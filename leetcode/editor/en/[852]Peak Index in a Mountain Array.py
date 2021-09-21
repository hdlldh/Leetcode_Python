# Let's call an array A a mountain if the following properties hold: 
# 
#  
#  A.length >= 3 
#  There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A
# [i] > A[i+1] > ... > A[A.length - 1] 
#  
# 
#  Given an array that is definitely a mountain, return any i such that A[0] < A
# [1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]. 
# 
#  Example 1: 
# 
#  
# Input: [0,1,0]
# Output: 1
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [0,2,1,0]
# Output: 1 
#  
# 
#  Note: 
# 
#  
#  3 <= A.length <= 10000 
#  0 <= A[i] <= 10^6 
#  A is a mountain, as defined above. 
#  
#  Related Topics Binary Search


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        low = 0
        high = N-1
        while low<=high:
            mid = low + (high-low)//2
            if mid>0 and A[mid]<A[mid-1]: high = mid -1
            else: low = mid +1
        return high
# leetcode submit region end(Prohibit modification and deletion)
