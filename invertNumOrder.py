import re

def invertNumOrder(text):
  expression = re.split('\d+', text)
  numbers = re.findall('\d+', text)

  counter = 0
  for number in numbers[::-1]:
    expression[counter] += number
    counter += 1

  return ''.join(expression)

# print(invertNumOrder("array(array(array(float, 43) 32), 21)"))
