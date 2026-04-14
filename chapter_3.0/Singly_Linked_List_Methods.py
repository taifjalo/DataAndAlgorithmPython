class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'


##### Important about head: it is only pointer to the first element in the list, it is not the element itself. So if we change head, it doesn't change the element in the list, it just changes where head point to.
class SinglyLinkedList():
    def __init__(self):
        self._head = None   #  top → رأس القائمة يشير لأول عنصر في القائمة
                            #  [head] → None
    
    
    def __repr__(self):     # "امشي بالعناصر وحدة وحدة "اطبعها
        current_node = self._head
        values = ''
        while current_node:                                     # طالما في عنصر في القائمة
            values += f', {current_node.data}'                  # نضيف القيمة للستركتشر اللي بنطبعه
            current_node = current_node.next                    # ننتقل للعنصر اللي بعده
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'   # نطبع الستركتشر اللي بنطبعه بدون الفاصلة الأولى
     
    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append: node = ListNode([40 → None])

        Returns: None
        """
        # Step 1: Create the node with the: node = ListNode([40 → None])
        node = ListNode(value, next=None) 

        # Step 2: If list is empty just point the header to the new node
        # الحالة 2: القائمة فارغة يعني إذا ماكو عناصر → خليه أول عنصر في القائمة و خليه يشير له
        if not self._head:              
            self._head = node   
            # قبل: head → None
            #             ^   آخر عنصر 
            # بعد: head → [40 → None]


        # Step 3: If list is not empty, search for the last element and point it to the new node
        # الخطوة 3: إذا القائمة مو فارغة
        else:
            current_node = self._head               # نبدأ من أول عنصر

            while current_node.next != None:        # Step 4: الخطوة 4: نمشي لآخر عنصر
                current_node = current_node.next
                
            # Step 5: Connect the last element to the new node (None) اربط آخر عنصر بالجديد 
            current_node.next = node
            # Before: 10 → None
            #               ^   آخر عنصر 
            # After:  10 → [20 → None]


            # Before: 10 → 20 → None
            #                   ^   آخر عنصر 
            # After:  10 → 20 → [30 → None]


            # Before: 10 → 20 → 30 → None
            #                        ^   آخر عنصر 
            # After:  10 → 20 → 30 → [40 → None]



    def pop(self):

        if not self._head:                       # الحالة 1: إذا القائمة فارغة؟ ماكو عناصر → ماكو شي نحذفه
            return None
            
        else: 
            current = self._head            # current_node  → يمشي داخل القائمة
            previous = None                 # previous_node → يبقى وراه (يتبعه)
            
                                                 # 🎮 تخيل الحركة
                                                 #  None   10 → 20 → 30  None
                                                 #   ^      ^
                                                 #   prev   current

            while current.next != None:     # _head.next != None → طالما في عنصر بعده
                previous = current
                current = current.next

        # if current_node(previous_node).next == None, update previous node
        if previous:                        # ⚠️ الحالة العادية يعني أكثر من عنصر في القائمة → نحذف العنصر الأخير ونخلي العنصر اللي قبله يشير إلى لا شيء  
            previous.next = None            #   None   10 → 20 → None   :قطعنا 30 من القائمة
                                                 #                ^     ^
                                                 #               prev  current


        else:                                    # ⚠️ الحالة الخاصة (مهمة جدًا) يعني عنصر واحد فقط في القائمة → نحذف هذا العنصر ونخلي الرأس يشير إلى لا شيء
            self._head = None
        return current.data # head → None 




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

    