def mergeSort(A, start, end):
    if start < end:
        mid = (start + end)/2
        mergeSort(A, start, mid)
        mergeSort(A, mid+1, end)
        merge(A,start, mid, end)
def merge(A, start, mid, end):
    L = A[start : mid+1]
    R = A[mid+1 : end + 1]
    i = 0
    j = 0
    k = start
    while(k<=end and i < len(L) and j < len(R)):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
    while(i<len(L)):
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while(j<len(R)):
        A[k] = R[j]
        j = j + 1
        k = k + 1

A = [1,5,8,3,2,5,6]
mergeSort(A, 0, len(A)-1)
print A
        
        
