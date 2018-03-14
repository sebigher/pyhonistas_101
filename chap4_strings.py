import random
# some questions

name1 = "Hawking"
name2 = "Hawking"


# objects has the same id
# working like two references to the same object
print(id(name1))
print(id(name2))


names = ["Bond", "Hawking"]

name3 = random.choice(names)
print(name3)
print(id(name3))

# will have the same id
print(id(names[1]))

if names[1] == name1:
    print("equals")
else:
    print("not equals")






