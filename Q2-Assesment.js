// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.


//  input> Story, StoryTeller, Translator`
//  output> creating an application that records these oral stories and translates them into different languages
//  process> create a class passs in the attributes, create a method


class AncestralStories{
    constructor(this, Story,StoryTeller,Translator){
        this.Story=Story
        this.StoryTeller=StoryTeller
        this.Translator=Translator
    }
}
    // checkStory extends AncestralStories(){
    //    return("{self.Story} which is of {length} narrated by {self.StoryTeller} is {self.Translator} into different languages which has {moral_lesson} suitable to different{age_group}")
        
    // check_story(age);{
    //    return "the story is for different (age) groups"
    // }
    // }



strory=new AncestralStories("honey_burger",5)
console.log(checkStory())







// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.




// **African Music Festival:** You're in charge of organizing a Pan-African music
// festival. Many artists from different countries, each with their own musical style
// and instruments, are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.



// # Create a class called Product with attributes for name, price, and quantity.
// # Implement a method to calculate the total value of the product (price * quantity).
// # Create multiple objects of the Product class and calculate their total values.

class Product{
    constructor(this,name,price,quantity){
        this.name=name
        this.price=price
        this.quantity=quantity
    }
}
    calculate_tital_value(self);{
        return "{this.price} * {this.quantity}"
    }
    


// # 6. Implement a class called Student with attributes for name, age, and grades (a
// # list of integers). Include methods to calculate the average grade, display the
// # student information, and determine if the student has passed (average grade >=
// # 60). Create objects for the Student class and demonstrate the usage of these
// # methods.

class Student{
    constructor(this,name,age,grade){
        this.name=name
        this.age=age
        this.grade=[]
    }
}
    grade=[]
    students_grade=[60,30,50,80]
    grade.append(students_grade)

    
    calculate_avarage_grade();{
        avarage_grade=("sum {this.greade}/4")
        if (avarage_grade>=60)
            return 'the student {self.name} has passed'
        else{
            return 'the student {self.name} has failed'
        }
    }

    





// # 7. Create a FlightBooking class that represents a flight booking system. Implement
// # methods to search for available flights based on destination and date, reserve
// # seats for customers, manage passenger information, and generate booking
// # confirmations.
class FlightBooking{
    constractor(this,destination, date){
        this.destination=destination
        this.date=date
    }

}
    
    search_available_flights();{
        if("flight for flights {this.destination} is available on {this.date}"){
            return 'the flight is available'
        }
        else{
            return "no flight is available"
        }
    }
        
    reserave_seat(self,customer);{
        if("flight for flights {self.destination} is available on {self.date}"){
            return 'reserve a seat for {customer}'
        }
        else{
            return 'dont researve a seat for {customer}'
        }
    }
        
    manage_passanger_information(name,age);{
        if("passanger for passangers is going to {self.destination} in this flight"){
            return 'the passanger {name} who is {age} is on the flight'
        }
        else{
            return 'the passanger {name} who is {age} is not on the flight'
        }
    }






// # 8. Create a LibraryCatalog class that handles the cataloging and management of
// # books in a library. Implement methods to add new books, search for books by
// # title or author, keep track of available copies, and display book details.