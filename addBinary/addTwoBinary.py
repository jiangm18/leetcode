def addTwoBinary(a,b):
    if len(a) < len(b):
        a,b = b,a
    i = 0
    flag = 0
    while(i<len(b)):
        tmp = a[i] + b[i] + flag
        if tmp <= 1:
            a[i] = tmp
        else:
            a[i] = tmp%2
            flag = tmp/2
        i = i + 1
    if flag == 0:
        return a
    else:
        if i == len(a):
            a.append(1)
            return a
        else:
            while(i<len(a)):
                tmp = a[i] + flag
                a[i] = tmp%2
                flag = tmp/2
                i = i + 1
            if flag == 0:
                return a
            else:
                a.append(1)
                return a
a = [1,0,1,1,1]
b = [1,1,0]
print addTwoBinary(a,b)
                
    
