ingredients = {
    "Mixed Soaked Fruit": "200g", 
    "Flour": "400g", 
    "Baking Powder": "1tsp", 
    "Ground Cinnamon": "0.5tsp", 
    "Ground Ginger": "0.5tsp", 
    "Ground Nutmeg": "1 pinch", 
    "Salt": "0.5tsp", 
    "Butter": "200g", 
    "Sugar": "50g", 
    "Eggs": 4
}

print(ingredients["Baking Powder"])

mixed_dict = {
    "integer": 3,
    "float": 4.0,
    "string": "Hello world!",
    "boolean": True,
    "none": None,
    "list": [1, "a", False],
    "dictionary": {"a": 1, "b": 2, "c": 3}
}

dict_mixed = {
    "abc": "A string",
    1: "An integer",
    2.0: "A float",
    False: "A boolean",
    None: "None" 
}

ingredients["Pecans"] = "25g"
print(ingredients)

print(ingredients)
print("That's way too much flour!")
ingredients["Flour"] = "200g"
print(ingredients)

print("I'm allergic to nutmeg...")
del ingredients["Ground Nutmeg"]
print(ingredients)
# ingredients.get("Flour")

# for key in ingredients.keys():
#     print(key)

for key, value in ingredients.items():
    print(f"Ingredient: {key}, Quantity: {value}")

# print(ingredients.keys()) # prints the keys from list in quotes
# print(ingredients.values()) # prints the values of teh keys from list in quotes
# print(ingredients.items()) # prints the keys and its values from list in quotes
print(ingredients["Salt"])