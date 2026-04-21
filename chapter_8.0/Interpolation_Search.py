class InterpolationSearch:
    def interpolation_search(array, value):
        """
        Performs an interpolation search in the the array for the given value
        
        Parameters:
        - array: The array where to perform the search
        - value: The value being searched
        
        Returns: The index of the value if it is found.
                Or None if it is not found.
        """
        start = 0
        end = len(array) - 1
        
        # While there are still elements to be searched, perform the search
        while start <= end and value >= array[start] and value <= array[end]:
            # Calculate the position using interpolation formula
            midpoint = start + ((end - start) * (value - array[start])) // (array[end] - array[start])
            
            # If the value is found at pos, return its index
            if array[midpoint] == value:
                return midpoint
            
            # If the value is greater than the value at pos, move start to pos + 1
            if array[midpoint] < value:
                # move the start to the right, just after the midpoint
                start = midpoint + 1
            
            # If the value is smaller than the value at pos, move end to pos - 1
            else:
                # move the end to the left, just before the midpoint
                end = midpoint - 1
        
        return None
        