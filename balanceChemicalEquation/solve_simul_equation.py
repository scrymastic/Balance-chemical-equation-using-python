from fractions import Fraction
from numpy import linalg
from math import lcm
from itertools import combinations

# solve simultaneous equations with some unknowns
# example:
# solve simultaneous equations with unknowns x, y, z
# x + y + z = 1
# x + 2y + 3z = 2
# x + 3y + 6z = 3
# A = [[1, 1, 1], [1, 2, 3], [1, 3, 6]]
# Y = [1, 2, 3]
# returns: [0, 1, 0]
# if number of equations is greater than number of unknowns, choose some equations to solve until all unknowns are solved then check if the result is correct
def solve(A, Y, number_of_unknowns):
    result = []

    number_of_equations = len(A)
    all_equations = [i for i in range(number_of_equations)]

    # combinations of number_of_unknowns equations selected from all_equations
    equations_to_solve = [list(i) for i in combinations(all_equations, number_of_unknowns)]
    if len(equations_to_solve) == 0: # if len(equations_to_solve) == 0, number_of_unknowns is greater than number_of_equations
        return None

    for equation in equations_to_solve:
        _A = []
        _Y = []
        for j in equation:
            _A.append(A[j])
            _Y.append(Y[j])

        try:
            result = linalg.inv(_A).dot(_Y)
            break
        except:
            pass

    if result == []:
        return None

    # get result as fractions
    result = [Fraction(x).limit_denominator() for x in result]

    # get lcm of all denominators
    lcm_of_denominators = lcm(*[x.denominator for x in result])

    # get result as integers
    result = [int(x * lcm_of_denominators) for x in result]

    # check if the result is correct
    for i in range(number_of_equations):
        left = 0
        right = 0
        for j in range(number_of_unknowns):
            left += A[i][j] * result[j]
        right += Y[i]*lcm_of_denominators

        if left != right:
            return None

    result = [lcm_of_denominators] + result
    return result


