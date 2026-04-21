
class LinearSearch:
    def linear_unsorted_search(array, value):
        # Iterate array
        for index in range(len(array)):
        # If value is found, return its index
            if array[index] == value:
                return index
            return None
        
    def linear_sorted_search(array, value):
        # Iterate array
        for index in range(len(array)):
            # If value is found, return its index
            if array[index] == value:
                return index
            # If current value is greater than the value we are looking for, then it is not found in the array
            elif array[index] > value:
                return None
        return None