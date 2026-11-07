n = [32,12,27,45]
elements = len(n)
print("BEFORE SORT",n)
def mergesort(n,low,mid,high):
    o = []
    start1 = low
    start2 = mid + 1 
    while start1 <= mid and start2 <= high:
        if n[start1] < n [start2]:
            o.append (n[start1])
            start1 += 1 
        else:
            o.append(n[start2])
            start2 += 1 
    while start1 <= mid:
        o.append (n[start1])
        start1 += 1 
    while start2 <= high:
        o.append(n[start2])
        start2 += 1 

    k= 0 
    for i in range (low,high+1):
        n[i] = o[k]
        k += 1 

def merge(n,low,high):
    if low<high:
        mid = (low+high)//2
        merge(n,low,mid)
        merge(n,mid+1,high)
        mergesort(n,low,mid,high)

merge(n,0,elements-1)
print("AFTER SORT ",n)