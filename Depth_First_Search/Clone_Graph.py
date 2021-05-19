# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/


 """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """"
    My solution. Works. Another approach is to use  the class itself for recursion seem to save time.
    """"
    
    def dfs(self, node, nodes_dict ):
        
        
        if node.val not in nodes_dict:
            nodes_dict[node.val] = Node(node.val )
        
        for neighbor in node.neighbors :
            if neighbor.val in nodes_dict :
                pass
            else:                
                self.dfs(neighbor, nodes_dict)
                
                
        
        nodes_dict[node.val].neighbors = [ nodes_dict[node.val] for node in  node.neighbors ]
        
        
                

    def cloneGraph(self, node: 'Node') -> 'Node':
        
        
        if node :            
            nodes_dict={}

            self.dfs( node, nodes_dict )
            
            return nodes_dict[node.val]
            
        else:
            return node

        
        
        