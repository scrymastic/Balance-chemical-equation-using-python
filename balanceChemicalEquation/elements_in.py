
import re

# find which elements are in the chemical
def find_elements_in(chemical):
    # remove non-alphabetical characters
    chemical = re.sub(r'[^a-zA-Z]', '', chemical)

    elements = []
    for i in range(len(chemical) - 1):
        if chemical[i].isupper() and chemical[i+1].islower():
            elements.append(chemical[i:i+2])
        elif chemical[i].isupper():
            elements.append(chemical[i])
    if chemical[-1].isupper():
        elements.append(chemical[-1])
    return elements


# find which elements are in the list of chemicals
def find_elements_in_list(chemicals):
    # remove non-alphabetical characters
    chemicals = [re.sub(r'[^a-zA-Z]', '', chemical) for chemical in chemicals]
    elements = []
    for chemical in chemicals:
        for element in find_elements_in(chemical):
            if element not in elements:
                elements.append(element)
    return elements


# find how many a element appears in a chemical
# example: how many K in K2(SO4)3, answer: 2
def number_of_occurrences_of_an_element_in_a_chemical(element, chemical):
    chemical += "~"
    # find all indexes of the element in the chemical
    indexes = [m.start() for m in re.finditer(element, chemical)]

    # those 2 lines asserts that "Cl" not counted as "C", "Ni" not counted as "N", etc.
    if len(element) == 1:
        indexes = [index for index in indexes if not chemical[index+1].islower()]

    if len(element) == 2:
        indexes = [index + 1 for index in indexes]
    
    total_times = 0

    for i in indexes:
        times_appear = 1
        appears = ""
        while chemical[i+1].isnumeric():
            appears += chemical[i+1]
            i += 1
        if appears:
            times_appear = int(appears)
        appears = ""
        brackets = 0
        for j in range(i+1, len(chemical)):
            if chemical[j] == ")":

                if brackets == 0:
                    while chemical[j+1].isnumeric():
                        appears += chemical[j+1]
                        j += 1
                    if appears:
                        times_appear *= int(appears)
                        appears = ""
                if brackets != 0:
                    brackets += 1
            elif chemical[j] == "(":
                brackets -= 1
            if chemical[j] == "~":
                break
            
        total_times += times_appear
    return total_times
            

