class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

##### Important about head and tail: they are only pointers to the first and last element in the list, they are not the elements themselves. So if we change head or tail, it doesn't change the elements in the list, it just changes where head and tail point to.
class SinglyLinkedList():
    def __init__(self):     # 👉 tail الفكرة القوية: بدل ما تمشي من البداية للنهاية... تروح مباشرة للنهاية باستخدام
        self._head = None   # head → أول عنصر      None → 10 → 20 → 30 → None
        self._tail = None   # tail → آخر عنصر        ↑     ↑    ↑   ↑     ↑
                            #                       head       size       tail
        self._size = 0      # size → عدد العناصر في القائمة

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        # نسوي عقدة جديدة
        new_node = ListNode(value)          # append [20 → None]

        # الحالة 1: القائمة فارغة
        if not self._tail:                  #    head → 10 → None
            # نخلي head و tail يشيرون لنفس العقدة
            self._head = new_node
            self._tail = new_node

        # الحالة 2: القائمة فيها عناصر
        else:
                                            # نخلي آخر عنصر يشير للجديد
            self._tail.next = new_node      #    head → 10.next = 20 → None 
            # نحدث tail يصير الجديد        #                           ↑
            self._tail = new_node           #                          tail = 20
            
            

        # نزيد الحجم
        self._size += 1


    def pop(self):
        # الحالة 1: إذا القائمة فارغة؟ ماكو عناصر → ماكو شي نحذفه
        if not self._head:                  
            return None
        
        #                  الحالة 2: إذا القائمة بيها عنصر واحد فقط 
        if self._head == self._tail: # head (10)   = tail (10): Remember they are Pinters to a specific value 
            value = self._head.data  #       ^        ^   
            self._head = None        # head (None) = tail (None) 
            self._tail = None
            self._size -= 1 # نحدث الحجم بعد الحذف
            return value
        
        #                          الحالة 3: إذا القائمة بيها عناصر
        current = self._head                # نبدأ من أول عنصر
        previous = None                     # نحتفظ بالعنصر اللي قبل الحالي عشان نقدر نحدثه إذا حذفنا العنصر الأخير 
        while current.next:                 # نمشي لآخر عنصر
            previous = current
            current = current.next

        # إذا كان العنصر الأخير هو العنصر الوحيد في القائمة
        if previous:
            previous.next = None         # So delete the item after the previous item
            self._tail = previous        # update the tail pointer to previous item

        # Update list's size
        self._size -= 1

        return current.data
    

    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        # Check if index is inside bounds
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        # Prepare some variables to make the necessary changes
        # The new node will be inserted between previous_node and next_node
        previous_node = None
        next_node = self._head
        # Move to the given index and update pointer variables
        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        # Create new node. It's next pointer points to next node or None
        new_node = ListNode(value, next_node)

        # If insert at front, update head
        if previous_node is None:
            self._head = new_node
        else:
            # If not, update previous node
            previous_node.next = new_node
        
        # If insert at the end, update tail
        if previous_node == self._tail:
            self._tail = new_node

        # Update list size
        self._size += 1



    def remove(self, index):
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
            self._head = self._head.next   # head (None) = next (None)
            
            if self._head is None:      # if head (None) = next (None)
                self._tail = None       # so head (None) = next (None) = tail (None)
                
            self._size -= 1
            return value
    
                                        
        current = self._head                # الحالة 3: إذا القائمة بيها عناصر
        previous = None                     # نبدأ من أول عنصر
        for _ in range(index):              
            previous = current
            current = current.next
                                            # إذا كان العنصر الأخير هو العنصر الوحيد في القائمة
        previous.next = current.next        # previous → current → next  # So delete the item after the previous item
        

        if current == self._tail:           # If we are deleting the tail, update the tail pointer to previous item
            self._tail = previous
        
        # Update list's size
        self._size -= 1

        return current.data

    


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    print("Singly Linked List Testing append: ")

    linked_list.append(10)                      # [head | data: 10 | next: None]
    linked_list.append(20)                      # [head | data: 10 | next: data: 20 | next: None]
    linked_list.append(30)                      # [head | data: 10 | next: data: 20 | next: data: 30 | next: None]

    print(linked_list)           


    print("Singly Linked List Testing pop: ")   # <SinglyLinkedList: [10, 20, 30]>

    print(linked_list.pop())                    # Output: 30
    print(linked_list)                          # Output: <SinglyLinkedList: [10, 20]>

    print(linked_list.pop())                    # Output: 20
    print(linked_list)                          # Output: <SinglyLinkedList: [10]>

    print(linked_list.pop())                    # Output: 10
    print(linked_list)                          # Output: <SinglyLinkedList: []>
