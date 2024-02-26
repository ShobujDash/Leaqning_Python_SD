# chai_type = {
#   "Masala":"Spicy",
#   "Ginger": "Zesty",
#   "Green":"Mild"

# }
# print(chai_type)
# print(chai_type["Masala"])
# print(chai_type.get("Ginger"))
# print(chai_type.get("Gingerrrrrr")) # return None
# print(chai_type["Gingerrrrrr"])  # return Error


# chai_type["Green"] = "Fresh"
# print(chai_type)

# for chai in chai_type:
#   print(chai)

# for chai in chai_type:
#   print(chai , chai_type[chai])


# for key, value in chai_type.items():
#   print(key, value)

# if "Masala" in chai_type:
#   print("I have masala chai")


# chai_type["Earl Grye"] = "Citrus"


# # Dictonary Methods 
# print(chai_type.items())
# print(chai_type.keys())
# print(chai_type.pop("Masala")) # Masala key and value ke delete kori felbe
# print(chai_type.popitem()) # last e jeta add korci oita delte kore return korbe
 

# print(chai_type)













# <----------------------Set---------------------->
# Set in Python
# Set is the collection of the unordered items 
# Each element in the set must be unique & immutable.

# nums = {1,2,3,4}
# set2 = {1,2,2,2}
# repeated elemets stored only once , so it resolved to {1,2}
# null_set = set() #empty set syntex


conllection = {1,2,3,4,5,5,5,"hello","world","world"}
print(conllection)
print(type(conllection))

# Empty set
collectionEmpty = set() 
collectionEmpty.add(1)
collectionEmpty.add(2)
collectionEmpty.add(3)
collectionEmpty.add("Shobuj")
collectionEmpty.add(((1,2,3,4)))

collectionEmpty.remove(2)
print(collectionEmpty)

