import sys
def eatenchocalate(ac,pr,wrdi):
     wraps=int(ac/pr)
     eaten=wraps
     while (wraps>=wrdi):
            newlyeaten=int(wraps/wrdi)
            eaten+=newlyeaten
            wraps=int(wraps%wrdi)
            wraps+=newlyeaten
     return eaten       
t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    answer=eatenchocalate(n,c,m)
    print(int(answer))
