
#  || Various BFS running at the same time  ||

#  You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.TimeoutError

# https://leetcode.com/problems/walls-and-gates/

from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        """
        Works. My Brute Force Approach. There is a a better approach
        Instead Do multiple Bfs starting from the doors. look solution2
        Do not return anything, modify rooms in-place instead.
        
        """
        
        def isValid (row, col, rooms):
            n_rows = len(rooms)
            n_columns = len(rooms[0])
            if row >=0 and col  >=0 and row < n_rows and col < n_columns and rooms[row][col] != -1 :
                return True
            else :
                return False 
            
            
        def bfs(row, col, rooms):
            """
            Since is a grapg ned to add set to keep track of nodes,
            """
            queue =deque()
            seen=set()
            queue.append( (row, col) )
            seen.add((row, col))
            distance = 0 
            
            
            
            while(queue):
                curr_size =len(queue)
                
                for i in range(curr_size) :
                    
                    if rooms[ (queue[0])[0] ]  [(queue[0])[1]  ] == 0:
                        return distance
                    
                    row=(queue[0])[0] 
                    col=(queue[0])[1] 
                    
                    if isValid(row-1,col, rooms ) and (row-1,col ) not in seen  :
                        queue.append( (row-1,col) )
                        seen.add(  (row-1,col) )
                        
                    if isValid(row+1,col, rooms )  and (row+1, col) not in seen :
                        queue.append( (row+1,col) )
                        seen.add(  (row+1,col) )
                        
                    if isValid(row,col+1, rooms ) and (row, col+1) not in seen :
                        queue.append( (row,col+1) )
                        seen.add(  (row,col+1) )
                        
                    if isValid(row,col-1, rooms  ) and (row, col-1) not in seen :
                        queue.append( (row,col-1) )
                        seen.add(  (row,col-1) )
                    
                    queue.popleft()
                distance +=1
                
            return -1


        #MAIN 
        
        n_columns =len(rooms[0])
        n_rows =len(rooms)
        inf= 2147483647
        
        for row in range(n_rows) :
            for col in range(n_columns):
                if rooms[row][col] == 0 or rooms[row][col] == -1:
                    pass 
                else:
                    result =  bfs(row, col, rooms)
                    rooms[row][col] = inf  if result ==-1 else result
                
        
        
        
class Solution2:
    """
    works. best solution until know
    1) find all doors 
    2) Do simultaneous BFS for all doors and change values as I go along.
    """
    door=0
    empty= 2147483647
    obstacle = -1
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        
        """
        
        
        
        def isValid (row, col, rooms):
            n_rows, n_cols =len(rooms), len(rooms[0])
            
            
            
            if row >=0 and  col>=0 and  row <n_rows and col < n_cols and rooms[row][col] ==self.empty:
                return True
            else : 
                return False
            
            return 
        
        
        
        queue =deque()
        #Get all doors and place in
        n_rows =  len(rooms)
        n_cols =  len(rooms[0])
        
        for row in range(n_rows) :
            for col in range(n_cols) : 
                if rooms[row][col] == self.door:
                    queue.append((row, col))
        
        
        # Simultaneous BFS
        while(queue):
            
            curr=  queue[0]
            # I want to append to queue the valid neighbors  AND change val 
            for r, c in [(curr[0]+1,curr[1]), (curr[0]-1,curr[1]), (curr[0],curr[1]+1), (curr[0],curr[1]-1)]:
                
                if isValid(r,c, rooms):
                    queue.append(((r,c)))
                    rooms[r][c] = rooms[curr[0]] [curr[1]] +1  # whatever the previous was +1
            
            queue.popleft()