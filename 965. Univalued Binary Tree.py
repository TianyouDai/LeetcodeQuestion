class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        v = root.val
        
        def check(root,v):
            if root:
                if root.val != v:
                    return False
                return check(root.left,v) and check(root.right,v)
            else:
                return True
        
        return check(root,v)
