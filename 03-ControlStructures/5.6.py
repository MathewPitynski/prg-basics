time = int(input("Enter time in seconds: "))

while time > 0:
    if time == 5:
        print("five")
    elif time == 4:
        print("four")
    elif time == 3:
        print("three")
    elif time == 2:
        print("two")
    elif time == 1:
        print("one")
    else:
        print(time)
    
    time -= 1