# -*- coding: utf-8 -*-
"""Lab 03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1exORWpLUNkjN6wMO51L9cjQqJytyoRZ_

# Maxima & Minima of a function

Topic covered:


1.   Differentiation and plotting
2.   Solving Equations using sympy
3. Finding maxima and minima
"""

from numpy import *
from sympy import *
from matplotlib.pyplot import *

x, y , z = symbols('x y z')
f= x**3 - 4*x + 3
init_printing(pretty_print=True)
display(solve(f))

"""Solve $ x^2 + x - 6 =0 $"""

solve(x**2+x-6, x)

"""Solve $ sin(x) + sin(2x) = 1$"""

solve(sin(x)+sin(2*x)-1,x)

solveset(sin(x)+sin(2*x),x)

"""Solveset gives us entire family of solution. If a range is given, we can also solve this as following"""

i = Interval(-pi, 2*pi/3)
solveset(sin(x)+sin(2*x),x,i)

"""We want real roots for $t^3-1=0$"""

t = symbols('t', real=True)
solve(t**3-1, t)

"""# Taking a function input and calculating derivative"""

f = eval(input())
print("given function")
display(f)
print("Differentiating wrt x: ")
g = diff(f,x)
# diff(f(x), x, order)
display(g)
print("Second derivative:")
display(diff(f,x,2))

"""Plotting $f(x)$ and $f'(x)$ in a given range"""

def dplt(f, r):
  a = linspace(r[0], r[1], 1001)

  f_val = [f.subs(x,i) for i in a]
  g = diff(f,x)
  g_val = [g.subs(x,i) for i in a]
  str1 = "function= "+ str(f)
  str2 = "derivative= "+ str(g)
  plot(a, f_val, label = str1 )
  plot(a, g_val, label = str2 )
  grid()
  legend()
  show()

f = eval(input())
dplt(f, [-5, 5])

"""# To find the extrema of a function $f(x)$ in given range $I$:


1.    Find $f'(x)$ and solve $f'(x)=0$ for $ x \in I$. Let the solution set is $X$
2.  Calculate $f''(x) $ for $x \in X$.

*   If $ f''(a) <0 $ for $a \in X$ then $f(a)$ is a local maxima.

*   If $ f''(a) >0 $ for $a \in X$ then $f(a)$ is a local minima.


3.  If $ f''(a) = 0 $ for $a \in X$ then, maxima or minima exists only if $f^{(2k+1)}(a) = 0 $ for all $k \in 	\mathbb{N} $. In that case, there exist a $p \in 	\mathbb{N} $ such that $f^{(2p)}(a) \neq 0 $ and  $f^{(2n)}(a) \neq 0 $ for $n < p$. $f(a)$ is a local maxima if $f^{(2p)}(a) <0 $ and $f(a)$ is a local minima if $f^{(2p)}(a) > 0 $
4. If $f^{(2k+1)}(a) \neq 0 $ for any $k \in 	\mathbb{N},  a \in X$ then $f(a)$ is neither local maxima nor minima.

"""

# The code is not generalized

def extremum(f):
  df = diff(f, x)
  ddf = diff(df, x)
  root = solve(df)
  roots = [i.evalf() for i in root]
  f_val = [f.subs([(x,i)]).evalf() for i in roots]
  ddf_val = [ddf.subs([(x,i)]).evalf() for i in roots]
  for i in range(len(roots)):
    if ddf_val[i] < 0:
      print(f"at x={roots[i]}, we have local maxima, f({roots[i]})= {f_val[i]}")
    elif ddf_val[i] > 0:
      print(f"at x={roots[i]}, we have local minima, f({roots[i]})= {f_val[i]}")
    else:
      print("Pari Na :( )")

f= eval(input())
extremum(f)

a = linspace(-1, 1, 1001)
f_val = [f.subs(x,i) for i in a]
plot(a, f_val )
grid()
show()

"""We can see, the maxima-minima was accurate"""

f= x**4
extremum(f)

a = linspace(-1, 1, 1001)
f_val = [f.subs(x,i) for i in a]
plot(a, f_val )
grid()
show()

"""There is a minima at x =0

# Extremum in an Interval
"""

def extremumr(f, r):
  df = diff(f, x)
  ddf = diff(df, x)
  root = solveset(df, x,r)
  roots = [i.evalf() for i in root]
  f_val = [f.subs([(x,i)]).evalf() for i in roots]

  ddf_val = [ddf.subs([(x,i)]).evalf() for i in roots]
  for i in range(len(roots)):
    if ddf_val[i] < 0:
      print(f"at x={roots[i]}, we have local maxima, f({roots[i]})= {f_val[i]}")
    elif ddf_val[i] > 0:
      print(f"at x={roots[i]}, we have local minima, f({roots[i]})= {f_val[i]}")
    else:
      print("Pari Na :( )")

"""Maxima, minima for $f(x) = sin(x) + sin(2x) $ for $x \in [0,5]$"""

f = sin(x)+sin(2*x)
i = Interval(0,5)
extremumr(f, i)