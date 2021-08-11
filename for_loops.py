
cats = ["fluffy", "snowball", "garfield"]

# for iterator in iterable:
#    do something

for cat_name in cats:
    print(cat_name)


scores = [99, 26, 94, 45, 65, 84, 101, 2, 62]

for score in scores:
    print(score)
    if score > 100:
        print("You cheated!")
    elif score > 89:
        print("Awesome A!")
    elif score > 79:
        print("Boo-yah B!")
    elif score > 69:
        print("Common C")
    elif score > 59:
        print("D's get Degrees")
    else:
        print("Please try again, somewhere else") 


for num in range(1, 6):
    print(num)

print(type(range(1,6)))
