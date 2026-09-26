import mathiew as mtw

a = mtw.fast_sqrt(252)
print(a)

b = mtw.MathVector([1, 3, 5, 28, -19])
print(f"Sum average length {b.sum(), b.average(), b.length()}")

print(f"Max min min(small) {b.max(), b.min(), b.min(True)}")

print(f"Mean len() {b.mean(), len(b.values)}")

b.add(-2.3)

print(f"Mean len() but odd {b.mean(), len(b.values)}")

c = mtw.MathVector(["e"]) #not a number

d = mtw.bit_div(15, 3, False) 
e = mtw.bit_div(2925, 8, True)
print(f"15/2^3 int, 2925/2^8 float {d, e}")
print(f"phi e {mtw.phi, mtw.e}")


