# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        dq = deque([(root, 0)])

        while dq:
            cur, level = dq.popleft()

            if cur.left:
                dq.append((cur.left, level+1))
            if cur.right:
                dq.append((cur.right, level+1))
                
            if len(res) == level:
                res.append([cur.val])
            else:
                res[level].append(cur.val)

        return res