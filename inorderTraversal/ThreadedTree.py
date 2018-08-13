Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def inorderTraversal(self, root):
    res=[]
    if root == None:
        return res
    cur = root
    while(cur):
        if cur.left == None:   #cur.right has 2 cases: to the right child and return 
            res.append(cur.val)
            cur = cur.right
        else:
            pre = cur.left
            while(pre.right and pre.right != cur):
                pre = pre.right
            if pre.right == None: #connect to cur
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None    
                res.append(cur.val) 
                cur = cur.right  #turn to right
    return res
            
