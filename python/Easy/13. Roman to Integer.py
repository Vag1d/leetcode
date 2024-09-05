class Solution(object):
    def romanToInt(self, s: str) -> int:
        roman_number_list= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}     

        arabic_number = 0 

        for i,symbol in enumerate(roman_number):
            roman_number_list[symbol]
 
        if  i + 1 < len(roman_number) and roman_number_list[roman_number[i]] < roman_number_list[roman_number[i+1]]:
            arabic_number -=  roman_number_list[roman_number[i]] 
        else:
            arabic_number += roman_number_list[symbol]
   
        rerurn arabic_number



# for i in range(len(roman_number)):
#     if i + 1 < len(roman_number) and roman_number_list[roman_number[i]] < roman_number_list[roman_number[i + 1]]:
#         arabic_number -=  roman_number_list[roman_number[i]] 
#     else:
#         arabic_number += roman_number_list[roman_number[i]] 
   

