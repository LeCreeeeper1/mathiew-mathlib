E: float       = 2.71828182845905
PI: float      = 3.14159265358979
TAU: float     = 6.28318530717959
PHI: float     = 1.61803398874989
PSI: float     = 0.61803398874989

class MathVector:
  def __init__(self, values: list):
    self.values = values
    for i in values:
      try:
        float(i)
      except ValueError: 
        print(f"{i} is not a number!")

  def sum(self): #Returns the sum of every value
    sum = 0
    for i in self.values:
      sum += i
    return sum

  def add(self, value: float):
    self.values.append(value)

  def pop(self, index: int = -1):
    self.values.pop(index)
    
  def average(self): #Returns the average of every value
     average = self.sum() / len(self.values)
     return average

  def mean(self):
    values = sorted(self.values)
    if len(values) % 2:
      mean = values[len(values) // 2] #Odd amount of values
    else:
      mean = values[len(values) // 2] / 2 + values[len(values) // 2 + 1] / 2 #Even amount of values
    return mean

  def length(self): #Returns the square root of the sums of all values
    squared = 0
    for i in self.values:
      squared += i*i
    length = fast_sqrt(squared, 15)
    return length

  def max(self, farthest_zero: bool = False): #Returns the biggest value
    max = self.values[0]
    for i in self.values[1:]:
      if farthest_zero: 
        if abs(i) > max: max = i
      else:
        if i > max: max = i
    return max

  def min(self, nearest_zero: bool = False): #Returns the smallest value
    min = self.values[0]
    for i in self.values[1:]:
      if nearest_zero:
        if abs(i) < min: min = i
      else:
        if i < min: min = i
    return min


def fast_sqrt(num: float, precis: int = 5, nthpow_of2: int = 1):
  near_sqr = None
  approx = None

  if nthpow_of2 <= 0: return num

  for i in range(precis):

    if approx is None:  
      for j in range(int(num)):
        near_sqr = j
        if j * j > num: break
      approx = (num + near_sqr * near_sqr)/(2 * near_sqr)

    else:
      approx = (num + approx * approx)/(2 * approx)

  return fast_sqrt(approx, 15, nthpow_of2 - 1)

def bit_div(num: int, pow: int = 1, floating: bool = False):
  displace = pow - 1 

  quot_bin = bin(num)
  quot = quot_bin[0:len(quot_bin) - displace]

  if floating:
    rest = quot_bin[len(quot_bin) - displace:]
    zeros = ""
    for i in range(displace): zeros += "0"

    rest = str(int(rest, 2)) + zeros
    quot = int(quot ,2)
    result = str(quot) + "." + str(bit_div(int(rest), pow, floating=False))
    result = float(result)
  else:
    result = int(quot, 2)
    
  return result

def fib(n: int):
  fibonnaci = [0, 1]
  while len(fibonnaci) - 1  < n:
    fibonnaci.append(fibonnaci[-1] + fibonnaci[-2])

  return fibonnaci[-1]

def factorial(n: int):
  factorials = [1]
  while len(factorials) - 1 < n:
    factorials.append(factorials[-1] * len(factorials))
  return factorials[-1]

def sin(x): # Bhaskara I’s approximation 
    x = x % (TAU) 
    sign = 1 
    if x > PI: 
        x -= PI 
        sign = -1 
    if x > PI/2: 
        x = PI - x 

    num = 16 * x * (PI - x) 
    den = 5 * (PI ** 2) - 4 * x * (PI - x) 
    return sign * num / den 

def cos(x): # Bhaskara I’s approximation 
    x = (PI/2 + x) % (TAU) 
    sign = 1 
    if x > PI: 
        x -= PI 
        sign = -1 
    if x > PI/2: 
        x = PI - x 

    num = 16 * x * (PI - x) 
    den = 5 * (PI ** 2) - 4 * x * (PI - x) 
    return sign * num / den 

def tan(x):   
  return sin(x) / cos(x)

def csc(x):   
  return 1 / sin(x)

def sec(x):   
  return 1 / cos(x)

def cot(x):   
  return 1 / tan(x)