#!python
# ----------------------------------------------------
# A better quicksort?  
# ----------------------------------------------------

numbers = [9, 5, 4, 9, 15, 3, 8, 11] 

def partition(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        left = [x for x in list[1:] if x < pivot]
        right = [x for x in list[1:] if x >= pivot]
    return (left, pivot, right)

def qsort(list):
    if len(list) <= 1:
        print(f'QSorting: {list} => {list}')
        return list
    else:
        print(f'QSorting: {list}')
        left, pivot, right = partition(list)
        print(f'Partitions: {left} | {pivot} | {right}')
        return qsort(left) + [pivot] + qsort(right)

print(qsort(numbers))
