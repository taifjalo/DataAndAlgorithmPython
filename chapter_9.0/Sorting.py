def bubble_sort(array):

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            # if the element found is greater than the next element, then swap them
            if array[j] > array[j + 1]:
                # Swap if the element found is greater than the next element 
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def insertion_sort(array):

    """
    Sort the array using the Insertion sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    
    # array = [6, 8, 5, 1, 2]
    for i in range(1, len(array)):

        key = array[i]   # it start with: take the first number in the list --> 6
        j = i - 1        #                then take the number just before the first --> 8 

            # 8 >= 0            8 > 6 ✔️ قارن --> 
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


def selection_sort(array):

    for i in range(len(array)):
        # Search for the minimum element value in the unsorted array
        minimum_index = i

        # Compare the minimum element with the next element in the array until the end of the array is reached. If the minimum element is greater than the next element, then update the minimum element.
        for j in range(i + 1, len(array)):
            # If the minimum element is greater than the next element, then update the minimum element
            if array[j] < array[minimum_index]:
                # Update minimum element if a smaller element is found
                minimum_index = j
                
        # Swap the minimum element with the first element of the unsorted array
        array[i], array[minimum_index] = array[minimum_index], array[i]

    return array

# Max-Heapify Sort Algorithm: Given an array like: [6, 2, 5, 8, 1] --> [6, 8, 5, 2, 1]
def sift_down(array, start, end):

    left = 2*start + 1        # 2 * 0 + 1 = 1 --> اليسار
    right = 2*start + 2       # 2 * 0 + 2 = 2 --> اليمين

    max = start           # نفترض أن الحالي هو الأكبر

    # إذا اليسار أكبر 
    if left <= end and array[left] > array[max]:
        max = left

    # إذا اليمين أكبر
    if right <= end and array[right] > array[max]:
        max = right

    # إذا لقينا واحد أكبر
    if max != start:
        # نبدل
        array[start], array[max] = array[max], array[start]
        
        # Recursive
        sift_down(array, max, end)

        # ننزل لهناك
        start = max


def heap_sort(array):

    # 1. بناء heap
    for i in range(len(array)//2 - 1, -1, -1):
        sift_down(array, i, len(array)-1)

    # 2. الترتيب
    for end in range(len(array)-1, 0, -1):

        # نبدل الأكبر مع الأخير
        array[0], array[end] = array[end], array[0]

        # نصلّح الباقي
        sift_down(array, 0, end-1)





if __name__ == "__main__":
    print(bubble_sort([5, 1, 4, 2, 8]))                 # Output: [1, 2, 4, 5, 8]
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))    # Output: [11, 12, 22, 25, 34, 64, 90]

    print(insertion_sort([5, 1, 4, 2, 8]))              # Output: [1, 2, 4, 5, 8]
    print(insertion_sort([12, 11, 13, 5, 6]))           # Output: [5, 6, 11, 12, 13]

    print(selection_sort([5, 1, 4, 2, 8]))              # Output: [1, 2, 4, 5, 8]
    print(selection_sort([64, 25, 12, 22, 11]))         # Output: [11, 12, 22, 25, 64]



    array = [6, 2, 5, 8, 1]          
    sift_down(array, 1, 4)
    print(array)            # Output: [6, 8, 5, 2, 1]

    heap_sort(array)
    print(array)            # Output: [1, 2, 5, 6, 8]