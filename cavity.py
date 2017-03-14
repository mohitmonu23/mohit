import sys

n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)
print(grid)
print("two dimensional",grid[2][1])
q=[]
x="X"
#q=grid[0]
#print("hvjhb",q[1:2])
#q=grid
x=n-1
print("ggjg",x)
n=0
m=1
v=""
if(grid[1][1]>grid[n][m]):
  print("1 the N AND M",n,m)
  t=n
  n=m
  m=t
  print("a1 the N AND M",n,m)
  if(grid[1][1]>grid[n][m]):
        print("2 the N AND M",n,m)
        #print(n)
        n=n+1
        m=m+1
        print("a2 the N AND M",n,m)
        if(grid[1][1]>grid[n][m]):
            print("3 the N AND M",n,m)
            n=n-1
            m=m+1
            print("a3 the N AND M",n,m)
            if(grid[1][1]>grid[n][m]):
                print("4the N AND M",n,m)
                b=list(grid[1])
                b[1]='X'
                l=v.join(b)
                print('oooo',l)
                print(b)
                print(grid)
                q.append(l)
                print("a4 the N AND M",n,m)
print(q[0])
