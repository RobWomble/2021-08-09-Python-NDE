dogs = True
cats = False

print(dogs) # True
print(cats) # False

x = 3
print(x < 5) # True
print(x > 5) # False
print(x == 3) # True
print(x >= 3) # True
print(x <= 3) # True

print("String Comparisons")
txt = "yarn"
print(txt == "yarn") # True
print(txt.upper() == "YARN") # True
print(txt.endswith("rn")) # True
print(txt.startswith("ya")) # True


# if <expression>:   # (only if it evaluates to True)
#    do this

if x == 4: 
    print("X is actually equal to 4!")
   
if x < 10:
    print("X must be a small number") 

if x == 3:
    print("X is 3")
else:
    print("X is not 3")

if x == 5:
    print("X is 5")
else:
    print("X is not 5")




print("Using elif")
y = 3
if y < 5:
    print("y is a really small number")
elif y < 20:
    print("y is a smallish-medium number")
elif y < 100:
    print("y is just a medium number")
else:
    print("y is a super big number")

print("Only IF")

if y < 5:
    print("y is a really small number")
if y < 20:
    print("y is a smallish-medium number")
if y < 100:
    print("y is just a medium number")
else:
    print("y is a super big number")












