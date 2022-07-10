
from analysis_chemical_equation import *

def main():
    """
    This function will calculate the balance of a chemical equation.
    """
    continuation = True
    while continuation:
        reactants = input("reactants: ")
        if reactants == "/":
            continuation = False
            print("Bye!")
            quit()
        products = input("products: ")

        print(balance(reactants, products))

    # f = open("testcase.txt", "r")
    # for line in f:
    #     reactants = line.split(' - ')[0]
    #     products = line.split(' - ')[1]
    #     print(balance(reactants, products))

print("This program will calculate the balance of a chemical equation.")
print("Enter the reactants and products of the chemical equation.")
print("Each chemical should be separated by a comma.")
print("Example:")
print("reactants: KMnO4, FeSO4, H2SO4")
print("products: MnSO4, Fe2(SO4)3, K2SO4, H2O")
print("Enter / to quit.")
print("Now, enter your equation:")

if __name__ == "__main__":
    main()


