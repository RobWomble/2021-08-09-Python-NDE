my_empty_list = []

cat_names = ["fluffy", "snowball", "garfield"]
# index         0           1           2

print(cat_names)
print(0, cat_names[0])
print(1, cat_names[1])
print(2, cat_names[2])

for cat in enumerate(cat_names):
    print(cat)

for cat in cat_names:
    print(cat)


something_else = [1, "a", 2.37, "duck", 3, True, 4]
# index           0   1     2     3     4    5   6

print(something_else)
print(something_else[0])
print(something_else[1])
print(something_else[2])
print(something_else[3])
print(something_else[4])
print(something_else[5])
print(something_else[6])
# print(type("oliver"))
# print(type(cat_names))
print(cat_names)
print(cat_names.append("nugget"))

print(cat_names)



