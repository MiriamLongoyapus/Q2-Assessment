# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.


# input> Story, StoryTeller, Translator`
# output> creating an application that records these oral stories and translates them into different languages
# process> create a class passs in the attributes, create a method
# class AncestralStories:
#     def __init__(self, Story,StoryTeller,Translator):
#         self.Story=Story
#         self.StoryTeller=StoryTeller
#         self.Translator=Translator

#     def __str__(self,length,moral_lesson,age_group):
#         print(f"{self.Story} which is of {length} narrated by {self.StoryTeller} is {self.Translator} into different languages which has {moral_lesson} suitable to different{age_group}")
    
#     def check_story(self,age):
#         strory="the story is for different {self.age} groups"



# strory=("honey_burger",5)
# strory.check_story()







# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.



# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.






# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.




# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculate_tital_value(self):
        return f"{self.price} * {self.quantity}"
    


# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=[]
    grade=[]
    students_grade=[60,30,50,80]
    # students_grade2=[70,30,50,60]
    # students_grade3=[40,30,50,50]
    grade.append(students_grade)
    
    def calculate_avarage_grade(self):
        avarage_grade=("sum {self.greade}/4")
        if avarage_grade>=60:
            return f'the student {self.name} has passed'
        else:
            return f'the student {self.name} has failed'

    





# 7. Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.
class FlightBooking:
    def __init__(self,destination, date):
        self.destination=destination
        self.date=date
    
    def search_available_flights(self):
        if("flight for flights {self.destination} is available on {self.date}"):
            return f'the flight is available'
        else:
            return f"no flight is available"
        
    def reserave_seat(self,customer):
        if("flight for flights {self.destination} is available on {self.date}"):
            return f'reserve a seat for {customer}'
        else:
            return f'dont researve a seat for {customer}'
        
    def manage_passanger_information(self,name,age):
        if("passanger for passangers is going to {self.destination} in this flight"):
            return f'the passanger {name} who is {age} is on the flight'
        else:
            return f'the passanger {name} who is {age} is not on the flight'






# 8. Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.