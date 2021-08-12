# Write a script that will accept a list of items separated by a space from user input.   Have your script then loop through that list and print each item with the phrase "was found at the dog park" appended to it.

items = input("What did you leave behind? ")

lost_items = items.split()

print(lost_items)

for thing in lost_items:
    print(f"{thing} was found at the dog park") 
