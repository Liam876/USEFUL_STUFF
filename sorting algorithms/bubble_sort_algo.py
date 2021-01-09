# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:35:18 2021

@author: Liam B.
"""
import random
import matplotlib.pyplot as plt


def rand_list (minval,maxval):
    a = []
    b = [i for i in range (minval,maxval + 1)]
    for i in range (len(b)):
        c = random.randint(0,len(b) -1)
        a.append(b[c])
        b.remove(b[c])
    return a


def rec_bubble_sort(a, ind = 0):
    if ind == len(a) - 1:
        return a
    for i in range(len(a) -1):
      if a[i] > a[i+ 1]:
          a[i],a[i+1] = a[i+ 1],a[i]
    return rec_bubble_sort(a,ind + 1)



def bubble_sort (brr):
    arr = coppy_arr(brr)
    for i in range(len(arr)):
        plt.plot([i for i in range(len(arr))], arr, color = 'green', linestyle = 'dashed',linewidth = 3, 
        marker='o', markerfacecolor='blue', markersize=9 )
    
        plt.show()
        swapped1 = False
        for j in range (len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j] ,arr[j + 1] = arr[j + 1], arr[j]
                swapped1= True
                
        if not swapped1:
            c = i
            break
        
    return [arr, "efficiency : " + str((len(arr) -1  - c)/(len(arr) - 1) * 100) + "%"]
      

  
def rev_bubble_sort (b):
    a = coppy_arr(b)
    for j in range (len(a)): 
        plt.plot([i for i in range(len(a))], a, color = 'green', linestyle = 'dashed',linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=9 )
    
        plt.show()
        swapped = False
        for i in range (len(a) - 1, 0, -1):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i -1], a[i]
                swapped = True

        if not swapped:
            c1 = j
            break
        
    return [a , "efficiency :  " + str((len(a) - 1 - c1)/(len(a) - 1) * 100) + "%"]



def coppy_arr (ar):
    return [ar[i] for i in range(len(ar)) ]


""" 
 ---MAIN---

li = rand_list(1,10)
print(li)
#print(rec_bubble_sort(li))
print(bubble_sort(li))
print(rev_bubble_sort(li))
"""
