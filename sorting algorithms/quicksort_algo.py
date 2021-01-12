import sys
from itertools import chain
from bubble_sort_algo import *
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    less, great = [] , []
    ind = random.randint(0,len(arr) -1)
    piv = arr[ind]
    arr.remove(arr[ind])
    for i in range(len(arr)):
        if arr[i] > piv:
            great.append(arr[i])
        else:
            less.append(arr[i])
    
    return quick_sort(less) + [piv] + quick_sort(great) 


li = rand_list(1, 10)

print(quick_sort(li))

