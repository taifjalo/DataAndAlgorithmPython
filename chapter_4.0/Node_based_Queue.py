class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'

class Queue():

    # الخطوة 1: إنشاء الطابور                 #  front → A → B → C ← rear
    def __init__(self):
        self._front = None                      # أول واحد بالطابور (ينحذف)
        self._rear = None                       # آخر واحد بالطابور (نضيف عنده)
        self._size = 0                          # عدد العناصر

    # الخطوة 2: طباعة الطابور
    def __repr__(self):

        values = []                             # 📦 صندوق نخزن بيه القيم
        current = self._front                   # 🚶 نبدأ من أول واحد

        # امشي على كل العناصر
        while current:
            values.append(str(current.data))   # خزن القيمة
            current = current.next             # روح للي بعده

        values.reverse()                       # اقلب الترتيب (حتى الجديد يصير على اليسار)

        # ترتيب كلمة element / elements
        plural = '' if self._size == 1 else 's'

        # اطبع الشكل النهائي
        return f'<Queue ({self._size} element{plural}): [{", ".join(values)}]>'
    


    # الخطوة 3: الإضافة (enqueue)
    def enqueue(self, data):
        new_node = Node(data)                       # سوِ عنصر جديد

        # الحالة 1: الطابور فارغ                   # front → None ← rear
        if self._rear is None:
            self._front = self._rear = new_node     # خليه أول وآخر عنصر

        # الحالة 2: الطابور بيه عناصر             # front → A → B ← rear --> enqueue(C): front → A → B → C.                     اربط آخر عنصر بالجديد
        else:                                       # then make the rear pointer point to added item: front → A → B → C ← rear    خلي الجديد يصير الأخير

            self._rear.next = new_node              # اربط آخر عنصر بالجديد     B → C
            self._rear = new_node                   # خلي الجديد يصير الأخير     B → C ← rear 

        self._size += 1                             # زيد العدد

        # الخطوة 4: الحذف (dequeue)
    def dequeue(self):

        # إذا الطابور فارغ
        if self._front is None:
            return None                         # ماكو شي نحذفه

        value = self._front.data                # خزن قيمة أول عنصر     
        self._front = self._front.next          # خلي الثاني يصير الأول

        # إذا الطابور صار فارغ بعد الحذف
        if self._front is None:
            self._rear = None                   # نظف المؤشر

        self._size -= 1                         # نقص العدد

        return value                            # رجّع القيمة



# Implement a function to make pairs of even-odd numbers
# You have to implement a function called get_pairs that given a list of numbers, makes pairs with them. Each pair consists 
# in one even number and one odd number. The function will return a list containing all pairs as tuples. You have to implement the 
# function using queues. A Queue class, that offers enqueue and dequeue methods, is already available for you to use.

# The function will accept as parameter a (Python) list of integer numbers. The function will return a (Python) list containing tuples. 
# Each tuple is a pair of even-odd numbers (first the even, then the odd number). The pairs have to be formed 
# in order: the first available even number with the first available odd number.

# To implement this function create two queues and traverse the numbers list. For each number, check is it an even number or an odd number, 
#  and check if there is a pair available in the appropriate queue. If there is, save the pair for the output. If not, enqueue it.

def get_pairs(numbers):
    even_queue = Queue()  # طابور للأعداد الزوجية
    odd_queue = Queue()   # طابور للأعداد الفردية
    pairs = []           # قائمة لتخزين الأزواج

    for num in numbers:
        if num % 2 == 0:  # إذا العدد زوجي
            if not odd_queue._size == 0:  # إذا في عدد فردي متاح
                odd_num = odd_queue.dequeue()  # خذ أول عدد فردي
                pairs.append((num, odd_num))  # خزن الزوج (زوجي، فردي)
            else:
                even_queue.enqueue(num)  # إذا ما في عدد فردي، خزن العدد الزوجي في الطابور
        else:  # إذا العدد فردي
            if not even_queue._size == 0:  # إذا في عدد زوجي متاح
                even_num = even_queue.dequeue()  # خذ أول عدد زوجي
                pairs.append((even_num, num))  # خزن الزوج (زوجي، فردي)
            else:
                odd_queue.enqueue(num)  # إذا ما في عدد زوجي، خزن العدد الفردي في الطابور

    return pairs  # رجّع قائمة الأزواج
    

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue('A')      # يضيف 'A' للطابور
    queue.enqueue('B')      # يضيف 'B' للطابور
    queue.enqueue('C')      # يضيف 'C' للطابور
    print(queue)            # <Queue (3 elements): [C, B, A]>   

    queue.dequeue()         # يزيل 'A'
    print(queue)            # <Queue (2 elements): [C, B]>