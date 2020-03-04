def prime(n):
    cnt=0
    for i in range(2,n//2+1):
        if(n%i==0):
            cnt+=1
            break
    if(cnt==0):
        return True
    else:
        return False

def test(m):
    for i in range(2,m):
        p=False
        q=False
        for j in range(2,m):
            if(m==i*j):
                p=prime(i)
                q=prime(j)
                k=j
                break
        if(p==True and q==True and i!=j):
            return True

spn=[]

for i in range(4,100):
    n=i
    k=i-2
    for j in range(2,i):
        m=j
        if(k!=1):  
            if(n==(m+k)):
                p=test(m)
                q=test(k)
                if(p==True and q==True):
                    if(spn.count(i)==0):
                        spn.append(i)
                k=k-1
            else:
                k=k-1
print(spn)
n=int(input("enter n:"))
if(spn.count(n)==1):
    print("Yes",end="")
else:
    print("No",end="")
            
