import sympy
x,p = sympy.symbols('x p')
fun = x**2+x
print(fun)

ans = sympy.solve([25*p**2-75*p+44], [p])#solves the equation
print(ans[0])
a = list(ans[0])[0]
print(a+a)
print(sympy.integrate(fun,x))#computes the integral