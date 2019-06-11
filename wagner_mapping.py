begin = [0,0]
end = [14,14]
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
tNet = [[[0,0]]]
tNet_raw = [[0,0]]
m = 14

def nex():
 re = []
 coords = []
 for i in range(0,len(tNet)):
   coords = []
   x = tNet[i][len(tNet[i])-1][0]
   y = tNet[i][len(tNet[i])-1][1]
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

def next_raw():
 coords1 = []
 for i in range(0,len(tNet)):
   x = tNet[i][len(tNet[i])-1][1]
   y = tNet[i][len(tNet[i])-1][0]
   if wS[y][x] == 0:
     coords1.append([x,y])
 return coords1

def mesh():
 meshm = []
 for i in range(0,len(wS)):
   b = []
   for j in range(0,len(wS[i])):
     if tNet_raw.count([j,i]) > 0:
       b.append(1)
     else:
       if wS[i][j] > 0:
         b.append(2)
       else:
         b.append(0)
   meshm.append(b)
 return meshm

def check():
 sum = 0
 for k in tNet:
   if k.count(end) > 0:
     sum += 1
 if sum > 0:
   return True
 else:
   return False

def y():
 y_var = []
 for k in tNet:
   if k.count(end) > 0:
     y_var.append(k)
 return y_var

def solution_raw():
 coords1 = []
 for i in range(0,len(y())):
   for j in y()[i]:
     coords1.append(j)
 return coords1

def solution_mesh():
 sm = []
 for i in range(0,len(wS)):
   b = []
   for j in range(0,len(wS[i])):
     if solution_raw().count([i,j]) > 0:
       b.append(1)
     else:
       if wS[i][j] > 0:
         b.append(2)
       else:
         b.append(0)
   sm.append(b)
 return sm

def display(array):
 for a in array:
   print(a)

t = 0

while check() == False:
 print("Time: " + str(t))
 display(mesh())
 print("\n")
 tNet = nex()
 tNet_raw = next_raw()
 t = t + 1

print("\n\nSolution:")
display(solution_mesh())
print("Time: " + str(t))