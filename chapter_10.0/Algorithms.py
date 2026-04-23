

### Recursion:
def factorial(n):
    # Base case
    if n == 1:
        return 1                # it will be 5 * factorial(4) --> 5 * (4 * factorial(3)) --> 5 * (4 * (3 * factorial(2))) --> 5 * (4 * (3 * (2 * factorial(1)))) --> 5 * (4 * (3 * (2 * 1))) = 120
    print(n)                    # To show the recursive calls

    # Common case
    return n * factorial(n-1)   # it will be n * (n-1) * (n-2) * ... * 1




### Backtracking: "جرّب كل الطرق + ارجع إذا غلط"
def backtrack(n):

    if n == 3:
        print("وصلنا 🎉")
        return True

    if n > 3:
        return False

    # جرّب
    if backtrack(n + 1):
        return True

    # رجوع (backtrack)
    return False


### Greedy: "خذ أفضل خيار في كل خطوة"
coins = [5, 2, 1]

def greedy(amount):

    result = []

    for coin in coins:          # تكرار على كل العملة
        while amount >= coin:   # إذا المبلغ أكبر أو يساوي العملة
            amount = amount - coin      # نخصم العملة من المبلغ
                #        18 - 5 = 13 
                #        13 - 5 = 8
                #         8 - 5 = 3
                #         3 - 2 = 1
                #         1 - 1 = 0
            result.append(coin)         # نضيف العملة إلى النتيجة

    return result

'''
    Divide & Conquer and Dynamic Programming
    بس شنو الفرق ؟

    👇هنا النقطة المهمة جدًا 

    🟦 Divide & Conquer

    👉 تقسم المشكلة
    👉 كل جزء ينحل لوحده
    👉 ما نهتم إذا تكرر الحل (Worse Time Complexity)


    🟩 Dynamic Programming

    👉 نفس الشي… بس أذكى

    💡 إذا حلّيت مشكلة صغيرة مرة
    👉 لا تعيد حلها مرة ثانية
    👉 خزن الجواب واستخدمه (Time Complexity أفضل بكثير)
    ------------------------------------------------------

    - Dynamic Programming has two types:

    1. Memoization (فوق لتحت ⬆️⬇️)
    👉 تبدأ من المشكلة الكبيرة
    👉 كل مرة تخزن النتائج

    مثل:
    تسأل سؤال
    تخزنه
    إذا رجع نفس السؤال → تستخدمه


    2. Tabulation (تحت لفوك ⬇️⬆️)
    👉 نبدأ من الصغير
    👉 نبني للأكبر تدريجيًا
    '''



def fib(n):

    if n < 2:                           # if 0, 1 
        return 1                        # 1

    a = 1
    b = 1

    for index in range(2, n + 1):       # 2, 3, 4, 5, 6, 7, 8, 9, 10

        new = a + b                     # 1 + 1 = 2
                                        # 1 + 2 = 3
                                        # 2 + 3 = 5
                                        # 3 + 5 = 8
                                        # 5 + 8 = 13
                                        # 8 + 13 = 21
                                        # 13 + 21 = 34
                                        # 21 + 34 = 55
                                        # 34 + 55 = 89

        # update a and b for the next iteration
        a = b                           # 1
        b = new                         # 2

    return b                            # 55
    
if __name__ == "__main__":

    print(factorial(5))  # Output: 120
    print(backtrack(0))  # Output: وصلنا 🎉
    print(greedy(18))    # Output: [5, 5, 5, 2, 1]
    
    print(fib(10))       # Output: 89

