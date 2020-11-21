# https://www.codechef.com/JULY20B/problems/CHFNSWPS
 

 # cook your dish here
from collections import Counter
def fun(a,b):
    aa=Counter(a)
    bb=Counter(b)
    h={}
    mi=1e10
    for i in range(0,len(a)):
        mi=min(mi,a[i])
    for i in range(len(b)):
        mi=min(mi,b[i])
    l_a=list((aa-bb).elements())
    l_b=list((bb-aa).elements())
    for i in range(len(a)):
        if a[i] not in h:
            h[a[i]]=1
        else:
            h[a[i]]+=1
    for i in range(len(b)):
        if b[i] not in h:
            h[b[i]]=1
        else:
            h[b[i]]+=1
    for key,val in h.items():
        if val%2!=0:
            return -1
    l_b.sort
    l_a.sort()
    l_b.sort(reverse=True)
    #print(l_b)
    s_min=0
    for i in range(0,len(l_a),2):
        s_min+=min(2*mi,min(l_a[i],l_b[i]))
    return (s_min)
t=int(input())
for i in range(t):
    n=int(input())
    a=list(int(x) for x in input().split())
    b=list(int(x) for x in input().split())
    print(fun(a,b))