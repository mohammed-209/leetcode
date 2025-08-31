# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dq = deque([(root, 0)])
        res = []
        last, lastLevel = root, 0

        while dq:
            cur, level = dq.popleft()
            if level != lastLevel:
                res.append(last.val)

            if cur.left:
                dq.append((cur.left, level+1))
            if cur.right:
                dq.append((cur.right, level+1))

            last, lastLevel = cur, level
        res.append(cur.val)

        return res
        
        # res = []
        # q = deque([root])

        # while q:
        #     rightSide = None
        #     qLen = len(q)

        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             rightSide = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if rightSide:
        #         res.append(rightSide.val)
        # return res