
from elements_in import *
from solve_simul_equation import solve


def balance(reactants, products):
    reactants = reactants.replace(" ","").split(",")
    products = products.replace(" ","").split(",")
    chemical_elements_in_reactants = find_elements_in_list(reactants)
    chemical_elements_in_products = find_elements_in_list(products)

    # compare the two lists
    if set(chemical_elements_in_reactants) != set(chemical_elements_in_products):
        print("The chemical equation is not valid.")
        quit()

    # balance the equation: KMnO4 + FeSO4 + H2SO4 → MnSO4 + Fe2(SO4)3 + K2SO4 + H2O
    # assume:
    # 1KMnO4 + aFeSO4 + bH2SO4 → cMnSO4 + dFe2(SO4)3 + eK2SO4 + fH2O
    # using the law of conservation of elements:
    # get:
    # K : 1 = 2e
    # Mn : 1 = c
    # O : 4 + 4a + 4b = 4c + 12d + 4e + 
    # Fe : a = 2d
    # S : a + b = c + 3d + e
    # H : 2b = 2f
    numbers_of_unknowns = len(reactants) + len(products) - 1
    A = []

    for element in chemical_elements_in_reactants:
        E = []
        for chemical in reactants[1:]:
            E.append(how_many_times_elements_in_chemical(element, chemical))
        for chemical in products:
            E.append(-how_many_times_elements_in_chemical(element, chemical))
        A.append(E)
        if len(A) == numbers_of_unknowns:
            break

    Y = []
    for element in chemical_elements_in_reactants:
        Y.append(-how_many_times_elements_in_chemical(element, reactants[0]))
        if len(Y) == numbers_of_unknowns:
            break


    result = solve(A, Y)
    chemical_equation = reactants + products
    answer = ""
    for i in range(len(result)):
        if result[i] == 1:
            result[i] = ""
        else:
            result[i] = str(result[i])
        answer += result[i] + " " + chemical_equation[i]
        if i == len(reactants) - 1:
            answer += " → "
        if i == len(chemical_equation) - 1 or i == len(reactants) - 1:
            pass
        else:
            answer += " + "
    return answer





