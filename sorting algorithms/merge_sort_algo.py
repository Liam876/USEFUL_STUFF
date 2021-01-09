
from bubble_sort_algo import rand_list



def merge_sort (arr):
    mid = len(arr) // 2
    if mid < 1:
        return arr[0] 
    left = arr[: mid]
    right = arr[mid: ]
    merge_sort(left)
    merge_sort(right)
    i = 0
    k = 0
    while k + i  < len(arr):
        if (i != len(right) and( k == len(left) or right[i] < left[k])  ):
            arr[i + k] = right[i]
            i += 1
        else:
            arr[i + k] = left[k]
            k += 1
    return arr


a = rand_list(1, 69)
print(merge_sort(a))        
        
        


