# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Neslinur Kaya
# Claudia Herrera
# Jasmine Gonzales
# Soley Mendoza
# Section: 403/503
# Assignment: Lab 9 Team
# Date: 23 10 2023

#given code
def print_puzzle(puzzle):
  ''' Print puzzle as a long division problem. '''
  puzzle = puzzle.split(',')
  for i in range(len(puzzle)):
      if i == 1:
          print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
      print(f'{puzzle[i]: >16}')
      if i > 1 and i % 2 == 0:
          print(f"{'-'*len(puzzle[i]): >16}")

#neslinur - function 1
def get_valid_letters(puzzle):
  first = ''
  result = ''
  for i in puzzle:
    if i not in first:
      first += i
  for char in first:
    if char.isalpha():
      result += char

  result = result[:10]
  return result


# jasmine- function 2
def is_valid_guess(letters, guess):
  sorted_letters = ''.join(sorted(letters))
  sorted_guess = ''.join(sorted(guess))
  if sorted_guess == sorted_letters:
    return True
  return False

#function 3-claudia 
def check_user_guess(dividend, quotient, divisor, remainder):
  if dividend == (quotient * divisor + remainder):
     return True
  return False

#fuction 4 - soley
def make_number(word, guess):
  num = []
  a = 0
  for a in word:
    for i in range(len(guess)):
      if a == guess[i]:
        num.append(i)
        break
  
  num = ''.join(str(x) for x in num)
  if num == "":
      num = 0
  return int(num)
                       
#function 5 - neslinur
def make_numbers(puzzle, guess):
  dividend_ind = puzzle.index("|")+2
  count = 0
  dividend_ind2 = -1
  for i, char in enumerate(puzzle):
    if char == ",":
        count += 1
        if count == 2:
            dividend_ind2 = i
            break
  quotient_ind = puzzle.index(",")
  divisor_ind = puzzle.index(" ")
  remainder_ind = puzzle.rfind(",")
  dividend = make_number(puzzle[dividend_ind:dividend_ind2], guess)
  quotient = make_number(puzzle[:quotient_ind], guess)
  divisor = make_number(puzzle[quotient_ind+1:divisor_ind], guess)
  remainder = puzzle[remainder_ind+1:]
  if remainder[-1] == ",":
      remainder = remainder[:-1]
  remainder = make_number(remainder, guess)

  result = (dividend, quotient, divisor, remainder)
  return result
 
#function 6 - neslinur
def main():
  # The lines below demonstrate what the print_puzzle function outputs.
  puzzle = input("Enter a word arithmetic puzzle: ")
  print()
  print_puzzle(puzzle)
  print()
  guess = input("Enter your guess, for example ABCDEFGHIJ: ")
  nums = make_numbers(puzzle, guess)
  check = check_user_guess(nums[0], nums[1], nums[2], nums[3])
  letters = get_valid_letters(puzzle)
  valid = is_valid_guess(letters, guess)
  if valid is False:
    print("Your guess should contain exactly 10 unique letters used in the puzzle.")
  elif check is False:
    print("Try again!")
  else:
    print("Good job!")


if __name__ == '__main__':
  main()
    

  



