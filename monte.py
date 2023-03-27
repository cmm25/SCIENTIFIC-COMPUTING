import random


def estimate_root(equation, lower_bound, upper_bound, num_simulations):
    count_roots = 0

    for _ in range(num_simulations):
        x = random.uniform(lower_bound, upper_bound)
        y = equation(x)

        if abs(y) < 1e-7:  # or choose another tolerance
            count_roots += 1

    root_estimate = count_roots / num_simulations * (upper_bound - lower_bound)
    return root_estimate

# Example: Estimate the root of the equation f(x) = 3*x**4+3*x**3-x**2in the interval [-1,1]


def f(x):
    return 3*x**4+3*x**3-x**2


root_estimate = estimate_root(f, -1, 1, 100000)
print(f"Estimated root: {root_estimate}")


def estimate_pi(num_simulations):
    innside_circle = 0
    total_sticks = 0

    for _ in range(num_simulations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            innside_circle += 1

        total_sticks += 1

    pi_estimate = 4 * innside_circle / total_sticks
    return pi_estimate


simulations = 1000000

pi_estimate = estimate_pi(simulations)
print(f"Estimated value of pi: {pi_estimate}")
