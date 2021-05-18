
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#  https://leetcode.com/problems/symmetric-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def main():
    """
       Works. my solution 
    """

    def isSymetrical( ls ):
        
        if len(ls)%2 == 0:
            for i in range(int(len(ls)/2)) :
                ele1= ls[i].val if ls[i] else None
                ele2 = ls[len(ls)-i-1].val if ls[len(ls)-i-1] else None
                if ele1 != ele2 :
                    return False
            return True
                    
        else: 
            return False
        
        
                    
    def isSymmetric(self, root: TreeNode) -> bool:

        if root :     
     
            queue=deque()
            queue.append(root)
            step = 0

            while(queue):
                
                level=[]
                size_queue =len(queue)
                for i in range(size_queue):
                    curr= queue[0]
                    if curr:
                        queue.append(curr.left)
                        queue.append(curr.right)
                    level.append( queue.popleft())

                if step > 0 :
                    if not self.isSymetrical(level) :
                        return False
                step += 1 

            return True 


        else:
            return False

if __name__ == '__main__':
    main()


