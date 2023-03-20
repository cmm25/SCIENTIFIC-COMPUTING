# Numercial Analysis Assignment

## Bissection method

The following equation will be under evaluation using bisection method:
$$ f(x)= 3x^4+3x^3-x^2$$

The graph of the equation is as below:
![graph](picture.png)

Bissection method intenst to find the routes ( nearest routes ) of the given non-linear equation.

In my code shared in this repo we see that we have defined the range of operation by using a and b variables. This is crucial as the route of this equation lies in range.

The intervals a and b are sub-divided until a close enough number per the tolerance is achieved.

The tolerance limits the accuracy of the code to find the closest value towards zero and the iterations gives us the scope of number of loops to be evaluated.

Evident from my equation we obtain:
>Root found at x=0.000000

>Bisection time 0.0007794000002832036 ms

## Newton Raptision method

The following equation will be under evaluation using bisection method:
$$ f(x)= 3x^4+3x^3-x^2-19$$

We also need its root which is:
$$ df(x)= 12x^3+9x^2-2x$$

The derivative is crucial as per its mathematical definition its the tangent line at a point which in this case closesest to the root of the above eqaution.

To find the closest approximation to the given root we have to iniatialize the new values of x1 after obtaining values of x, the eqaution result using x and its derivative as below:
$$ x1= x0 - \dfrac{fx}{dfx}$$

the obtained root is a below:
>Root found at x=0.263763

And the execution time is:
>Newton time 0.00010569999994913815 ms

Which is faster than the bisection time


