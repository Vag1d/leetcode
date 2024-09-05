class Solution:    
 # метод twoSum принимает на вход список nums и целевое значение target
    # и возвращает список из двух индексов чисел в nums, сумма которых равна target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # словарь для хранения уже просмотренных чисел
        seen = {} 
  # проходимся по всем числам в списке nums с индексами
        for i, num in enumerate(nums): 
   # вычисляем "комплемент" - значение, которое должно быть в списке, чтобы получить target
            complement = target - num 
   # если комплемент уже был просмотрен, то нашли нужные индексы чисел
            if complement in seen: 
                return [seen[complement], i]
    # сохраняем текущее число и его индекс в словарь seen
            seen[num] = i 
  # если не найдено нужных индексов, возвращаем None
        return None 