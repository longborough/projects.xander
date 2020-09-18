#!python
# ----------------------------------------------------
# Bubble sort (improved) -- 
# ----------------------------------------------------
numbers = [9, 5, 4, 15, 3, 8, 11] 
numItems = len(numbers)         # get number of items in the array 
flag = True                     # indicates when a swap is made
i = 0                           # pass counter 
while i < (numItems - 1) and (flag == True): 
    print(f'Start pass {i}: {numbers}')
    flag = False 
#   for j = 0 to (numItems - 2) - i: 
    for j in range(numItems - i - 1): 
        if numbers[j] > numbers[j + 1]:   # Compare these two items
                                          # Swap if required 
            print(f'Swapping {j} -> {numbers[j]} with {j+1} -> {numbers[j+1]}')
            temp = numbers[j] 
            numbers[j] = numbers[j + 1] 
            numbers[j + 1] = temp 
            flag = True                   # Mark that we have swapped 
        # endif 
    # next j 
    print(f'End pass {i}: {numbers} -- Swapped {flag}')
    i = i + 1 
# endwhile 
print(f'Total passes: {i-1} out of {numItems - 1}')
