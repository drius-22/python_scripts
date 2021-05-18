
from collections import deque

class Solution:  
    """
      Works. Look at implementation with DFS as well they both work.
    """
    
    def is_valid(self, r, c, grid):
        # n_rows = len (grid)
        # n_colms= len (grid[0])
        
        if r >=0 and r< self.n_rows and c >=0 and c < self.n_colms and grid[r][c] == "1":
            return True
        else:
            return False
        
    
    def dfs(self, row,col, grid):
        grid[row][col] = 0
        for r, c  in [(row,col+1), (row,col-1), (row+1,col), (row-1,col)] :
            if self.is_valid(r,c, grid):
                
                self.dfs(r, c, grid )
        
        
    def bfs(self, row, col, grid):
        grid[row][col] = "0" 
        queue=deque()
        queue.append( (row,col) )
        
        while (queue):
            
            curr_size =len(queue)
            
            
            for i in range(curr_size):
                
                curr_r = (queue[0] )[0]
                curr_c = (queue[0] )[1]
                
                for r,c  in [(curr_r,curr_c+1), (curr_r,curr_c-1), (curr_r+1,curr_c), (curr_r-1,curr_c)] :
                    
                    if self.is_valid(r,c,grid) :
                        grid[r][c] = "0"                         
                        queue.append( (r,c) )
                
                queue.popleft()
                    
        
                
                

                  
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        self.n_rows =  len(grid)
        self.n_colms= len (grid[0])
        n_islands = 0

        for row in range(self.n_rows):
            for col in range (self.n_colms ):
                
                if self.is_valid(row, col, grid):
                    n_islands +=1 

                    self.bfs(row, col, grid)
                
                    
                    
                    
        return n_islands

