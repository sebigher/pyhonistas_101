import random

verbs = ["koko", "kiki"]

verb =random.choice(verbs)
print(verb)

age = input("what's your dog's age?=>")
name = input("what's your dog's name?=>")

print("age:", age)
print("name:", name)

print("age is", age, "and name is ", name)

# we can use the same variable
# to contain string or int
trans = "42"
print("trans: ", trans)
print("type is ", type(trans))

trans = int("42")
print("trans: ", trans)
print("type is ", type(trans))


# you need float
print("3.14")
print(float("3.14"))