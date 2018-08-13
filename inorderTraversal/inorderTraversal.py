class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def inorderTraversal(root):
    res = []
    stack = []
    p = root
    while(p or stack):
        while(p):
            stack.append(p)
            p = p.left
        p = stack.pop()
        res.append(p.val)
        p = p.right
    return res