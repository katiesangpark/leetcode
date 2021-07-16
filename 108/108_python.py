# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        x= len(nums)//2
        m= TreeNode (nums[x])
        x1 = nums[:x]
        x2 = nums[x+1:]
        m.left = self.sortedArrayToBST(x1)
        m.right = self.sortedArrayToBST(x2)
        
        return m 
        #time  = O(n)
        #space = o(n)