def selection_sort(arr):
    size = len(arr)

    for i in range (size - 1):
        min = i 
        for j in range (min + 1, size):
            if arr[j] < arr[min]:
                min = j
               
        
        if i != min:
         arr[i], arr[min] = arr[min], arr[i] 



if __name__ == "__main__":
    elements = [78, 12, 15, 8, 2,61, 53, 23,27]
    selection_sort(elements)
    print(elements)