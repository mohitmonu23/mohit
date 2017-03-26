n = int(input())
a = list(map(int, input().split(' ')));
# print(*a)
maxValue = 0
for i in range(0,n):
    curMax = 0
    for j in range(i+1,n):
        # print(str(a[j])+" is the j value "+str(a[i])+" is the i value")
        if a[j] is (a[i]+1):
            # print("This runs")
            curMax = curMax + 1
        elif a[j] is a[i]:
            curMax = curMax + 1 
    if maxValue < curMax:
        maxValue = curMax
print(maxValue+1)
