def partition(arr, start, end):
    pivot = start
    print("Pivot: ")
    print(pivot)
    for i in range(start+1, end+1):
        if arr[i] <= arr[start]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[start] = arr[start], arr[pivot]
    return pivot

def qSort(arr, start=0, end=None): #null=none
    if end is None:
        end = len(arr) -1
    if start >= end:
        return
    pivot = partition(arr, start, end)
    print("Pivot: ")
    print(pivot)
    print(arr)
    qSort(arr, start, pivot-1) #all from the start to before the pivot
    print(arr)
    qSort(arr, pivot+1, end)   #all from right after the pivot to the end
    print(arr)

#main
arr = [123,456,23,6,13,7,3576,1235,7,234,0]
qSort(arr)
print(arr)
