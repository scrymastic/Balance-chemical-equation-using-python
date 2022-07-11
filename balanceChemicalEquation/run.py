
from analysis_chemical_equation import *


def main():
    """
    This function will calculate the balance of a chemical equation.
    """
    while True:
        chemical_equation = input("Equation: ")
        if chemical_equation == "/":
            print("Bye!")
            quit()

        print(balance(chemical_equation))

    # f = open("testcase.txt", "r")
    # for line in f:
    #     if line == "/":
    #         print("Bye!")
    #         quit()
    #     print(balance(line))

print("This program will calculate the balance of a chemical equation.")
print("Enter the chemical equation or / to exit.")
print("The reactants and products should be separated by a equal sign (=).")
print("Each chemical should be separated by a plus sign (+).")
print("Example:")
print("Equation: KMnO4 + FeSO4 + H2SO4 = MnSO4 + Fe2(SO4)3 + K2SO4 + H2O")
print("Now, enter your equation:")

if __name__ == "__main__":
    main()


