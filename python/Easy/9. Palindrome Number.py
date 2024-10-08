class Solution(object):
    def isPalindrome(self, x):
        # Проверяем исключительные случаи:
        # Если число меньше 0 или оканчивается на 0 (кроме нуля),
        # то оно не может быть палиндромом.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        original_x = x
        
        # Пока исходное число x больше 0, выполняем следующие действия:
        # - Получаем последнюю цифру числа x с помощью операции взятия остатка от деления на 10
        #   и добавляем ее в конец числа reversed_num.
        # - Уменьшаем исходное число x на один разряд путем целочисленного деления на 10.
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Сравнение исходного числа x с перевернутым числом reversed_num.
        return original_x == reversed_num