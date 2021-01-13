
from bubble_sort_algo import rand_list
import matplotlib.pyplot as plt




def insert_sort (arr):
    arr1 = [ i for i in arr ]
        
    for i in range(1,len(arr1)):
        plt.plot([i for i in range(len(arr1))], arr1, color = 'green', linestyle = 'dashed',linewidth = 3, 
        marker='o', markerfacecolor='blue', markersize=6 )
    
        plt.show()
        
        if (arr1[i] < arr1[i -1]):
            while(arr1[i] < arr1[i -1] and i >= 1):
                arr1[i], arr1[i-1] = arr1[i -1], arr1[i]
                i -= 1
    plt.plot([i for i in range(len(arr1))], arr1, color = 'green', linestyle = 'dashed',linewidth = 3, 
        marker='o', markerfacecolor='blue', markersize=6 )
    
    plt.show()
    return arr1
                


li = rand_list(1,100)

print(insert_sort(li))
