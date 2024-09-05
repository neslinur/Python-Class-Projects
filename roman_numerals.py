# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya
# Section: 403
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date: 01 11 2023

def is_empty(s):
    return len(s) == 0

def from_roman(roman_numeral):
    '''
    In the Roman numeral system, the symbols I, V, X, L, C, D, and M stand
    respectively for 1, 5, 10, 50, 100, 500, and 1,000 in the Hindu-Arabic
    numeral system.
    A symbol placed after another of equal or greater value
    adds its value.
    A symbol placed before one of greater value subtracts its
    value.
    '''
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
   
    if is_empty(roman_numeral):
        return 0
       
    if len(roman_numeral) == 1:
        return symbols[roman_numeral[0]]
   
    symbol = roman_numeral[-1]
    decimal_value = symbols[symbol]
    previous_symbol = symbol
    for i in range(1, len(roman_numeral)):
        if symbols[roman_numeral[-1 - i]] >= symbols[previous_symbol]:
            decimal_value += symbols[roman_numeral[-1 - i]]
        else:
            decimal_value -= symbols[roman_numeral[-1 - i]]
        symbols[previous_symbol]
        previous_symbol = roman_numeral[-1 - i]
   
    return decimal_value

def compare_roman_numerals(roman_numeral_1, roman_numeral_2):
    a = from_roman(roman_numeral_1)
    b = from_roman(roman_numeral_2)
    if a < b:
        return -1
    if a == b:
        return 0
    return 1
   
def main():
    num1 = input("Enter the first Roman numeral: ")
    num2 = input("Enter the second Roman numeral: ")
    result = compare_roman_numerals(num1, num2)
    if result == -1:
        compare = 'smaller than'
    elif result == 0:
        compare = 'equal to'
    else:
        compare = 'larger than'
    print(f'{num1} is {compare} {num2}')
   
if __name__ == '__main__':
    main()