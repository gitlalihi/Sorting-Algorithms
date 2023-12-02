#Python program for implementation of Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    my_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", my_array)
    bubble_sort(my_array)
    print("Sorted array:", my_array)
