import sympy as sp
sp.init_printing() # Print sympy objects in symbols, not as python objects

# 0. In sympy, symbol is a node of excution tree structure.

# 1. Defining symbol : It is recommended to enter "real" and "pos" option.
#   if not specified, all is operates as imaginary. 
#   ex) sqrt(y^2) => "sqrt(y^2) while sqrt(x^2) = "x"
real_symbols = [sp.Symbol("x", real=True, positive=True),]
img_symbols = [sp.Symbol("y", imaginary=True),]
    # String is the value of this object in sympy
    # If two objects have the same symbol, sympy cannot distinguish them.

    # Implicit property setting
    # "negative", "positive" -> implicitly imply "real"
    # "even", "odd" -> implicitly imply "integer"

# 1-1. Tuple Assignment : Parsed with ", \n\t"
a, b, c = sp.symbols("a, b, c", negative=True)
tupel_symbols = list(sp.symbols("d e f", negative=True))
tupel_symbols2 = list(sp.symbols("d\ne\nf", negative=True))
print(f"{tupel_symbols=}, len={len(tupel_symbols)}")
print(f"{tupel_symbols2=}, len={len(tupel_symbols2)}")

a, b, c = sp.symbols(":c", negative=True)
x0, x1, x2 = sp.symbols("x:3", negative=True)
x3, x4, x5 = sp.symbols("x3:6", negative=True)
x01, x02, x03, a01, a02, a03 = sp.symbols("x0(:3), a0(:3)", negative=True)
((x01, x02, x03,), (a01, a02, a03)) = sp.symbols(("x0(:3)", "a0(:3)"), negative=True)
coordinates_symbols = list(sp.symbols(r"x(:2\,:2)"))    # Grid
print(f"{coordinates_symbols=}")

# 1-2. Numerical Symbol
#   - To avoid the python native type and symbolic number, sympy defines seperate class
#   for numeric values.
#   - This numerics are inheritantly precise since it is symbol.
i = sp.Integer(19)
f = sp.Float(0.3)       #   Already polutted by the python interpreter before initialize
f = sp.Float("0.3")     #   Recommended
f = sp.Float(0.3, 25)   #   Precision by 25 digits under the point
r = sp.Rational(11, 13)#   11 / 13

#   - It can be created with sympy.sypify() <= Recommended
i, f = sp.sympify(19), sp.sympify(1.9)


# Two kinds of symbol can be distinguished as following
n = sp.Symbol("n", integer=True)
i, f = sp.sympify(19), sp.sympify(1.9)

n.is_Symbol     # True
n.is_Integer    # False         <= Whether n is sympy.Integer
n.is_integer    # True          <= Whether n is integer value

i.is_Symbol     # False
i.is_Integer    # True
i.is_integer    # True
f.is_Symbol     # False
f.is_Float      # True
f.is_float      # True
f.is_integer    # False

# In Numerical symbol calculation, 
#   Integer * Rational = Rational
#   Integer * Float    = Float   
#   Float   * Rational = Float  


# 1-3. Fuction Symbol



# 2. Check whether variable is real or imaginary
print(f"{real_symbols[0].is_real=}")
print(f"{img_symbols[0].is_imaginary=}")
#   Other checkings
print(f"{real_symbols[0].is_positive=}")
print(f"{real_symbols[0].is_integer=}")
print(f"{real_symbols[0].is_odd=}")
print(f"{real_symbols[0].is_prime=}")
print(f"{real_symbols[0].is_finite=}")


#   *** Options are important in optimizing the result
natural = [sp.Symbol("n"), sp.Symbol("n", integer=True), sp.Symbol("n", odd=True), ]
print(f"{sp.cos(natural[0]*sp.pi)=}")   # cos(pi*n)
print(f"{sp.cos(natural[1]*sp.pi)=}")   # (-1)**n
print(f"{sp.cos(natural[2]*sp.pi)=}")   # -1

