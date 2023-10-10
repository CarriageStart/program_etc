import sympy as sp
sp.init_printing()


x, y, z = sp.symbols("x:z", real=True)
a, b, c, d = sp.symbols("a:d", real=True)

#   1. Derivative
#       - Undefined Function
f = sp.Function("f")(x, y)
sp.diff(f, x)               # rho f/ rho x
sp.diff(f, x, x)            # rho rho f/ rho x rho x
sp.diff(f, x, 2)            # rho rho f/ rho x rho x
f.diff(x, y)                # rho rho f/ rho x rho y
sp.diff(f, x, 2, y, 2)      # rho rho rho rho f/ rho x rho x rho y rho y

#   - Defined Function
expr = x**4 + x**3 + x**2 + x + 1
expr.diff(x)                # 4x**3 + 3x**2 + 2x + 1
sp.diff(expr, x)            # 4x**3 + 3x**2 + 2x + 1


#   - Late Derivative
bef_der = sp.Derivative(sp.exp(sp.cos(x)), x)   # d exp(cos(x)) / dx
aft_der = bef_der.doit()                        # -sin(x)exp(cos(x))



#   2. Integration
f= sp.Function("f")(x, y)
sp.integrate(f, x)                  #   INT(f)dx
sp.integrate(f, (x, a, b))          #   INTa_to_b(f)dx
sp.integrate(f, (x, a, b), (y,c,d)) #   INTc_to_d(INTa_to_b(f)dx)dy
f.integrate(x)                      #   INT(f)dx
f.integrate((x, a, b))              #   INTa_to_b(f)dx

#   - Late Integral
i = sp.Integral(-1*sp.sin(x)*sp.exp(sp.cos(x)), x)  # INT(-sin(x)exp(cos(x)))dx
i.doit()                                            # exp(cos(x))



#   3. Sigma and Pi
#   - sympy.Sum for Sigma and sympy.Product for Pi
n = sp.symbols("n", integer=True)
expr = sp.Sum(1/(n**2), (n, 1, sp.oo))
print(expr)                             # Sigma(1/n**2)
print(expr.doit())                      # pi**2/6

expr = sp.Sum( x**n / sp.factorial(n), (n, 1, sp.oo))
print(expr)
expr = expr.doit()
print(expr)
expr = expr.simplify()
print(expr)

expr = sp.Product(n, (n, 1, 7))
print(expr)
print(expr.doit())                      # 5040



#   4. limit
#   -   sympy.limit(expr, var, target)
sp.limit(sp.sin(x)/x, x, 0)             # limit to 0

f = sp.Function("f")
h = sp.Symbol("h", real=True)
diff_limit = (f(x+h) - f(x))/h
print(sp.limit(diff_limit.subs(f, sp.cos), h, 0))   # -sin(x)
print(sp.limit(diff_limit.subs(f, sp.sin), h, 0))   # cos(x)

expr = (x**2 - 3*x) / (2*x - 2)
p = sp.limit(expr/x, x, sp.oo)
q = sp.limit(expr - p*x, x, sp.oo)
expr_limit = p*x + q
print(f"{expr=} limit to {expr_limit} while x to {sp.oo}")



#   5. Series
#   - sympy.series(expr, var, pos=0, n=num_terms) : Taylor expansion at var=pos with order n-1
#   - Seires can calculate the number after O(~) is removed with ".removeO" method.
f = sp.Function("f")(x)
print(sp.series(f,x))
print(sp.series(f,x,y))                 
print(sp.series(f,x, n=2).removeO())    # calculatable form 




