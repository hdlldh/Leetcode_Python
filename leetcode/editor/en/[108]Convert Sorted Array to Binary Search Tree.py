#Given an array where elements are sorted in ascending order, convert it to a height balanced BST. 
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
#
# Example: 
#
# 
#Given the sorted array: [-10,-3,0,5,9],
#
#One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#      0
#     / \
#   -3   9
#   /   /
# -10  5
# 
# Related Topics Tree Depth-first Search



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, start, end):
        if start>end: return None
        mid = start+(end-start)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, start, mid-1)
        root.right = self.helper(nums, mid+1, end)
        return root
#leetcode submit region end(Prohibit modification and deletion)
