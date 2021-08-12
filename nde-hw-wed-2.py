# Create a function that will accept two strings. Have the function return a single string after having the two strings inputted combined around the phrase "the last time I was in a porta-potty".

def potty(prepend, append):
    silly_txt = " the last time I was in a porta-potty "
    full_txt = prepend + silly_txt + append
    #f_full_txt = f"{prepend} {silly_txt} {append}"
    return full_txt


my_story = potty("I lost my keys", "but thankfully they were just on the ground")
print(my_story)


