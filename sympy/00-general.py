# Resources
# - YouTube: https://www.youtube.com/watch?v=cvHyaE_bs8s&list=PLRJx8WOUx5Xd3_dgw5xRmABUd8MWdsA_C&index=8
# - iPython Notebook: http://nbviewer.ipython.org/github/twistedhardware/mltutorial/blob/master/notebooks/IPython-Tutorial/8%20-%20SymPy.ipynb
# - http://docs.sympy.org/0.7.1/tutorial.html
# http://docs.sympy.org/dev/tutorial/printing.html


from sympy import *

x, y, z = symbols('x y z')

print Integral(sqrt(1/x), x)

pprint(Integral(sqrt(1/x), x))

expr = 2**x+1
print expr
pprint(sqrt(expr))

print solve(expr)
pprint(solve(sqrt(expr)))

