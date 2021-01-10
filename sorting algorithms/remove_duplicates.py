
from bubble_sort_algo import rand_list, rec_bubble_sort


def rm_dup (arr):
    
# gets a sorted list and returns it without duplicates
    c = 0
    i = 0
    while i + c < len(arr):
        arr[i] = arr[i +c]
        try:
            while (arr[i] == arr[i + c + 1]):
                c += 1
        except:
            break
        i += 1
    return arr[: len(arr) -c]




li = rand_list(1, 6) + rand_list(1, 15) + rand_list(4, 17)
li = rec_bubble_sort(li)
print(li)
print(rm_dup(li))

