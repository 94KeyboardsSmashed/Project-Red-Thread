import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

wS = np.array([[0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]])

testsolve = np.random.randint(0,255,wS.shape)

class slimemoldMapping:
    def __init__(self):
        self.grid = np.array([])
        self.solve = testsolve #np.array([]) 

    def add_maze(self, m_array):
        m_array[m_array != 0] = 100
        m_array[m_array == 0] = 255
        self.grid = m_array 

    def add_oat(self, x, y):
        self.grid[x][y] = 0
    
    def add_slime(self, x, y):
        self.grid[x][y] = 50

    def plot(self):
        fig, ax = plt.subplots() 
        img = ax.imshow(self.grid, interpolation='nearest', cmap='plasma')
        fig.colorbar(img, ax=ax)
        #fig.colorbar(maze, ax=ax)
        plt.show()

test = slimemoldMapping()
test.add_maze(wS) 
test.add_slime(0,0)
test.add_oat(14,14)
test.plot()