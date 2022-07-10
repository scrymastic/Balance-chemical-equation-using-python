from fractions import Fraction
from numpy import linalg
from math import lcm

# solve simultaneous equations with some unknowns
# example:
# solve simultaneous equations with unknowns x, y, z
# x + y + z = 1
# x + 2y + 3z = 2
# x + 3y + 6z = 3
# A = [[1, 1, 1], [1, 2, 3], [1, 3, 6]]
# Y = [1, 2, 3]
# returns: [0, 1, 0]
def solve(A, Y):
    result = linalg.inv(A).dot(Y)
    # get result as fractions
    result = [Fraction(x).limit_denominator() for x in result]
    # get lcm of all denominators
    lcm_of_denominators = lcm(*[x.denominator for x in result])
    # get result as integers
    result = [int(x * lcm_of_denominators) for x in result]

    result = [lcm_of_denominators] + result
  
    return result

