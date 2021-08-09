cars = []
fords = ["F150", "Mustang"]
chevy = ["cobalt", "spark"]
toyota = ["Tacoma", "prius"]

cars.append(fords)
cars.append(chevy)
cars.append(toyota)

print(cars)
#              [['F150', 'Mustang'], ['cobalt', 'spark'], ['Tacoma', 'prius']]
# outer_index           0                     1                     2
#               ['F150', 'Mustang']  ['cobalt', 'spark']  ['Tacoma', 'prius']
# inner_index      0         1           0         1          0         1
print(cars[0])
zero_list = cars[0]
cars[0] = "poodles"
print("Zero List")
print(zero_list)
print(zero_list[1])

print("New Cars with Poodles")
print(cars[0][1])

print(cars[0] == zero_list)





