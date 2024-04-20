def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

arr = [30, 17, 9, 9, 1, 5, 14 ,11 ,29, 2 ,21]
sorted_arr = quick_sort(arr)
print("Arreglo ordenado:")
print(sorted_arr)

