# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, maxParent=None) -> int:
        if not root:
            return 0
        if maxParent == None:
            maxParent = root.val

        if root.val >= maxParent:
            maxParent = root.val

        left = self.goodNodes(root.left, maxParent)
        right = self.goodNodes(root.right, maxParent)

        return 1 + left + right if root.val >= maxParent else left + right
        
        
        
        # if not root:
        #     return []

        # if not root.right and not root.left:
        #     return 1
        
        # res = 0
        # stack = [(root, root.val)]
        # while stack:
        #     cur, maxParent = stack.pop()
        #     if cur.val >= maxParent:
        #         res+=1
        #         maxParent = cur.val


        #     if cur.left:
        #         stack.append((cur.left, maxParent))

        #     if cur.right:
        #         stack.append((cur.right, maxParent))

        # return res