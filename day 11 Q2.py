class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Barks")

class Cat(Animal):
    def sound(self):
        print("Meows")

for Animal in (Dog(),Cat()):
    Animal.sound()


OUTPUT----\

PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 11 Q2.py"
Barks
Meows
