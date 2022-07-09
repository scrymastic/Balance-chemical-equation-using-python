from fractions import Fraction
from numpy import linalg

# solve simultaneous equations with some unknowns
# example:
# solve simultaneous equations with unknowns x, y, z
# x + y + z = 1
# x + 2y + 3z = 2
# x + 3y + 6z = 3
# A = np.array([[1, 1, 1], [1, 2, 3], [1, 3, 6]])
# Y = np.array([1, 2, 3])
# returns: [0, 1, 0]
def solve(A, Y):
    result = linalg.inv(A).dot(Y)
    # get result as fractions
    result = [Fraction(x).limit_denominator() for x in result]
    # get max denominator
    max_denominator = max([x.denominator for x in result])
    # get result as integers
    result = [int(x * max_denominator) for x in result]
    result = [1*max_denominator] + result
    return result

