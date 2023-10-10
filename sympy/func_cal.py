import sympy as sp
sp.init_printing()


x = sp.Symbol("x", real=True)
y = sp.Symbol("y", real=True)
z = sp.Symbol("z", real=True)
a, b = sp.symbols("x, y", positive=True)

# 1. Simplification of function
#   - Factorization
expr = 2*(x**2-x) - x*(x+1) # Saved as 2x*2 - x(x+1) - 2x
expr.simplify()             # x(x-3)
expr.factor()             # x(x-3)
sp.simplify(expr)           # x(x-3)

#   - Trigonal Symplification
expr = 2 * sp.cos(x) * sp.sin(x)
sp.simplify(expr)        # sin(2x)
sp.trigsimp(expr)        # sin(2x)

#   - Exponentials
expr = sp.exp(2x)  * sp.exp(3y)     # exp(2x)exp(3y)
sp.simplify(expr)                   # exp(2x+3y)
sp.powsimp(expr)                   # exp(2x+3y)

#   - Log
expr = sp.log(a) - sp.log(b)
sp.simplify(expr)           # log(a/b)
sp.logcombine(expr)         # log(a/b)

#   - Others...
expr = x + y + x*y*z
expr.collect(x)             # x(yz+1) + y


# 2. expansion
#   - epand() : wrapper function for 
#   "sympy.expand_mul, sympy.expand_trig, sympy.expand_log, sympy.expand_exp, ..."
#   
expr = (x+1) * (x+2)
sp.expand(expr)                             # x**2 + 3*x + 2
sp.expand(expr, mul=True)                   # x**2 + 3*x + 2

sp.sin(x+y).expand(trig=True)               # sin(x)cos(y) + sin(y)cos(x)
sp.log(a * b).expand(log=True)              # log(a) + log(b)
sp.exp(sp.I*a + b).expand(complex=True)     # i e^b sin(a) + e^b cos(a)
sp.exp((a-b)*x).expand(power_exp=True)      # e^(iax) * e^(-ibx)


# 3. Rationals
sp.aprat(1/(x**2 + 3*x + 2), x)             # 1/(x+1) - 1/(x+2)
sp.together(1/(x*y + y) + 1/(1+x))          # (y+1)/(y*(x+1))
sp.cancel(y/(y*x + y))                      # 1/(1+x)


# 4. Substitude
sp.sin(x*sp.exp(x)).subs({x: sp.exp(y), sp.exp: sp.cos})    # cos(exp(y)* exp(exp(y)))
(x + y + z**2 *x).subs({x:1.25, y:0.4, z:3.2})              # 13.3

# 5. Calculation
expr = (x+1) * (x+2)
expr(1)                 # 6
sp.N(x + sp.pi, 10)     # x + 3.1415926535
(x + sp.pi).evalf(10)   # x + 3.1415926535

#   - In array
expr = sp.sin(sp.pi * x * sp.exp(x))
[expr.sins(x, xx).evalf(3) for xx in range(0, 10)]      # [expr(0), expr(1), ...]

#   - In np.array   (Faster)
expr_arr = sp.lambdify(x, expr, "numpy")     # lambdify(symbol, expression)
expr_arr(np.arange(0, 10))  # [expr(0), expr(1), ...]






