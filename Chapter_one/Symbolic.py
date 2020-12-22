from sympy import (
    symbols,    # define symbols for symbolic math
    diff,       # differentiate expressions
    integrate,  # integrate expressions
    Rational,   # define rational numbers
    lambdify,   # turn sumbolic expression into python functions
    solve,
    exp,
    sin,
    cos,
    latex,
    simplify,
    expand,
)

t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt = diff(y, t)

print(dydt)
print("Acceleration:", diff(y,t,t))

y2 = integrate(dydt,t)

print(y2)

v = lambdify([t, v0, g], dydt)
print(v(t=0, v0=5, g=9.81))
print(v(t=2, v0=5, g=9.81))

roots = solve(y,t)
print(roots)

f = exp(t)
print(f.series(t,0,3))

f = exp(sin(t))
print(f.series(t,0,8))

print(latex(f.series(t,0,8)))

x, y = symbols('x y')
f = -sin(x)*sin(y)+cos(x)*cos(y)
print(simplify(f))

print(expand(sin(x+y), trig=True))