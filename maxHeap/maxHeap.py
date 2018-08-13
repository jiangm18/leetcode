def maxHeapify(A, i, heapSize):
    l = left(i)
    r = right(i)
    if l < heapSize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeapify(A,largest,heapSize)

def buildMaxHeap(A):
    heapSize = len(A)
    i = (len(A)-1)/2
    while(i>=0):
        maxHeapify(A, i, heapSize)
        i = i - 1
def heapSort(A):
    heapSize = len(A)
    buildMaxHeap(A)
    i = len(A)-1
    while(i>=1):
        A[0],A[i] = A[i],A[0]
        heapSize = heapSize - 1
        maxHeapify(A,0,heapSize)
        i = i - 1
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)/2
A = [1,3,5,2,4,6,8,9]
heapSort(A)
print A
