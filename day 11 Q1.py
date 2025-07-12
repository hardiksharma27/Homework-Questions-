class Student:
    def __init__(self):
        self.__name = "unknown"
        self.__marks = 0

    def set_details(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_result(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)
        if self.__marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

s1 = Student()
s1.set_details("Ram", 85)
s1.get_result()

OUTPUT --- 

PS C:\next yug classes> & C:/Users/DELL/AppData/Local/Programs/Python/Python313/python.exe "c:/next yug classes/day 11 Q1.py"
Name: Ram
Marks: 85
Result: Pass
