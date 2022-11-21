from thesaurusrex import *
from line_gen import *

idk = determine_emotions(noun_sent)
tester = trex_on_combo(idk)

def trex_on_emotional_word(emotions_list):
    for word in emotional_word:
        print(word.modifiers)

print(tester())
"""coffee = SingleResult("coffee")

print("--------------------")
print("Query: coffee")
print("--------------------")
print("Categories")
print(coffee.categories)
print()
print("Modifiers")
# modifiers are the cool ones
print(coffee.modifiers)
print()
print("Category heads")
print(coffee.category_heads)

purple = SingleResult("purple")

print("--------------------")
print("Query: purple")
print("--------------------")
print("Categories")
print(purple.categories)
print()
print("Modifiers")
print(purple.modifiers)
print()
print("Category heads")
print(purple.category_heads)

#two at once not working"""