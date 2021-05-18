

class Solution: 
    """
        Works. This is my DFS approach. 
        It can also be implemented using  BFS. 
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
                
                

                  
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        self.n_rows =  len(grid)
        self.n_colms= len (grid[0])
        n_islands = 0

        for row in range(self.n_rows):
            for col in range (self.n_colms ):
                
                if self.is_valid(row, col, grid):
                    n_islands +=1 

                    self.dfs(row, col, grid)
                    
                    
                    
        return n_islands
    
    



        
        
        
        
        
        
               
