class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     if node.val == subRoot.val:
        #         if self.isSame(node, subRoot):
        #             return True
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        # return False
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            

        
    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)