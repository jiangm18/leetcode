def cycleLeader(a, start, n):
    print a
    print 'start with' + str(start)
    pre = a[start-1]
    mod = 2*n+1
    nex = (start*2%mod)-1

    while(nex!=(start-1)):
        t = pre
        pre = a[nex]
        a[nex] = t
        nex = (2*(nex+1)%mod)-1
        print a
    a[start-1] = pre

a = [1,2,3,4,5,6,7,8]
cycleLeader(a, 1, 4)
cycleLeader(a, 3, 4)
print a
