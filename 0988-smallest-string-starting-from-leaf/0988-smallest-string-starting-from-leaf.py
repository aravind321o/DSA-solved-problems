# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = []

        def findPath(root , path):
            if not root:
                return
            if not (root.left or root.right):
                path += chr(root.val + 97)
                path = path[::-1]
                paths.append(path)
                return

            findPath(root.left , path + chr(root.val + 97))
            findPath(root.right , path + chr(root.val + 97))
        findPath(root , "")
        paths.sort()
        return paths[0]
        