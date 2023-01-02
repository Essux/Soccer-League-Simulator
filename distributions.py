import math
import random

def sample_poisson(mean: float) -> int:
    # Generate a uniform random number between 0 and 1
    u = random.random()
    
    # Initialize x to 0
    x = 0
    
    # Calculate the cumulative distribution function at x
    f = math.exp(-mean)
    
    # Loop until f is greater than or equal to u
    while f < u:
        # Increment x
        x += 1
        
        # Calculate the cumulative distribution function at x
        f += math.exp(-mean) * mean ** x / math.factorial(x)
    
    # Return x
    return x
