user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

with open("files.txt", "w") as file:
    file.write(f"Name: {user_name}\nAge: {user_age}\n")

with open("files.txt", "r") as file:
    print(file.read())