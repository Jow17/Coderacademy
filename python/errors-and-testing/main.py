class NegativeNumberError(Exception):
  pass

try:
  n = int(input('Enter a numerator: '))
  d = int(input('Enter a denominator: '))

  if n < 0 or d < 1: 
    raise NegativeNumberError()

  q = n / d #Exception was raised when trying to divide by zero

  print(q)

except ZeroDivisionError: 
  print('The denominator cannot be zero.')

except ValueError: 
  print('Inputs must be integers')

except NegativeNumberError:
  print('Inputs cannot be negative')

except Exception as e:
  print('Something went wrong')
  print(e) 
  #Log debug information (including traceback) to an error log file