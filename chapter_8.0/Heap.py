class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0



    ### def _float(self) is a helper method to maintain the heap property after adding a new element to the end of the heap. It compares the newly added element with its parent and swaps them if the new element is smaller (for a min-heap). This process continues until the new element is in the correct position, ensuring that the heap property is maintained throughout the structure.

    #    Original Heap
    #          3                      -->                    3
    #        /   \                                         /   \
    #       6     5                                       6     5
    #      / \   / \                                     / \   / \
    #     9   7 8   _(add here new item = 2)            9   7 8   2
         
    #    self._heap = [3, 6, 5, 9, 7, 8]         --> [3, 6, 5, 9, 7, 8, 2] -->
    
    #          3                      -->                    2
    #        /   \                                         /   \
    #       6     2                                       6     3
    #      / \   / \                                     / \   / \
    #     9   7 8   5                                   9   7 8   5
    #    self._heap = [3, 6, 2, 9, 7, 8, 5]      -->  [2, 6, 3, 9, 7, 8, 5]

        
        def _float(self):

            # Start at the end of the heap 
            index = self._size - 1              # من اخر عنصر بالشجره نبدأ من اخر تحت

            # Calculate index of parent element
            parent_index = (index-1) // 2       # من اخر عنصر بالشجره نبدأ من اخر تحت ونحسب ابوه وين موجود في الشجره

            # While not at Root node and value less than its parent
            while index > 0 and self._heap[index] < self._heap[parent_index]:

                # swap value with its parent
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]

                # Update indices
                index = parent_index
                parent_index = (index-1) // 2

        def insert(self, value):
            # Add the value to the heap
            self._heap.append(value)
            # Update size of the heap
            self._size += 1
            # And float the last element of the heap
            self._float()

        def _sink(self):

            index = 0  #    من اول عنصر بالشجره نبدأ من فوق
        
            while True:
        
                left = 2 * index  + 1           #   من اول عنصر بالشجره نبدأ من فوق ونحسب اول ابن له وين موجود في الشجره
                right = 2 * index  + 2          #   من اول عنصر بالشجره نبدأ من فوق ونحسب ثاني ابن له وين موجود في الشجره
        
                smallest = index                #  من اول عنصر بالشجره نبدأ من فوق ونفترض ان هو اصغر عنصر في الشجره
        
                if left < self._size and self._heap[left] < self._heap[smallest]:                           #  من اول عنصر بالشجره نبدأ من فوق ونحسب اول ابن له وين موجود في الشجره ونقارن بينه وبين الاب ونشوف اذا هو اصغر منه ولا لا 
                    smallest = left
        
                if right < self._size and self._heap[right] < self._heap[smallest]:                         #  ن من اول عنصر بالشجره نبدأ من فوق ونحسب ثاني ابن له وين موجود في الشجره ونقارن بينه وبين الاب ونشوف اذا هو اصغر منه ولا لا 
                    smallest = right
        
                if smallest != index :                                                                      # نقارن بين الاب والابناء ونشوف اذا هو اصغر منهم ولا لا اذا كان هو اصغر منهم يبقى مكانه في الشجره اذا كان هو اكبر منهم نبدل بينهم
                    # swap
                    self._heap[index ], self._heap[smallest] = self._heap[smallest], self._heap[index ]     # من اول عنصر بالشجره نبدأ من فوق ونفترض ان هو اصغر عنصر في الشجره ونقارن بينه وبين اول ابن له وثاني ابن له ونشوف اذا هو اصغر منهم ولا لا ونبدل بينهم اذا كان هو اكبر منهم
                    index  = smallest
                else:
                    break







                
