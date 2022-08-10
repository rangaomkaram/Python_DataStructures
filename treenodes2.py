class TreeNode():
    def __init__(self,key):
        self.key,self.left,self.right = key ,None , None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left),)