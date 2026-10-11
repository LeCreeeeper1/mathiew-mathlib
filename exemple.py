import mathiew as mtw
import math

a = mtw.fast_sqrt(252)
a2 = mtw.fast_sqrt(252, nthpow_of2=2)
print(a, pow(a, 2))
print(a2, pow(a2, 4))

b = mtw.MathVector([1, 3, 5, 28, -19])

print(f"Sum, average, length :  {b.sum(), b.average(), b.length()}")
print(f"Max, min, min(near to zero) {b.max(), b.min(), b.min(True)}")
print(f"Mean, nb of elements {b.mean(), len(b.values)}")

b.add(-2.3)

print(f"Mean, nb of elements but odd {b.mean(), len(b.values)}")

c = mtw.MathVector(["cheese"]) #not a number

d = mtw.bit_div(15, 3, False) 
e = mtw.bit_div(2925, 8, True)

print(f"15/2^3 int, 2925/2^8 float {d, e}")
print(f"phi = {mtw.PHI}, e = {mtw.PHI}")

f = mtw.fib(20)
print(f)

g = mtw.factorial(7)
print(g)

h = [mtw.sin(2), mtw.cos(2), mtw.tan(2)]
i = [mtw.csc(2), mtw.sec(2), mtw.cot(2)]
print(h, i)

