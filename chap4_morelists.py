mixed_list = ["white", True, 123 ]
print(mixed_list)


# can you add a value to an index that doesn't exist?
# no

# mixed_list[4] = "aaa" # IndexError: list assignment index out of range

# generally wrong: you can add to whatever index --> gaps

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

print(len(scores))

index = 0
while index < len(scores):
    print("bubble solution index:" + str(index), "have score:", scores[index])
    index = index + 1

# we know how many elements, why not for, but we are losing the index...
for score in scores:
    print("bubble: ", score)

length = len(scores); print("length is:", length)
for i in range(length):
    print("bottle #" + str(i), "with scores:", scores[i])


# not limited to 0 ..

for i in range(1, length):
    print("bittle #" + str(i), "with scores:", scores[i])

# with step
for i in range(1, length, 2):
    print("buttle #" + str(i), "with scores:", scores[i])

#backwards
for i in range(length - 1, 0, -3):
    print("bettle #" + str(i), "with scores:", scores[i])