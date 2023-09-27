# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width_info = []
        def dfs(node, height, place):
            if len(width_info) <= height:
                width_info.append([place,place])
            
            width_info[height][0] = min(width_info[height][0], place)
            width_info[height][1] = max(width_info[height][1], place)
            if node.left:
                dfs(node.left, height+1, place*2 - 1)
            if node.right:
                dfs(node.right, height+1, place*2)
        dfs(root, 0, 1)
        result = 0
        for i in range(len(width_info)-1, -1, -1):
            if result < width_info[i][1] - width_info[i][0] + 1:
                result = width_info[i][1] - width_info[i][0] + 1
                print(i)
        return result
