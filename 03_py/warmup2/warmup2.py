def string_times(str, n):
  return str * n

def front_times(str, n):
  return str[:3] * n

def string_bits(str):
  answer = ""
  length = len(str)
  for num in range(length):
    if num % 2 == 0: # only even positions are present
      answer += str[num]
  return answer

def string_splosion(str):
  # you write one part of the string at a time
  answer = ""
  for i in range(len(str)):
    answer += str[:i+1]
  return answer

def last2(str):
  last = str[len(str)-2 : len(str)]
  num = 0
  for n in range(len(str)-2):
    if(str[n : n+2] == last):
      num += 1
  return num

def array_count9(nums):
  answer = 0
  for i in nums:
    if i == 9:
      answer += 1
  return answer

def array_front9(nums):
  size = len(nums)
  if size > 4:
    size = 4
  for i in range(size):
    if(nums[i] == 9):
      return True
  return False

OR!!!!

def array_front9(nums):
  counter = 0
  for i in nums:
    counter += 1
    if(counter != 5):
      if(i == 9):
        return True
    if(counter >=5):
      return False
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if(nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
      return True
  return False

def string_match(a, b):
  number = 0
  length = len(a)
  if(len(b) < length):
    length = len(b)
  for i in range(length-1):
    if(a[i:i+2] == b[i:i+2]):
      number += 1
  return number
