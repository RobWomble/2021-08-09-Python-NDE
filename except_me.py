import time

SUCCESS = False
try:
    word = input("Whats the db password dude?")
    time.sleep(30)
    if word == "radical":
        print("You win!")
    elif int(word) > 41 and int(word) != 42:
        print("You won the secret prize!")
    SUCCESS = True
except TypeError as err:
    print(err)
    print("You should try this again!")
    SUCCESS = False

#finally:
print(f"Alert: Success message: {SUCCESS}")
