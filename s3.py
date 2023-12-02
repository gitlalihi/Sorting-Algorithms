#Python program for implementation of Selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    
    my_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", my_array)
    
    
    selection_sort(my_array)
    
    print("Sorted array:", my_array)
