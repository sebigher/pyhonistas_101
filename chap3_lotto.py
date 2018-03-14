import random

# stupid draws
number1 = random.randint(1, 49)
number2 = random.randint(1, 49)
number3 = random.randint(1, 49)
number4 = random.randint(1, 49)
number5 = random.randint(1, 49)
number6 = random.randint(1, 49)

print("#1:", number1)
print("#2:", number2)
print("#3:", number3)
print("#4:", number4)
print("#5:", number5)
print("#6:", number6)

# type less
draw = [random.randint(1, 49), random.randint(1, 49), random.randint(1, 49),
        random.randint(1, 49), random.randint(1, 49), random.randint(1, 49)]

print(draw)

# type less
redraw = [] # empty list
while len(redraw) < 6:
        redraw.append(random.randint(1, 49))

print(redraw)

# what is the last number in a draw
print(redraw[-1])
print(redraw[-6])

# break the boundary
# print(redraw[7]) # IndexError: list index out of range
# print(redraw[-7]) # IndexError: list index out of range

# are the Python lists heterogenous?


