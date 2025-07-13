user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

with open("files.txt", "w") as file:
    file.write(f"Name: {user_name}\nAge: {user_age}\n")

with open("files.txt", "r") as file:
    print(file.read())

OUTPUT ---

PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 12 question.py"
Enter your name: hardik
Enter your age: 18
Name: hardik
Age: 18
