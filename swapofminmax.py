n=int(input())
lists =[]
lists = list(map(int,input().split(' ')))
mini = 0
maxi = 0
maxnum = 0
minnum = 99999
for index,value in enumerate(lists):
    # print(index)
    if(value < minnum):
       minnum = value
       mini = index
      
    elif(value >= maxnum):
        maxnum = value
        maxi = index
        
print("minindex = "+str(mini)+" Max index "+str(maxi))
# print(*lists)
lists[mini],lists[maxi]=lists[maxi],lists[mini]
print(*lists)
    
