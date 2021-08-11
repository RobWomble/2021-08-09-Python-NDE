# Write a program which accepts a sequence of comma-separated numbers from console and generate a list which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']

num_input = input("Gimme a list of numbers")
print(num_input)
num_out = num_input.split(',')
print(num_out)
print(type(num_out))

text_input = input("Whats your name?  ")
print(text_input)
print(text_input.lower())
print(text_input.upper())
print(text_input.title())
print(text_input.capitalize())


abcs = ["x", "y", "z", "next time won't you sing with me?"]
joined_text = " % ".join(abcs)
print(joined_text)


