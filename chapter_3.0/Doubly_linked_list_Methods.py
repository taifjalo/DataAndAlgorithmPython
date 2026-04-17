class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data # The content of the node
        self.next = next # Pointer to the next node
        self.prev = prev # Pointer to the previous node

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self._head = None # Pointer to the first node
        self._tail = None # Pointer to the last node
        self._size = 0     # Number of nodes in the list

    def __repr__(self):

        values = []
        current = self._top
    
        while current:
            values.append(str(current.data))  # نحولها نص بدون quotes
            current = current.next
    
        plural = '' if self._size == 1 else 's'
    
        return f'<Stack ({self._size} element{plural}): [{", ".join(values)}]>'
    
    
    def __len__(self):
        return self._size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration
            
    def __getitem__(self, index):
        """
        Return value at index
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        
        # Return the value
        return current_node.data

    def __setitem__(self, index, value):
        """
        set value at index k with val
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # Set the value
        current_node.data = value

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value. This is the last node, so next is None,
        # but there can be already some node in the list, hence the prev value
        new_node = ListNode(value, next=None, prev=self._tail) # The prev pointer of the new node points to the item which is after it (the current tail)

        # If list is empty, update head and tail pointers
        if self._head is None:
            self._head = new_node
            self._tail = new_node

        else:
            # In any other case, update tail node to point to the new element
            # and update tail pointer. The new node already points to its
            # previous element
            self._tail.next = new_node
            self._tail = new_node

        # update size
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list
        
        Parameters: None
        
        Returns:
            The content of the removed node. If list is empty, returns None
        """
        # If list is empty, returns None
        if not self._size:
            return None
        
        # Locate previous_node (the node just before last node)
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._tail:
            self._head = None
        else:
            # If not, update the pointer of the previous node
            previous_node.next = None   # It is now the last node

        # Update tail pointer
        self._tail = previous_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value

    def contains(self, value):
        """
        Returns True if value if found in the list and False if not
        """
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        """
        Clear the list
        """
        # Remove all nodes
        current_node = self._head
        while current_node:
            next = current_node.next
            del(current_node)
            current_node = next

        # Update pointers and size
        self._head = self._tail = None
        self._size = 0

    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        
        #  الحالة 1: إذا القائمة فارغة؟ ماكو عناصر → نضيف العنصر في أول القائمة
        if self._size == 0:
            self.append(value) # We can use append method to add the new node in the empty list
            return
        
        # Check if index is inside bounds
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))
        
        # insert by index if the list is not empty
        # Prepare some variables to make the necessary changes
        # The new node will be inserted between previous and next
        previous = None
        next = self._head
        # Move to the given index and update pointer variables
        for _ in range(index):
            previous = next
            next = next.next

        # Create new node. It's next pointer points to next node or None
        new_node = ListNode(value, next=next, prev=previous)


        # If insert at front, update head
        if previous is None:
            self._head = new_node
        else:
            # If not, update previous node
            previous.next = new_node

        # If insert at the end, update tail
        if next is None:
            self._tail = new_node
        else:
            # If not, update next node
            next.prev = new_node

        # Update list size
        self._size += 1

        return None
    

    def remove(self, index):
        """
        Remove a new node from the position given by the index

        Parameters:
        - 'index': The position where to insert the new node

        Returns: The value of the node being removed
        """

        # الحالة 1: إذا القائمة فارغة؟ ماكو عناصر → ماكو شي نحذفه
        if not self._head:                  
            return None

        # Check if index is inside bounds 
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))
        

        #                  الحالة 2: إذا القائمة بيها عنصر واحد فقط 
        # Step 2: check if the list has only one index [0]: remove it
        if index == 0:
            value = self._head.data
            self._head = self._head.next     # head (None) = next (None)
            self._head.prev = None           # If we removed the first element, update the prev pointer of the new head to None
            if self._head is None:           # if head (None) = next (None)
                self._tail = None            # so head (None) = next (None) = tail (None)
                
            self._size -= 1
            return value
        
        #                  الحالة 3: إذا القائمة بيها أكثر من عنصر
        # Step 3: if the list has more than one element, we need to update
        # the pointers of the previous and next nodes to bypass the removed node


        return None


    def remove(self, index):

        # 1. إذا القائمة فارغة
        if self._size == 0:
            return None

        # 2. تحقق من الحدود
        if index < 0 or index >= self._size:
            raise ValueError("Index out of bounds")

        # 3. روح للمكان المطلوب
        current = self._head
        for _ in range(index):
            current = current.next

        previous = current.prev
        next_node = current.next

        # 4. حالة حذف أول عنصر (head)
        if previous is None:
            self._head = next_node
            if next_node:
                next_node.prev = None

        # 5. حالة حذف آخر عنصر (tail)
        elif next_node is None:
            self._tail = previous
            previous.next = None

        # 6. حالة حذف من النص by index
        else:
            previous.next = next_node
            next_node.prev = previous

        # 7. تحديث الحجم
        self._size -= 1

        # 8. إذا صارت القائمة فارغة بعد الحذف
        if self._size == 0:
            self._head = None
            self._tail = None

        # 9. رجّع القيمة
        return current.data
    

    
