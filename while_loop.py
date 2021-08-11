import time
# while <expression>:
#    do something
count = 0
while True:
    count += 1  # count = count + 1
    if count != 3:
        print(f"{count}: This will always run!")
    else:
        print("Skipping number 3")
        continue
    time.sleep(3)
    if count == 5:
        break # exits the while loop


num = 1
while num < 20:
    print(num)
    if num == 7:
        print("Lucky Number!")
    elif num > 17:
        print("Getting Close!")
    num += 3

print("All done while-ing away")
