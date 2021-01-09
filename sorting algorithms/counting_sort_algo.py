# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:33:56 2021

@author: Admin
"""

from bubble_sort_algo import rand_list


def counting_sort (arr):
    # assuming the range is known 
    small = arr[0]
    big = arr[0]
    for i in range (len(arr)):
        if (arr[i] > big):
            big = arr[i]
        if (arr[i] < small):
            small = arr[i]
    mod = lambda x,mn : x - mn
    arr1 = [mod(i,small) for i in arr]
    li = [0 for i in range(small,big+ 1)]
    for i in range (len(arr1)):
        li[arr1[i]] += 1
    for i in range (1,len(li)):
        li[i] += li[i -1]
    fin = [0 for i in range(len(arr1))]
    for i in range (len(arr1)):
        fin[li[arr1[i]] - 1] = arr[i]
        li[arr1[i]] -= 1
        
        
    return fin
        
        
        
        
lis = rand_list(50,65) + rand_list(20, 30)

print(lis)
print(counting_sort(lis))









