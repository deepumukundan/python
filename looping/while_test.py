def looper(): 
    while True:
        user_input = input("Enter a word (q to quit): ")
        if user_input == "q":
            break
        print(f"You entered: {user_input}")

looper()