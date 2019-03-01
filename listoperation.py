
if __name__ == '__main__':
    N = int(input())
l=[]
m=[]
for i in range(0,N):

    x = list(map(str, input().split()))
    l.append(x)

count=0
for i in range(0,N):



    if l[i][0]=='insert':

        man=int(l[i][2])
        k=int(l[i][1])

        m.insert(k,man)
        count=count+1

    elif l[i][0]=='print':
        print(m)


    elif l[i][0]=='append':
        z=int(l[i][1])



        m.append(z)
        count=count+1


    elif l[i][0]=='sort':
        for i in range(0,count):
            m[i]=int(m[i])
        m.sort()



    elif l[i][0]=='reverse':
    

        m.reverse()

    elif l[i][0]=='pop':
        m.pop()
        count=count-1

    elif l[i][0]=='remove':

        l[i][1]=int(l[i][1])

        m.remove(l[i][1])

        count=count-1





