import math
def bisection(a,b,f,tolerance=1e-6,max_tolerance=100 ):
    for i in range(max_tolerance):
        c=(a+b)/2
        if abs (f(c))< tolerance:
            print(f"Root found at x={c:7f}")
            return
        elif (f(c)*f(a)) < 0:
            max_tolerance=100
            b=c
        else:
            a=c
def f(x):
    return 3*x**4+3*x**3-x**2
bisection(-1,1,f)
import math
def newton_raphson(x0,f,df,tolerance= 1e-7,max_tolerance=100):
    for i in range(max_tolerance):
        fx=f(x0)
        dfx=df(x0)
        x1=x0 - fx/dfx
        if abs(f(x1)) < tolerance:
         print(f"Root found at x={x1:6f}")
         return
        else:
            x0=x1
def f(x:int):
    return 3*x**4+3*x**3-x**2-19
def df(x:int):
    return 12*x**3+9*x**2-2*x
newton_raphson(1,f,df)
import timeit
from timeit import Timer
max_loops=1
bisection_timer= Timer("bisection(-1,1,f)","from __main__ import bisection,f")
bisection_time= bisection_timer.timeit(max_loops)
print("bisection time", bisection_time, "ms")
print()
newton_timer= Timer("newton_raphson(1,f,df)","from __main__ import newton_raphson,f,df")
newton_time= newton_timer.timeit(max_loops)
print("Newton time", newton_time, "ms")
