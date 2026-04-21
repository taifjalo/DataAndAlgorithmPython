class BinarySearch:
    def binary_search_recursive(self, array, value, start=None, end=None):
        # Prepare the variables this way, so the user can call
        # the function with just the array and value to be searched.
        # If start and none are not defined, the search is conducted
        # in the whole array.
        if start is None:
            start = 0
        if end is None:
            end = len(array) - 1
        
        # Calculate the midpoint
        midpoint = start + (end - start + 1) // 2
        
        # If the value if found in the midpoint, return its index
        if array[midpoint] == value:
            return midpoint
        
        # if the value being searched is smaller than the one in the midpoint
        # and there is at least one element left to the midpoint
        if value < array[midpoint] and midpoint >= start+1:
            # Perform the search on the left half
            return self.binary_search_recursive(array, value, start=start, end=midpoint-1)
        
        # if the value being searched is bigger than the one in the midpoint
        # and there is at least one element right to the midpoint
        if value > array[midpoint] and midpoint <= end-1:
            # Perform the search on the right half
            return self.binary_search_recursive(array, value, start=midpoint+1, end=end)
        
        return None
    

    def binary_search_iterative(self, array, value):
        """
        Performs a binary search in the the array for the given value
        
        Parameters:
        - array: The array where to perform the search
        - value: The value being searched
        
        Returns: The index of the value if it is found.
                Or None if it is not found.
        """
        start = 0
        end = len(array) - 1
        
        # While there are still elements to be searched, perform the search
        while start <= end:
            # Calculate the midpoint
            midpoint = start + (end - start + 1) // 2 

            # If the value if found in the midpoint, return its index
            if array[midpoint] == value:
                return midpoint
            
            # if the value being searched is smaller than the one in the midpoint
            if value < array[midpoint]:
                # move the end to the left, just before the midpoint
                end = midpoint - 1  
    
            # if the value being searched is bigger than the one in the midpoint
            else:
                # move the start to the right, just after the midpoint
                start = midpoint + 1
        
        # Value has not been found
        return None
    