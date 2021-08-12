

#def mine(x, y, z):
#    print(x * y * z)


#mine("7", 8.5, 2) 


while True:
    try:
        x = input("score ")
        x = int(x)
        if x > 89:
            print("You got an A")
        break
    except ValueError as err:
        print(err, "That didn't work")
        continue
    except TypeError as err:
        print(err, "That was the wrong type")
        continue
    except KeyboardInterrupt as err:
        q = input("\nDo you really want to quit? Type 'y' to quit\n")
        if q.lower() == "y":
            break
        else: 
            continue 

print("la fin")
