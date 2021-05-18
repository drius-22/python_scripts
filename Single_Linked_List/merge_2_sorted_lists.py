
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# https://leetcode.com/explore/interview/card/google/60/linked-list-5/3065/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
     Works. My solution.
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        prev_node=ListNode(None,None )
        head = prev_node
        
        while (l1 or l2):
            

            if l1 and l2:
                #they both exist: I m assuminf that all node have values 
                ls=  [l1.val] +[l2.val ]
                min_idx= ls.index( min(ls) )

                just_node= ListNode( min(ls), None  )
                prev_node.next = just_node                    
                prev_node= just_node

                if min_idx ==0 :
                    l1=l1.next
                else:
                    l2=l2.next


            elif l1:
                just_node= ListNode( l1.val, None  )
                
                prev_node.next = just_node
                prev_node = just_node           
                
                
                
                l1=l1.next


            else:
                just_node= ListNode(  l2.val , None  )                    
                prev_node.next = just_node
                prev_node=just_node

                l2=l2.next
                    
            
            
        return head.next
            


#  Smarter Solution 
class Solution2:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
