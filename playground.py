#many positional arguments

def add(*args):
  sum = 0
  for x in args:
    sum += x
  return sum