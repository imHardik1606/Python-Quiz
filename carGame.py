command = ""
while True:
    command = input("> ")
    if command.upper() == "STOP":
        print("car stopped..")
    elif command.upper() == "START":
        print("car started !!!! ")
    elif command.lower() == "help":
        print("""
        START - TO START THE CAR
        STOP - TO STOP THE CAR
        QUIT - TO EXIT
        FAST - TO INCREASE SPEED
        SLOW - TO DECREASE SPEED
        """)
    elif command == "fast":
        print("car fasten")
    elif command == "slow":
        print("car slowed...")


    elif command == "quit":
        confirm = input("are you sure ? ")
        if confirm == "yes":
         break
        elif confirm == "no":
         continue
    else:
        print("sorry i didn't understand that")
print("Thank you for playing")