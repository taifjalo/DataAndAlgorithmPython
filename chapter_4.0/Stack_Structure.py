class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):

        new_node = Node(data, self._top)   # اربط الجديد بالقديم اولا
        self._top = new_node               # خليه يكون الجديد هو الأعلى
        self._size += 1                    # زيد حجم الستاك بواحد
        

    def pop(self):

        if not self._top:
            return None

        value = self._top.data        # خزن القيمة
        self._top = self._top.next    # حرّك الأعلى إلى التالي

        self._size -= 1

        return value

    def __repr__(self):

        values = []
        current = self._top
    
        while current:
            values.append(str(current.data))  # نحولها نص بدون quotes
            current = current.next
    
        plural = '' if self._size == 1 else 's'
    
        return f'<Stack ({self._size} element{plural}): [{", ".join(values)}]>'
    



#   Write function to check the brackets balance
#   You have to write a function named "check_balance" that checks whether a string with different kind of 
#   bracket symbols is balanced or not using stack. The stack class is already available with the name "Stack"
#   The function "check_balance" accepts a string and it will check if the different sets of brackets symbols 
#   in the text are balanced, i.e. every kind of open bracket symbol is closed with the same kind of bracket 
#   symbol ('()', '[]' or '{}'). If everything checks, the function should return the text "Ok - C", 
#   being C the number of pairs found. If not, it should return the text: "Match error at position X", 
#   being X the position of the character relative to the beginning of the text.

#   Notice that texts should be exactly like shown and with the same capitalization.

#   The idea is simple, when you encounter an opening bracket symbol (`(` or a `{` or a `[`) you will push it to the stack. 
#   When you encounter a closing bracket symbol (`)` or a `}` or a `]`), pop the one in the stack and check if they match. 
#   If they don't match, you can return the error. If you get to the end of text without errors, return the "Ok" text as told before.

#   Some cases you want to take into account are when you encounter a closing bracket symbol before any opening one, 
#   and when the text leaves an unmatched opening bracket symbol.

#   Esimerkiksi:
#   Syöte	        Tulos
#   a(b)c[d]e{f}g   Ok - 3

    
def check_balance(text):
    stack = Stack()
    pairs = 0
    opening_brackets = '([{'
    closing_brackets = ')]}'
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for index, char in enumerate(text):
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if len(stack) == 0:                 # لا يوجد شيء في الستاك يعني لا يوجد فتح لهذا الإغلاق
                return f'Match error at position {index}'
            
            # إذا كان هناك شيء في الستاك، خذ آخر فتح وتحقق إذا كان يتطابق مع نوع الإغلاق الحالي
            top = stack.pop()                               # خذ آخر فتح من الستاك
            if top != bracket_map[char]:                    # إذا لم يتطابق مع نوع الإغلاق الحالي
                return f'Match error at position {index}'   # ارجع خطأ في الموقع الحالي
            pairs += 1                                      # إذا تطابق، زيد عدد الأزواج المتطابقة

    if len(stack) > 0:                                       # إذا كان هناك شيء في الستاك بعد الانتهاء من النص، يعني أن هناك فتحات لم يتم إغلاقها
        return f'Match error at position {len(text) - 1}'    # ارجع خطأ في نهاية النص لأن هناك فتحات لم يتم إغلاقها

    return f'Ok - {pairs}'
    
if __name__ == "__main__":
        stack = Stack()
        print(stack)  # <Stack (0 elements): []>
    
        stack.push(10)
        print(stack)  # <Stack (1 element): [10]>
    
        stack.push(20)
        print(stack)  # <Stack (2 elements): [20, 10]>
    
        print(stack.peek())  # 20
    
        print(stack.pop())   # 20
        print(stack)         # <Stack (1 element): [10]>
    
        print(stack.pop())   # 10
        print(stack)         # <Stack (0 elements): []>
    
        print(stack.pop())   # None

        print(check_balance("a(b)c[d]e{f}g"))  # Ok - 3
        print(check_balance("a(b]c"))  # Match error at position 3
        print(check_balance("a(b)c]"))  # Match error at position 6
        print(check_balance("a(b)c[d]e{f}g)"))  # Match error at position 14
        print(check_balance("a(b)c[d]e{f}g{"))  # Match error at position 14
