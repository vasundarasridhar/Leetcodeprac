"""Runtime: 42 ms, faster than 68.52% of Python3 online submissions for Find Leaves of Binary Tree.
Memory Usage: 13.8 MB, less than 73.99% of Python3 online submissions for Find Leaves of Binary Tree."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        leaves = []
        
        dummy = TreeNode( left = root)
        
        while dummy.left:
            leaves.append(self.traverse(root,dummy))
        
        return leaves
    
    
    def traverse(self, node, parent):
        
        if not node:
            return []
        
        elif (not node.left) and (not node.right):
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return [node.val]
        else:
            return self.traverse(node.left, node) + self.traverse(node.right, node)
            
            
