#Python program for implementation of Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    my_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", my_array)
    
    insertion_sort(my_array)
    
    print("Sorted array:", my_array)
