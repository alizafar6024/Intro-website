# file_path = r"C:\Users\Ali Hamza Zafar\Desktop\Python\demo.txt"

# f = open(file_path, "r")
# # data = f.read()
# # print(data)

# data1 = f.readline()
# print(data1)

# # data2 = f.readline()
# # print(data2)

# f.close()

# f = open(file_path, "a")
# f.write("\nbut it was all in vain")
# f.close()

# file_path = r"C:\Users\Ali Hamza Zafar\Desktop\Python\demo.txt"

# f = open(file_path, "a+")
# # f.write("abs")
# print(f.read())
# f.write("abs")

# with open(file_path, "r")as f:
#     data = f.read()
#     print(data)

# with open(file_path, "w") as f:
#     data = f.write("this is me again")

# file_path = r"C:\Users\Ali Hamza Zafar\Desktop\Python\demo.txt"

# import os
# # DEFINE THE FILE PATH
# file_path = os.path.join(os.path.expanduser("~"), "desktop", "folder","python", "demo.txt")
# # checking the file
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print("file deleted successfully")
# else:
#     print("FILE NOT FOUND")

# os.remove(file_path)

# with open("practice.txt", "w") as f:
#     f.write("hi everyone. \nWe are learning File I/O")
#     f.write("\nusing Java. \nI like programming in Java.")

# f = open("practice.txt", "r+")
# data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     data.find(word)
# if (data.find(word) != -1):
#     print("exist")
# else:
#     print("not exist")

# def find_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         data.find(word)
#         if (data.find(word) != -1):
#             print("exist")
#         else:
#             print("not exist")

# find_word()

# def find_line():
#     word = "puy"
#     line = 1
#     data = True
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line)
#                 return
#             line += 1
#         return -1

# # print(find_line())

# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(num)
#             num = ""
#         else:
#             num += data[i]

# count = 0 
# with open("practice.txt", "r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if (int(val) % 2 == 0):
#             count += 1

# print(count)


# Chapt 8

# class Employees:
#     code = 302
#     name = "ali hamza"

# s1 = Employees()
# print(s1.name)
# print(s1.code)

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding a new one")

# s1 = Student("Ali", 00)
# print(s1.name, s1.marks)

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def Welcome(self):
#         print("welcome students")

#     def get_marks(self):


# s1 = Student("Ali", 00)
# print(s1.name, s1.marks)

# class Student:
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("Here you go...")

#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum += val
#         print("well", self.name, "avg score is", sum/3)



# s1 = Student("Ali", [55,65,66])
# s1.get_avg()

# s1.name = "Ali Hamza"
# s1.get_avg()


# class Account:
#     def __init__(self, name, bal, acc):
#         self.name = name
#         self.balance = bal
#         self.account = acc 
        
#     # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print(self.name, "Rs.", amount,  "has been debited from your account")
#         print("your remaining balance is:", self.get_balance())
#     #  credit method
#     def credit(self, amount):
#         self.balance += amount
#         print(self.name, "Rs.", amount,  "has been credited to your account")
#         print("your remaining balance is:", self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account("Ali Hamza", 3000, 24287000650103)
# acc1.debit(1100) 
# acc1.credit(5000)
# acc1.credit(70000)

# Inheritance

# class car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class toyotacar(car):
#     def __init__(self, name):
#         self.name = name

# car1 = toyotacar("fortuner")
# car1 = toyotacar("prius")

# car1.start()

# Multiple Inheritance

# parent class 1
# class A():  
#     varA = "This is class A"

# # Parent class 2
# class B():
#     varB = "This is class B"

# # Derived/child class
# class C(A, B):
#     varC = "This is class C"
     
# var1 = C()

# print(var1.varC)
# print(var1.varB)
# print(var1.varA)       


# class car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class toyotacar(car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()


# car1 = toyotacar("Fortuner", "electric")
# print(car1.name,"\n",car1.type)

# Class method

# class student:
#     name = "anonymous"
    
#     @classmethod
#     def changename(cls, name):
#         cls.name = name

# s1 = student()
# s1.changename("ali")
# print(s1.name)
# print(student.name)

# Q1

# class circle:
#     def __init__(self, radius):
#         self.radius = radius 
    
#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# a1 = circle(2 1)
# print(a1.area())
# print(a1.perimeter())

# Q2

# class employee:
#     def __init__(self, role, depart, sal):
#         self.role = role
#         self.depart = depart
#         self.sal = sal

#     def showdetails(self):
#         print("role =", self.role)
#         print("depart =", self.depart)
#         print("sal =", self.sal)

# class engineer(employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "60,000")

# e1 = employee("cone checker", "packing", "40,000")
# e1.showdetails()
# e2 = engineer("wahiyaat", 40)
# e2.showdetails()
# print(e2.name)

# Q3

class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __lt__(self, od2):
        return self.price > od2.price

od1 = order("chips", 40)
od2 = order("lays", 60)

print(od1 > od2)
