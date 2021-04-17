def radixsort(arr):
    temp=len(str(max(arr)))
    print(temp)
    order=1
    for i in range(temp):
        order*=10
    print(order)

arr=[84, 23, 62, 44, 16, 30, 95, 51]
radixsort(arr)
print(list(arr))  