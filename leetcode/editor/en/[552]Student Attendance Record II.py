# Given a positive integer n, return the number of all possible attendance recor
# ds with length n, which will be regarded as rewardable. The answer may be very l
# arge, return it after mod 109 + 7. 
# 
#  A student attendance record is a string that only contains the following thre
# e characters: 
# 
#  
#  
#  'A' : Absent. 
#  'L' : Late. 
#  'P' : Present. 
#  
#  
# 
#  
# A record is regarded as rewardable if it doesn't contain more than one 'A' (ab
# sent) or more than two continuous 'L' (late). 
# 
#  Example 1: 
#  
# Input: n = 2
# Output: 8 
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.
#  
#  
#  
# 
#  Note:
# The value of n won't exceed 100,000.
#  
# 
# 
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        Mod = 1e9 +7
        A = [0] * n
        P = [0] * n
        L = [0] * n
        A[0] = 1
        P[0] = 1
        L[0] = 1

        if n>1:
            L[1] = 3
            A[1] = 2
        if n>2:
            A[2] = 4
        for i in range(1,n):
            P[i] = (A[i-1] + P[i-1] + L[i-1]) % Mod
            if i>1: L[i] = (A[i-1] + P[i-1] + A[i-2] + P[i-2]) % Mod
            if i>2: A[i] = (A[i-1] + A[i-2] + A[i-3]) % Mod
        #print(A, P, L)
        return int((A[-1]+P[-1]+L[-1]) % Mod)

# leetcode submit region end(Prohibit modification and deletion)
