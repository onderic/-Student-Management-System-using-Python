
class Student:
    # Constructor
    def __init__(self,name, rollno, marks1, marks2) -> None:
        self.name = name
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2

    #function to create and append new students
    def accept(self,name,rollno,marks1,marks2):

        # use ' int(input()) ' method to take input from user
        obj = Student(name,rollno,marks1,marks2)
        ls.append(obj)

    def display(self,obj):
        print("Name : ", obj.name)
        print("RollNo  :", obj.rollno)
        print(" Marks1  :", obj.marks1)
        print("Marks2  :", obj.marks2)
        print("\n")

    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn ):
                return i 

    def delete(self, rn):
        i = ob.search(rn)
        del ls[i]            

    def update(self,rn, No):
        i = ob.search(rn)
        roll = No
        ls[i].rollno = roll


# Create a list to add Students
ls = []

# an object of Student class
ob = Student('',0,0,0)

print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")

# ch = int(input("Enter choice:"))
# if(ch == 1):
ob.accept("A", 1, 100, 100)
ob.accept("B", 2, 90, 90)
ob.accept("C", 3, 80, 80)

 
# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    ob.display(ls[i])
 
# elif(ch == 3):
print("\n Student Found, ")
s = ob.search(2)
ob.display(ls[s])
 
# elif(ch == 4):
ob.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    ob.display(ls[i])
 
# elif(ch == 5):
ob.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    ob.display(ls[i])
 
# else:
print("Thank You !")