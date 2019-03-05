def swap_case(s):
    
    l=[]
    for i in s:
        if i.isupper():
            l.append(i.lower())
            
        elif i.islower():
            l.append(i.upper())
        elif i.isspace():
            l.append(" ")
        else:
            l.append(i)
    new=""

    for x in l:
        new=new+x
    



    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
