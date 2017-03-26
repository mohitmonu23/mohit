a=int(input())
for i in range(a):
    b=list(map(int,input().split(" ")))
    c=0
    x=abs(b[c]-b[c+2])
    y=abs(b[c+1]-b[c+2])
    if(x>y):
        print("Police2")
    if(x<y):
        print("police1")
    if(x==y):
        print("Both")
    
