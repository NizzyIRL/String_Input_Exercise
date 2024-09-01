print ("Username Input Exercise")
print ("1. Username must be more than 12 characters.")
print ("2. Username must not contain spaces.")
print ("3. Username must contain digits.")


username = input("Enter a username: ")
username.find(" ")
username.isalpha()

if len(username) > 12:
    print("Invalid username. Must not be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username must not have spaces.")
elif not username.isalpha():
    print("Your username can't contain numbers.")
else:
    print(f"Welcome {username}!")