# There are 2N people a company is planning to interview. The cost of flying the
#  i-th person to city A is costs[i][0], and the cost of flying the i-th person to
#  city B is costs[i][1]. 
# 
#  Return the minimum cost to fly every person to a city such that exactly N peo
# ple arrive in each city. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people inte
# rviewing in each city.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= costs.length <= 100 
#  It is guaranteed that costs.length is even. 
#  1 <= costs[i][0], costs[i][1] <= 1000 
#  Related Topics Greedy


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n==0: return 0
        n = n//2
        costs.sort(key=lambda x: x[0]- x[1])
        ans = 0
        for i in range(n):
            ans += costs[i][0] + costs[i+n][1]
        return ans



        
# leetcode submit region end(Prohibit modification and deletion)
