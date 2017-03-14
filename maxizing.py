#!/usr/bin/python3
def maxXor(l, r):
    P = l^r
    ret = 1
    while(P): # this one takes (m+1) = O(logR) steps
        ret <<= 1
        P >>= 1
    return (ret - 1)
l = int(input())
r = int(input())
print(maxXor(l, r))
