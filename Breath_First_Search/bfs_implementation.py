
from collections import  deque

class node():
  def __init__(self, val=None, neighbors=[]):
    self.val = val
    self.neighbors = neighbors



def bfs (node):
    queue= deque() # FIFO : append to the end append   AND popleft()
    seen =set()
    queue.append(node)
    seen.add(node.val)

    while (queue):
        current_size= len(queue)

        for i in range(current_size): # i does not reference anywhere the loop itself is what we need. Iterate the same number of time as the q size at this specific point
            current = queue[0] # dont pop it yet 
            for neighbor in current.neighbors:
                if not neighbor.val in seen:
                    queue.append(neighbor)
                    seen.add(neighbor.val)

        print( queue.popleft().val )
        

if __name__ == '__main__':

    E=node('E')
    G=node('G')
    F=node('F', [G])



    B=node('B',[E])
    C=node('C',[E,F])
    D=node('D',[G])
    X=node('X',)

    A= node('A',[B,C,D,X])

    bfs(A)
