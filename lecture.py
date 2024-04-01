# Object Oriented Programming
# built around Classes using the class keyword
# defining a calss
class Vehicle(): # Pascal Case
    pass

# creating an instance of a class
# create variable and set it equal to the class name, WITH PARANTHESES
# creates an object with all the information from our class blueprint
# object is another word for an instance of a class
mazda = Vehicle()
# mazda gets access all the attributes and methods that exist in our class

# =========== Benefits of OOP ===================
# Modularity - separting concerns within classes and divides a program into specific modules

# Scalability  - classes make it easy to expand with new attributes, methods etc..

# Reuse - reusing a user class to access username, password, first name, last name

# Maintenance - update specific instances rather than an entire catalog of data

# __init__ method in classes
# instantiates all the attributes for our class

class OfficeBuilding():
    # this is a special method called a constructor. It is automaticall called when an 
    # object of a class is created. It initializes the objects attributes in its initial state
    #          object, param1  param2
    def __init__(self, floors, offices):
        self.floors = floors #setting attributes in the init
        self.offices = offices #attributes variables inside a class
        # print function to show that this gets called when we
        # instantiate
        # print("HELLO from the __init__")
    
    # adding a class method
    # method is a function inside of a class
    def open_doors(self): #need to take in self
        print(f"Doors are open for business! All {self.offices} of them")

    # self is whats used to reference a speciifc instance of class
    # self in the init assings our arguments to the instances attributes
    # self in the open_doors methods gives the open_doors method
    # access to attributes in the init

the_office = OfficeBuilding(10, 15)

# calling methods from an object (instance of the class)
# using dot notation when calling class methods
# my_list.append(something)
# my_list = []
# my_list.len() attribute error list object has no attribute len
# unique instance of OfficeBuilding

the_office.open_doors()

# creating several unique instances of a class
# another unique instance
parks_and_rec = OfficeBuilding(1, 10)
# another unique instance
office_space = OfficeBuilding(20, 80)
# calling the open_doors() class method
parks_and_rec.open_doors()
# calling the open_doors() class method
office_space.open_doors()

# user class example
class User():
    def __init__(self, email, first_name, last_name, username ):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        # default attribute
        self.login_counter = 1

    def user_info(self):
        print(f"User: {self.username} was created. User Info: first name: {self.first_name} last name: {self.last_name} email: {self.email} ")
    
    def log_ins(self):
        self.login_counter += 1

    def show_logins(self):
        print(f"This user has logged in {self.login_counter} times.")

user1 = User("ryanr@codingtemple.com", "Ryan", "Rhoades", "Rhoadehouse")
user2 = User("jamesmbcarlson@gmail.com", "James", "Carlson", "CoolGuy420ayylamo")
user3 = User("danielcopeland0021@gmail.com", "Daniel", "Copeland", "Frogman")

print("Info for user1")
user1.user_info()
print("Info for user2")
user2.user_info()
print("Info for user3")
user3.user_info()
user1.log_ins()
user1.show_logins()
user1.log_ins()
user1.show_logins()
user1.log_ins()
user1.show_logins()
user1.log_ins()
user1.show_logins()

# setting default parameters
class Car():
    def __init__(self, wheels, engine, doors = 4):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors
#                    doors arugment will overwrite my default parameter
mazda = Car(4, "i4 or 2.31 i4", 5)
# accessing attributes from a class
print(mazda.doors)
# default paramter of 4 will be taken
lumina = Car(4, "v6")
print(lumina.doors)

class Car():
    def __init__(self, wheels, engine, doors):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors
        self.color = "blue"

    # add a method to change the car color
    def paint_job(self):
        color = input("What color would you like to paint your car? ")
        self.color = color
    
    


honda = Car(4, "i4", 4)
# chaning the value of an attribute by access in the attribute
print(honda.color)
# honda.color = "Orange"
# honda.paint_job()
print(honda.color)

# Creating A Library System with OOP
# Book Class
# Libary Class
# Driver Code to prompt the user to interact with the library

# Step 1:
# Define a Book Class
# Attributes title, author, availablity
# Methods for checking out and returning a book, which will update
# its availability

# Step 2:
# Create a Library Class
# store a collection of books - using data structures as class attributes
# include methods to add books and search for a book by title, lend books, and return book

# Step 3
# Driver Code
# While loop with inputs from the user
# Include exception handling to ensure correct user input

# Step 1
class Book(): #physical book copy with book information
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def check_out(self):
        if self.is_available:
            print(f"You succesfully checked out {self.title}")
            self.is_available = False
            return True
        print(f"{self.title} is not available")
        return False
    
    def return_book(self):
        self.is_available = True

# book = Book("Lord of the Rings: The Two Towers", "J.R.R Tolkien")
# print(book.check_out())
# print(book.check_out())
# book.return_book()
# print(book.check_out())
        
# Step 2 
class Library():
    def __init__(self):
        # store instances of the Book class
        self.books = []

    def add_book(self, book):
        # appends a book(parameter) to the self.books atttribute which is a list
        self.books.append(book)

    def find_book(self, title):
        # takes a title as an argument and then checks our list of book objects
        # to see if the title matches a title attribute on one of our books
        for book in self.books:
            if book.title == title:
                # if we find a book that matches, we return the whole book object
                return book
        # if we dont find the book we None
        return None
    def lend_book(self, title):
        # takes title as an argument
        # that we pass into the find_book method to make sure our book exists
        book = self.find_book(title)
        # we set book variable to the output of find_book method
        # which is either going to be the whole book object
        # or None
        if book and book.check_out():
            print(f"Book '{title}' has been lent out!")
        else:
            print(f"'{title}' is not available")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
            print(f"'{title}' has been returned")
        else:
            print(f"{title} not found in the library")

# Step 3
library = Library()

while True:
    action = input("What would you like to do? (add, lend, return, search, exit): ").lower()
    if action == "exit":
        break
    try:
        if action == "add":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            # book = Book(title, author)
            # library.add_book(book)
            library.add_book(Book(title,author))
            print(f"Added book {title}")
        elif action == "lend":
            title = input("Enter a book title to lend: ")
            library.lend_book(title)
        elif action == "return":
            title = input("Which book are you returning?")
            library.return_book(title)
        elif action == "search":
            title = input("Which book are you looking for? ")
            book = library.find_book(title)
            if book:
                availablity = "available" if book.is_available else "not available"
                print(f"{title} by {book.author} is {availablity}")
            else:
                print(f" {title} was not found")   


    except Exception as e:
        print(f"An error occurred: {e}")
print("Closing Library Systems")
print("beep boop beep")
print("Have a nice day!")

# current library doesnt have a way to view a catalog
# create a method in the library class that displays 
# the entire library's catalog
# looping through your books attribute in library and showing the title and author
# for each book object

# update your driver code with the option to view the catalog





















    