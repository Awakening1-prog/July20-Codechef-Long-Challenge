# https://www.codechef.com/JULY20B/problems/PTMSSNG/


# cook your dish here
t1=int(input())
for i in range(t1):
    n1=int(input())
    h_x1={}
    a,b=0,0
    h_y1={}
    for i in range(4*n1-1):
        x,y=map(int,input().split())
        if x not in h_x1:
            h_x1[x]=1
        else:
            h_x1[x]+=1
        if y not in h_y1:
            h_y1[y]=1
        else:
            h_y1[y]+=1
    for key,val in h_x1.items():
        if val%2!=0:
            a=key
    for key,val in h_y1.items():
        if val%2!=0:
            b=key
    print(a,b)