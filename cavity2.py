import sys

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)
num_of_elem=n
q=[]
x="X"
x=n-1
v=""
i=1
j=1
for i in range(1,num_of_elem-1):
    for j in range(1,num_of_elem-1):
      n=-1+i
      m=0+j
      if(grid[i][j]>grid[n][m]):
        n=i+0
        m=j+1
        if (grid[i][j]>grid[n][m]):
                  n=i+1
                  m=j+0
                  if(grid[i][j]>grid[n][m]):
                       n=i+0
                       m=j-1
                       if(grid[i][j]>grid[n][m]):
                             b=list(grid[i])
                             b[j]='X'
                             l=v.join(b)
                             q.append(l)
                             grid[i]=l
for i in range(num_of_elem):
    print(grid[i])
