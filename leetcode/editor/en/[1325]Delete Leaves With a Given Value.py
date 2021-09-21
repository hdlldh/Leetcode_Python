# Given a binary tree root and an integer target, delete all the leaf nodes with
#  value target. 
# 
#  Note that once you delete a leaf node with value target, if it's parent node 
# becomes a leaf node and has the value target, it should also be deleted (you nee
# d to continue doing that until you can't). 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture 
# in left). 
# After removing, new nodes become leaf nodes with value (target = 2) (Picture i
# n center).
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: root = [1,3,3,3,2], target = 3
# Output: [1,3,null,null,2]
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: root = [1,2,null,2,null,2], target = 2
# Output: [1]
# Explanation: Leaf nodes in green with value (target = 2) are removed at each s
# tep.
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,1,1], target = 1
# Output: []
#  
# 
#  Example 5: 
# 
#  
# Input: root = [1,2,3], target = 1
# Output: [1,2,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= target <= 1000 
#  Each tree has at most 3000 nodes. 
#  Each node's value is between [1, 1000]. 
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root: return None
        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)
        if left is None and right is None:
            if root.val == target: return None
        root.left = left
        root.right = right
        return root
        
# leetcode submit region end(Prohibit modification and deletion)
