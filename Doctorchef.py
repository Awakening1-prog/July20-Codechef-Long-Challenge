# https://www.codechef.com/JULY20B/problems/DRCHEF


t=int(input())
for i in range(t):
    m,k=map(int,input().split())
    a=list(int(x) for x in input().split())
    #a.sort()
    c=0
    if len(set(a))==1:
        if a[0]<=k:
            print(len(a))
        else:
            c=0
            s=a[0]
            while s>k:
               # print(s)
                k1=s-k
                c+=1
                k=k*2
                k1=k1*2
                if k1>s:
                    s=s
                else:
                    s=k1
           # print(s)
            print(c+1+(m-1))
    else:
        a.sort()
        a=a[::-1]
        for i in range(len(a)):
            if a[i]<=k:
                c+=1
                k=k*2
            else:
                while a[i]>k:
                    #print(k)
                    k1=a[i]-k
                    #print(a[i])
                    k1=k1*2
                   # print(k1)
                    #print(k1,end=" ")
                    if k1>a[i]:
                        a[i]=a[i]
                    else:
                        a[i]=k1
                    k=k*2
                    #print("for" ,a[i])
                    c+=1
                if a[i]+k<k:
                    k=k*2
                    c+=1
                    break
                #print(k)
            #print(a[i])
        print(c)
          