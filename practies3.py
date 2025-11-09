# Getters & Setters : This two methods that allows controlled to an objects's attributes.
"""class Student :
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self): # getter( any attribute taken into a method its getter)  
        return self.__name
    
    def set_name(self,name): # stters
        self.__name = name

    def set_age (self,age):
        if isinstance(age,int): # Use this insintance its maintain only put in integer 
            self.__age  = age
        else:
            print("Age should be an int. Error")

    def get_age(self):
        return self.__age



s = Student("Srujan",20)
#s.__age = 100 # there is no controlled access (want to come under controll use getters and setters)
#print(s.age)  # They helps in validating data from accidental modification , and providing controlled access.

print(s.get_name())
# given None becouse no set
s.set_age("chandan")

s.set_name("Kishan")
s.get_age(100)
print(s.get_name()) # its giev error s.__name = kishan 

print(s.get_age())


# 2. Method Overloading : is the ability to define multiple methods with the same name but diffrent parameters.
# python never accept method over loading(like two method put on same one method is over load with other then give the Error ) directly . 
# But we can use defult parameters


class Calculator:
    #def add(self,a,b):
    #    print( a + b)

    def add (self,a,b,c = 0): # This is Overloading
        print (a+b+c)   

c  = Calculator()
c.add(4,5)
c.add(6,7,8)

# 3. Methodoverriding: Method overriding allows a child class to provide a specific implementation for a method that is already defined in its parent class.
# It enable a child  class to alter or extend behaviour of a parent method.
# 4.super : The super() function is used in child class to call a method from the parent class ,enacling access to inherited methods or attributes.

class Animal:
    def make_sound(self)      :
        print("Animal is making sound ")

class Dog (Animal):
    def make_sound(self):
        super().make_sound() # parent class method na child class mathod over ride madodu its over ride
        print("Bark")"""
"""class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} is Barking")

    def get_anggry(self,name)   :
        self.name  = name
        super().make_sound()
        self.make_sound()

        print(f"{self.name} is anggry")


d = Dog("doggy")        
d.make_sound()

# 5. Abstract class :  like [ Class  - Template for object] [Abs_class = template  blue print]
#  An abstarct class in python is a class that cannot be instantiated directly . It can have abstract methods, which much be implemented by subclasses
# ABSTRACT classes provide a bule print for other class.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod   # it is a decorator [this decorate under 2 line functions]
    def start_engine(self):
        pass              # mean by "psss" will want after its not working now

class Bike(Vehicle) :
    def __init__(self,name):
        self.name = name

    def start_engine(self):
        print("Starting engine") 

b  = Bike ("Royal Enfield")

print(b.name)

# Home Work on OOP

# 1

class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self)    :
        print(f"{self.brand}  cost {self.price}")

m1  = Mobile("Nokia",10000)
m2 = Mobile("i phone",50000)


m1.display()
m2.display()


# 2

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"{self.name} marks is  {self.marks}")

s1 =  Student("Srujan", 60)        
s2  = Student("Kishan",70)

s1.display_info()
s2.display_info()


# 3

class Movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating  = rating

    def  display_rating(self):
        print(f"{self.title} and its rating is {self.rating}")


m1 = Movie("KGF",9.5)
m2 = Movie("Bahubali",9.5 )

m1.display_rating()

# 4

class Employee:
    def __init__(self,name,designation,salary  = 30000):
        self.name = name
        self.designation= designation
        self.salary = salary

    def display_info(self):
        print(f"{self.name} has a {self.designation} destignation - {self.salary}")

E1  = Employee("Srujan","Owner",10000)        
E2  = Employee("Kishan","Ownbissneuss")

E1.display_info()
E2.display_info ()
        

# Home work on 4 pillors


class  BankAccont():
    def __init__(self,acc_num,balance):
        self.__acc_num = acc_num
        self.__balance = balance

    def check_balance(self)    :
        print(self.__balance)

    def deposit(self,ammount)   :
        self.__balance += ammount

    def Withdrow(self,amount)     :
        if self.__balance<amount:
            print("Insufficiant funds")
            return

        self.__balance -= amount
        print(f"Withdraw successful - Balance:{self.__balance}")


a = BankAccont(acc_num=4454636,balance=5000)
#a.deposit(100)
#a.check_balance()
a.Withdrow(300000)

# Home work 5
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle):
    def __init__(self,name):
        self.name = name

    def ride(self):
        print("Riding")
b = Bike("Royal Enfield")

b.start()
b.ride()

# 6 polymorphisom

class Shape():
    def calc_area(self):
        print("Area calculated")

class Circle(Shape):
    def __init__(self,radious):
        self.radious = radious

    def calc_area(self):
        print(f"Area of circle: {(22/7)*self.radious*self.radious}")    

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calc_area(self):
        print(f"Area od rectangle:{self.l*self.b}")     

c =  Circle(5)        
r  = Rectangle(3,4)

c.calc_area()
r.calc_area()"""

# 7 HW on Gettrs and Setters

class BankaAccount:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,updated_balance):
        if updated_balance<0:
            print( "ERROR: Balance cannot be  negative value")
            return
        self.__balance = updated_balance
        print(f"Balance updated to :{self.__balance}")

acc1 = BankaAccount(5000)
print("Current Balance:",acc1.get_balance())

acc1.set_balance(8000)

print("Updated Balance:",acc1.get_balance())

# 8 Method overriding

class Shape:
    def draw(self):
        print("Drawing Shape")

class Circle(Shape):
    def draw(self):
        #super().draw()
        print("Drawing Circle")

c  = Circle()
c.draw()

# 9 Abstract class

from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def claculate_salary(self):
        pass  #print("Salary is calculated")

class Manager(Employee):
    def claculate_salary(self):
      print("Maneger's salary is calculated")

m = Manager()    
m.claculate_salary()













        







