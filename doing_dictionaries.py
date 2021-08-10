empty = {}

# syntax = {"key": "value"}

my_car = {"type": "minivan"}

your_car = {"type": "sports coup", "brand": "ferrari", "color": "red"}

jays_cars = {"cars": ["black lambo", "white rolls royce phantom", "midget"]}

print(jays_cars.get('dogs'))
print(jays_cars.get('cars'))
# ['black lambo', 'white rolls royce phantom', 'midget']

# GOAL: Jay Leno has a white rolls royce phantom
print(f'Jay Leno has a {jays_cars["cars"][1]}')


print(my_car)
print(my_car["type"])

print(your_car)
print(your_car["type"])
print(your_car["brand"])
print(your_car["color"])
