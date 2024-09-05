class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # создание фиктивной (dummy) ноды для возврата
        dummy = ListNode()
        # установка указателя текущей (curr) ноды на dummy
        curr = dummy
        # инициализация переменной carry для хранения "переноса" в следующий разряд
        carry = 0
        # цикл, который будет выполняться до тех пор, пока l1 или l2 содержат ноды или есть остаток от прошлого разряда (carry)
        while l1 or l2 or carry:
            # инициализация переменной sum как текущей суммы
            sum = carry
            # если l1 не равно None, то добавляем его значение в sum и перемещаемся на следующий узел
            if l1:
                sum += l1.val
                l1 = l1.next
            # если l2 не равно None, то добавляем его значение в sum и перемещаемся на следующий узел
            if l2:
                sum += l2.val
                l2 = l2.next
            # вычисляем carry для следующей итерации
            carry = sum // 10
            # создание новой ноды с результатом текущей суммы в текущем разряде
            curr.next = ListNode(sum % 10)
            # перемещаем указатель на следующую ноду
            curr = curr.next
        # возврат ноды, следующей за фиктивной нодой (dummy)
        return dummy.next

class ListNode:
    def __init__(self, val=0, next=None):
        # инициализация значения текущей ноды (val) и указателя на следующую ноду (next)
        self.val = val
        self.next = next