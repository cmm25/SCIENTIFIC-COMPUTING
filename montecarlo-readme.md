# MONTE CARLO METHODS
## AUTHORS
1. Zahir Yusuf - SCT211-0037/2021
2. Emmanuel Mulwa - SCT211-0507/2021
3. Mutegi Mutugi -SCT211-0015/2021
## THEORY
Monte Carlo method is a computational techniques u.system by numerous simulations that give an approximation of the result. Named after the gambling town of Monte Carlo due to the gambling scene being a game of chance.
To solve the Buffon's needle problem, which can be solved by dropping needles on a floor constructed of parallel, evenly spaced strips, an early version of the Monte Carlo approach was developed. Enrico Fermi used the Monte Carlo method for the first time when researching neutron diffusion in the 1930s, but he did not publish the results of his experiments.
Although Monte Carlo techniques differ, they frequently have the following characteristics:

1. stablish a range of potential inputs.
2. Create inputs at random from a domain-wide probability distribution.

3. run the inputs via a deterministic calculation.
Add up the outcomes
### Estimation of pi
The basic implementation is the estimation of pi. In our example we shall illustrate using the number of circles within a the larger circle problem to find pi or its estimate:
~~~python
import random

def estimate_pi(num_simulations):
    innside_circle = 0
    total_sticks = 0

    for _ in range(num_simulations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x*2 + y*2 <= 1:
           innside_circle += 1

        total_sticks += 1

    pi_estimate = 4 * innside_circle / total_sticks
    return pi_estimate

simulations=1000000

pi_estimate = estimate_pi(simulations)
print(f"Estimated value of pi: {pi_estimate}")
~~~
The code above sets the sticks within the given area to 0 and the total sticks thrown as zero. We also specify the simulations  set 1000000 in our case. The formulae of the area of the circle at the origin is needed namely:
$$f(x)=x^2+y^2 $$
 where
$$f(x)=1$$
Generating random variables within the range of the roots of x and y we use this as a loop statement to generate more points which intern increase our points thus increase our accuracy measure.
The pi estimate id given through the pi_estimate formulae which we multiply by number of simulations to boost accuracy. Our answer was:
>Estimated value of pi = 3.1423

### Using monte carlo method to find roots of an equation at a point
~~~python
import random

def estimate_root(equation, lower_bound, upper_bound, num_simulations):
    count_roots = 0

    for _ in range(num_simulations):
        x = random.uniform(lower_bound, upper_bound)
        y = equation(x)

        if abs(y) < 1e-5:  # or choose another tolerance
            count_roots += 1

    root_estimate = count_roots / num_simulations * (upper_bound - lower_bound)
    return root_estimate

# Example: Estimate the root of the equation f(x) = 3*x*4+3*x3-x*2in the interval [-1,1]
def f(x):
    return 3*x*4+3*x**3-x*2

root_estimate = estimate_root(f, -1, 1, 100000)
print(f"Estimated root: {root_estimate}")
~~~
To find the roots of our equation namely $$f(x)=3x^4+3x^3-x^2 $$
We need its limits, the accuracy tolerance and number of simulation cycles. Values of x are generated at random within range of the limits and y ist the resultant answer which is compared against the tolerance to initialize a loop that increases the number of roots.
The final step is to find the root estimate which is
>x= 0.0005
