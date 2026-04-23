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

def quick_sort(array, left_index=None, right_index=None):
    # Set these values so the function can be called by the user with only the array as parameter
    if not left_index:
        left_index = 0
    if not right_index:
        right_index = len(array) - 1
    # The pivot selection is a problem in its own.
    # For now let's use the first element, but any other element could have been chosen (with necessary algorithm's adjustments)
    pivot_index = left_index
    # We set a border index to indicate that values less or equal than pivot are to 
    # its left (border index inclusive) and values bigger than pivot are at its right
    # Right now the only element less or equal than the pivot, is the pivot itself.
    border_index = left_index
    # And start traversing the partition
    for current in range(left_index+1, right_index+1):
        # if the value of the current position is less than pivot,
        # let's add it (current value) to the minors part
        if array[current] <= array[pivot_index]:
            # Update border as there is one minor more now.
            border_index += 1
            # Check if we actually need to do the swap. If current index was
            # the next value after minors, then no swap is necessary
            if current > border_index:
                # If that was not the case, then swap their values
                array[current], array[border_index] = array[border_index], array[current]
    # After traversing the partition, the pivot can be swapped with the last of the minors.
    # If pivot is the only  minor, then there is no need to swap.               
    if border_index != pivot_index:
        # swap
        array[border_index], array[pivot_index] = array[pivot_index], array[border_index]
        pivot_index = border_index  # Update pivot index after swap
    # The pivot is in its position and all values less or equal than pivot are at the left,
    # and all values bigger than pivot are at the right.
    # Now call recursively this function on both partitions.
    # Check if left partition has at least 2 elements
    if (pivot_index - left_index) > 1:
        quick_sort(array, left_index, pivot_index-1)
    # Check if right partition has at least 2 elements
    if (right_index - pivot_index) > 1:
        quick_sort(array, pivot_index+1, right_index)

def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: The sorted array.
    """
    # If array has only 1 element, it is sorted
    if len(array) == 1:
        return array
    # Calculate the midpoint
    midpoint = len(array) // 2
    # And call recursively on the two half arrays.
    first_half = merge_sort(array[:midpoint])
    second_half = merge_sort(array[midpoint:])
    # Merge. Initialize helper variables
    first_index = second_index = 0
    merged_array = []
    # Loop while neither index reaches the end of its half
    while first_index < len(first_half) and second_index < len(second_half):
        # Loop merges the two arrays. Two pointers go forward depending on which one is less than the other
        first_value = first_half[first_index]
        second_value = second_half[second_index]
        # The smaller of the two values get added to the merged list and the pointer of
        # the array it came from advances one position
        if first_value < second_value:
            merged_array.append(first_value)
            first_index += 1
        else:
            merged_array.append(second_value)
            second_index += 1
    # When one of the indices reaches the end of its half, loop ends
    # and the remaining of the other half get added to the merged array.
    # Function has to check which one has to add
    if first_index < len(first_half):
        merged_array.extend(first_half[first_index:])
    elif second_index < len(second_half):
        merged_array.extend(second_half[second_index:])
    # And finally, return the merged array
    return merged_array


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

    print(quick_sort([10, 7, 8, 9, 1, 5]))             # Output: [1, 5, 7, 8, 9, 10]
    print(quick_sort([64, 34, 25, 12, 22, 11, 90]))    # Output: [11, 12, 22, 25, 34, 64, 90]

    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))      # Output: [3, 9, 10, 27, 38, 43, 82] 


    array = [6, 2, 5, 8, 1]          
    sift_down(array, 1, 4)
    print(array)            # Output: [6, 8, 5, 2, 1]

    heap_sort(array)
    print(array)            # Output: [1, 2, 5, 6, 8]