"""instead of line 10 and further we can just type the command as follows to  do the same task
print([[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n])
"""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
newlist=[]
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):


            if (i + j + k) != n:

                l = []
                for m in range(0, 3):
                    if m == 0:
                        l.append(i)

                    if m == 1:
                        l.append(j)
                    if m == 2:
                        l.append(k)
                newlist.append(l)

print(newlist, end='')
