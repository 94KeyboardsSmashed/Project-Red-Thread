#(Coordinates of oat at which the slime mold starts at)
begin = [0,0] 

#(Coordinates of oat at which the goal is)
end = [14,14] 

#(Coordinates of walls and empty spaces, arranged in wS[x][y] in which x is the x coordinate and y is the y coordinate of the wall/empty space)
wS = [[0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
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
      [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0]]

#(Array with all tunnel networks of the slime mold, each tunnel is described as several coordinates,
# with each consecutive coordinate being within the Moore neighborhood of the previous and next coordinate, 
# in which nutrition moves. For example, a tNet value of [[[0,0],[1,0],[2,0]]] 
# would show that there is 1 tunnel that transports food from (0,0) to (1,0), then to (2,0)) 
tNet = [[[0,0]]] 

# (List of all coordinates in which a tunnel is present)
tNet_raw = [[0,0]] 

# Size of wS measured by length of wS + 1.
m = 14 

#(Function that outputs next generation of plasmodium which is still in its growing stage)
def nex():
 #(Value that is returned) 
 re = [] 

 #(Value that is used for creating a multidimensional array)
 coords = [] 

 #(Iterates over all tunnels present in tNet)
 for i in range(0,len(tNet)): 
   coords = []

  # (Describes x and y of the end of the tunnel)
   x = tNet[i][len(tNet[i])-1][0]
   y = tNet[i][len(tNet[i])-1][1] 

   # (All the rest of the code creates tunnels that branch off of the previous tunnel
   # network (using Moore neighborhood) and add it to the return value)
   if (x - 1) >= 0 and wS[x-1][y] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x-1,y])
     re.append(coords)
     coords = []
   if (x + 1) <= m and wS[x+1][y] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x+1,y])
     re.append(coords)
     coords = []
   if (y - 1) >= 0 and wS[x][y-1] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x,y-1])
     re.append(coords)
     coords = []
   if (y + 1) <= m and wS[x][y+1] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x,y+1])
     re.append(coords)
     coords = []
   if wS[y][x] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x,y])
     re.append(coords)
     coords = []
   if (y+1) <= m and (x+1) <= m and wS[x+1][y+1] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x+1,y+1])
     re.append(coords)
     coords = []
   if (y-1) >= 0 and (x-1) >= 0 and wS[x-1][y-1] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x-1,y-1])
     re.append(coords)
     coords = []
   if (y-1) >= 0 and (x+1) <= m and wS[x+1][y-1] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x+1,y-1])
     re.append(coords)
     coords = []
   if (y+1) >= 0 and (x-1) <= m and wS[x-1][y+1] == 0:
     for j in tNet[i]:
       coords.append(j)
     coords.append([x-1,y+1])
     re.append(coords)
     coords = []
 return re

# (Function that converts tNet to tNet_raw)
def next_raw(): 
 coords1 = []
 for i in range(0,len(tNet)): #(Iterates over tunnels)
   x = tNet[i][len(tNet[i])-1][1] #(Describes x and y)
   y = tNet[i][len(tNet[i])-1][0]
   if wS[y][x] == 0:
     coords1.append([x,y])
 return coords1

# (Function that creates array that can be easily visualized with plasmodium, walls, and empty spaces)
def mesh(): 
 meshm = []
 for i in range(0,len(wS)): #(Part of process that checks every coordinate (Part 1))
   b = []
   for j in range(0,len(wS[i])): #(Part of process that checks every coordinate (Part 2))
     if tNet_raw.count([j,i]) > 0: #(Checks if tunnel is present at coordinate)
       b.append(1)
     else:
       if wS[i][j] > 0: #(Checks if wall is present at coordinate)
         b.append(2)
       else: #(displays 0 if none are present)
         b.append(0)
   meshm.append(b)
 return meshm

# (Function that checks if plasmodium has reached the goal)
def check(): 
 sum = 0
 for k in tNet:
   if k.count(end) > 0: #(counts all tunnels that led to the goal)
     sum += 1
 if sum > 0:
   return True #(True means that the plasmodium has reached the goal)
 else:
   return False

# (Function that returns a set of all solutions of the shortest path problem)
def y(): 
 y_var = []
 for k in tNet:
   if k.count(end) > 0:
     y_var.append(k)
 return y_var

# (Function that returns raw coordinates for each point in the solution set)
def solution_raw(): 
 coords1 = []
 for i in range(0,len(y())):
   for j in y()[i]:
     coords1.append(j)
 return coords1

# (Function that creates a visual of the solution set, walls, and empty spaces)
def solution_mesh(): 
 sm = []
 for i in range(0,len(wS)): #(Part of process that checks every coordinate (Part 1))
   b = []
   for j in range(0,len(wS[i])): #(Part of process that checks every coordinate (Part 2))
     if solution_raw().count([i,j]) > 0: #(Checks if tunnel occupies the coordinate)
       b.append(1)
     else:
       if wS[i][j] > 0: #(Checks if wall occupies the coordinate)
         b.append(2)
       else: #(Puts 0 if none of the two are present)
         b.append(0) 
   sm.append(b)
 return sm

# (Function that can display a 2D array)
def display(array): 
 for a in array:
   print(a)

#(Actual running of the algorithm (set to display generations and solution mesh on console))

#(Resets time for algorithm)
t = 0 

# (Repeats following code while the plasmodium grows and is not at the goal)
while check() == False: 
 #(Displays the time passed since the plasmodium began growing)
 print("Time: " + str(t)) 

 # (Displays the mesh (maze with plasmodium and walls))
 display(mesh()) 

 # (Separates generations from each other to avoid confusion)
 print("\n") 

 # (Evolves the plasmodium by one step (tunnels branch out 1 unit))
 tNet = nex() 

 # (Resets raw coordinates for each location that has a tunnel)
 tNet_raw = next_raw() 
 t = t + 1 #(Increases time by 1)

print("\n\nSolution:") #(Separates growing plasmodium from solution plasmodium and labels it)
display(solution_mesh()) #(Displays the solution plasmodium with walls in the maze)
print("Time: " + str(t)) #(Displays time that it took for the slime mold to reach the end)
