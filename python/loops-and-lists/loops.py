# spam = 0 
# while spam < 5: 
#   print('Hello')
#   spam += 1

# print ('Done')

# for spam in range(1, 50, 4): 
#   print(f'Hello {spam}')

import random 

count = int(input('How many random integers? '))
for i in range (count):
  print(random.randint(1, 100))


