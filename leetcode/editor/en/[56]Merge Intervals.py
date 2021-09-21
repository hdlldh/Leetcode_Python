#Given a collection of intervals, merge all overlapping intervals. 
#
# Example 1: 
#
# 
#Input: [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# 
#
# Example 2: 
#
# 
#Input: [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping. 
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature. 
# Related Topics Array Sort



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n<=1: return intervals
        intervals.sort(key=lambda x: x[0])
        ans = []
        i = 0
        j = 1
        while j<n:
            if intervals[j][0] > intervals[i][1]:
                ans.append(intervals[i])
                i = j
            else:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
            j += 1
        ans.append(intervals[i])
        return ans


        
#leetcode submit region end(Prohibit modification and deletion)
