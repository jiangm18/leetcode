def quickSort(A, start, end):
    if start < end:
        pivot = partition(A, start, end)
        quickSort(A, start, pivot-1)
        quickSort(A, pivot+1, end)
def partition(A, start, end):
    x = A[end]
    i = 0     #next index of first part end 
    j = 0     #next index of second part end
    while(j <= end-1):
        if A[j] < x:
            A[i],A[j] = A[j],A[i]
            i = i + 1
        j = j + 1
    A[i],A[end] = A[end],A[i]
    return i

A = [1,4,6,8,8,4,3,3]
quickSort(A, 0, len(A)-1)
print A
    
            
    
        
