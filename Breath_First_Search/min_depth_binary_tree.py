


# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from collections import deque

def minDepth(self, root) : # output is an integer
    """"
        My Aapproach. Works

    """"
    if root : 
        queue = deque()
        queue.append(root)
        depth= 1

        while(queue):
            nodes_in_queue = len(queue) # implicitly this could be 1,2 

            for i in range(nodes_in_queue):
                curr = queue[0]
                if  curr.right==None and curr.left ==None  :
                    return depth # if found the leaf : THERE MUST BE LEAVES since is tree

                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                queue.popleft()
            depth +=1
    else:
        return 0     




if __name__ == "__main__" :

    # need to make tree before call minDepth
    minDepth(root)
