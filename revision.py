# // 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# // down from generation to generation. Imagine you're creating an application that
# // records these oral stories and translates them into different languages. The
# // stories vary by length, moral lessons, and the age group they are intended for.
# // Think about how you would model `Story`, `StoryTeller`, and `Translator`
# // objects, and how inheritance might come into play if there are different types of
# // stories or storytellers.
# // pseudo code
# // 1. record stories as objects(length,moral lessons,age-group)
# // 2.Create another class with more attributes for storyteller and translato

# class AncestralStories:
#     def __init__(self, length, moralLessons, ageGroup, title, language):
#         self.length = length
#         self.moralLessons = moralLessons
#         self.ageGroup = ageGroup
#         self.title = title
#         self.language = language

#     def translate_story(self, new_language):
#         if self.language != new_language:
#             return f"The story is translated to {new_language}."
#         else:
#             return "The story is already in this language."

# class StoryTeller(AncestralStories):
#     def __init__(self, name, length, moralLessons, ageGroup, title, language):
#         super().__init__(length, moralLessons, ageGroup, title, language)
#         self.name = name

#     def tell_story(self):
#         print(f"This is a story called {self.title}. It teaches {self.ageGroup} about {self.moralLessons}.")

# story1 = AncestralStories("long", "courage", "children", "The Lion King", "English")
# print(story1.title)
# print(story1.translate_story("Kiswahili"))

# story2 = StoryTeller("Mercy", "short", "Savings", "Youths", "Smart Money Woman", "English")
# print(story2.title)
# story2.tell_story()





# class AncestralStories:
#     def __init__(self, length, moralLessons, ageGroup, title, language):
#         self.length = length
#         self.moralLessons = moralLessons
#         self.ageGroup = ageGroup
#         self.title = title
#         self.language = language

#     def translate_story(self, new_language):
#         if self.language != new_language:
#             return f"The story is translated to {new_language}."
#         else:
#             return "The story is already in this language."


# class StoryTeller(AncestralStories):
#     def __init__(self, name, length, moralLessons, ageGroup, title, language):
#         self.name = name
#         AncestralStories.__init__(self, length, moralLessons, ageGroup, title, language)

#     def tell_story(self):
#         print(f"This is a story called {self.title}. It teaches {self.ageGroup} about {self.moralLessons}.")


# story1 = AncestralStories("long", "courage", "children", "The Lion King", "English")
# print(story1.title)
# print(story1.translate_story("Kiswahili"))

# story2 = StoryTeller("John", "short", "perseverance", "children", "The Tortoise and the Hare", "English")
# print(story2.title)
# story2.tell_story()






# class AncestralStories:
#     def __init__(self, length, moralLessons, ageGroup, title, language):
#         self.length = length
#         self.moralLessons = moralLessons
#         self.ageGroup = ageGroup
#         self.title = title
#         self.language = language

#     def translateStory(self, newLanguage):
#         if self.language != newLanguage:
#            self.language = newLanguage
#            return self.language
#         else:
#             return self.language

#     def addStoryToDatabase(self):
#         database = []
#         if self.title not in database:
#             database.append(self.title)
#             print(database)
#         else:
#             print("This story already exists in storage")

# class StoryTeller(AncestralStories):
#     def __init__(self, length, moralLessons, ageGroup, title, language, name):
#         super().__init__(length, moralLessons, ageGroup, title, language)
#         self.name = name
        
#     def tellstory(self):
#         print(f"This is a story called {self.title}, it teaches {self.ageGroup} about {self.moralLessons}")

# story1 = AncestralStories("long", "courage", "children", "The Lion King", "English")
# story2 = AncestralStories("short", "hardwork", "teenagers", "Vuna Ulichopanda", "Kiswahili")
# print(story1)
# print(story1.translateStory("Kiswahili"))
# story1.addStoryToDatabase()

# abunwasi = StoryTeller("long", "bravery", "Young Adults", "Adventures of Kinjikitile", "Mijikenda", "Abunwasi")
# abunwasi.tellstory()




# class AncestralStories:
#     def __init__(self, length, moral_lessons, age_group, title, language):
#         self.length = length
#         self.moral_lessons = moral_lessons
#         self.age_group = age_group
#         self.title = title
#         self.language = language
#     def translate_story(self, new_language):
#         if self.language != new_language:
#             self.language = new_language
#         return self.language
#     def add_story_to_database(self, database):
#         if self.title not in database:
#             database.append(self.title)
#             print(database)
#         else:
#             print("This story already exists in storage")
# class StoryTeller(AncestralStories):
#     def __init__(self, length, moral_lessons, age_group, title, language, name):
#         super().__init__(length, moral_lessons, age_group, title, language)
#         self.name = name
#     def tell_story(self):
#         print(f"This is a story called {self.title}, it teaches {self.age_group} about {self.moral_lessons}")
# # instances
# database = []
# story = AncestralStories(10, "Unity", "Children", "The Lion and the Mouse", "English")
# database.append(story)
# story_teller = StoryTeller(20, "Courage", "Teenagers", "The Three Musketeers", "English", "John")
# story_teller.tell_story()
# story_teller.translate_story("Spanish")
# print(story_teller.language)




class AncestralStories:
    def __init__(self, length, moralLessons, ageGroup, title, language):
        self.length = length
        self.moralLessons = moralLessons
        self.ageGroup = ageGroup
        self.title = title
        self.language = language
    
    def __str__(self):
       return f"{self.title} is a {self.length} story that teaches {self.moralLessons} to {self.ageGroup} and is written in {self.language} language."


    def translateStory(self, newLanguage):
        
        if self.language != newLanguage:
            self.language = newLanguage
            return self.language
        else:
            return self.language

    def addStoryToDatabase(self):
        database = []
        if self.title not in database:
            database.append(self.title)
            print(database)
        else:
            print("This story already exists in storage")


class StoryTeller(AncestralStories):
    def __init__(self, length, moralLessons, ageGroup, title, language, name):
        super().__init__(length, moralLessons, ageGroup, title, language)
        self.name = name

    def tellStory(self):
        print(f"This is a story called {self.title}. It teaches {self.ageGroup} about {self.moralLessons}.")


story1 = AncestralStories("long", "courage", "children", "The Lion King", "English")
story2 = AncestralStories("short", "hardwork", "teenagers", "Vuna Ulichopanda", "Kiswahili")
print(story1)
print(story1.translateStory("Kiswahili"))
story1.addStoryToDatabase()




# class AncestralStories:
#    def __init__(self, length, moralLessons, ageGroup, title, language):
#        self.length = length
#        self.moralLessons = moralLessons
#        self.ageGroup = ageGroup
#        self.title = title
#        self.language = language

#    def __str__(self):
#        return f"{self.title} is a {self.length} story that teaches {self.moralLessons} to {self.ageGroup} and is written in {self.language} language."





# class Recipe:
#     def __init__(self, name, country, ingredients, prep_time, cooking_method, nutrition_info):
#         self.name = name
#         self.country = country
#         self.ingredients = ingredients
#         self.prep_time = prep_time
#         self.cooking_method = cooking_method
#         self.nutrition_info = nutrition_info

#     def timeForPreparation(self):
#         if self.preparationtime>=3:
#             return f"this cuisine takes a long time to prepare"
        
#         else:
#             return f"This cuisine can be prepared within a reasonable amount of time"
        
    
#     def __str__(self):
#         return f"Name: {self.name}\nCountry: {self.country}\nIngredients: {', '.join(self.ingredients)}\nPrep Time: {self.prep_time} minutes\nCooking Method: {self.cooking_method}\nNutrition Info: {self.nutrition_info}"
        
# class MoroccanRecipe(Recipe):
#     def __init__(self, name, ingredients, prep_time, cooking_method, nutrition_info):
#         super().__init__(name, "Moroccan", ingredients, prep_time, cooking_method, nutrition_info)
        
# class EthiopianRecipe(Recipe):
#     def __init__(self, name, ingredients, prep_time, cooking_method, nutrition_info):
#         super().__init__(name, "Ethiopian", ingredients, prep_time, cooking_method, nutrition_info)
        
# class NigerianRecipe(Recipe):
#     def __init__(self, name, ingredients, prep_time, cooking_method, nutrition_info):
#         super().__init__(name, "Nigerian", ingredients, prep_time, cooking_method, nutrition_info)



# recipe1 = Recipe("Rice beans", "Nigerian", ["Rice", "Tomatoes", "Pepper", "Onions", "Chicken"], 60, "Boiling/Stir-frying", {"Calories": 200, "Fat": 5})
# print(recipe1)

# moroccan_recipe = MoroccanRecipe("chapo beans", ["Lentils", "Tomatoes", "Chickpeas", "Coriander", "Lemon"], 30, "Boiling", {"Calories": 250, "Fat": 3})
# print(moroccan_recipe)
# ethiopian_recipe = EthiopianRecipe("Injera", ["Flour", "Water", "Salt"], 60, "Fermentation", {"Calories": 150, "Fat": 2})
# print(ethiopian_recipe)

# nigerian_recipe = NigerianRecipe("mushroom Soup", ["mushroom", "Meat", "Fish", "Vegetables", "Pepper"], 90, "Boiling", {"Calories": 300, "Fat": 8})
# print(nigerian_recipe)





# class Recipe:
#     def __init__(self,ingredients,cookingmethod,nutritionalinfo):
#         self.ingredients=ingredients
#         # // self.preparationtime=preparationtime;
#         self.cookingmethod=cookingmethod
#         self.nutritionalinfo=nutritionalinfo
    
#     def timeForPreparation():
#         if self.preparationtime>=3:
#             return f"this cuisine takes a long time to prepare"
        
#         else:
#             return f"This cuisine can be prepared within a reasonable amount of time"
        
#  class MoroccanRecipe (Recipe):
#     constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,flavorings){
#         super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
#         this.flavorings = flavorings;
#     }
#  }
#  class EthiopianRecipe extends Recipe{
#     constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,typeOfOilUsed){
#         super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
#         this.typeOfOilUsed = typeOfOilUsed;
#     }
#  }
#  class NigerianRecipe extends Recipe{
#     constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,chilliesUsed){
#         super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
#         this.chilliesUsed = chilliesUsed;
#  }
# }

# recipe1 = Recipe("Rice beans", "Nigerian", ["Rice", "Tomatoes", "Pepper", "Onions", "Chicken"], 60, "Boiling/Stir-frying", {"Calories": 200, "Fat": 5});
# print(recipe1)

# moroccan_recipe = MoroccanRecipe("chapo beans", ["Lentils", "Tomatoes", "Chickpeas", "Coriander", "Lemon"], 30, "Boiling", {"Calories": 250, "Fat": 3})
# print(moroccan_recipe)
# ethiopian_recipe = EthiopianRecipe("Injera", ["Flour", "Water", "Salt"], 60, "Fermentation", {"Calories": 150, "Fat": 2})
# print(ethiopian_recipe)

# const nigerian_recipe = new NigerianRecipe("mushroom Soup", ["mushroom", "Meat", "Fish", "Vegetables", "Pepper"], 90, "Boiling", {"Calories": 300, "Fat": 8})
# console.log(nigerian_recipe)

# class Recipe:
#     def __init__(self, name, country, ingredients, preparation_time, cooking_methods, nutritional_info):
#         self.name = name
#         self.country = country
#         self.ingredients = ingredients
#         self.preparation_time = preparation_time
#         self.cooking_methods = cooking_methods
#         self.nutritional_info = nutritional_info
#     def timeForPreparation(self):
#         if self.preparationtime>=3:
#             return f"this coloured Rice takes a long time to prepare"
#         else:
#             return f"This coloured Rice  can be prepared within a reasonable amount of time"
#     def __str__(self):
#         return f"Name: {self.name}\ncountry: {self.country}\ningredients: {', '.join(self.ingredients)}\npreparation_time: {self.prep_time} minutes\ncooking_method: {self.cooking_method}\nnutrition_info: {self.nutrition_info}"
# class MoroccanRecipe(Recipe):
#     def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
#         super().__init__(name, "Morocco", ingredients, preparation_time, cooking_method, nutritional_info)
#         self.spice_level = spice_level
# class EthiopianRecipe(Recipe):
#     def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, injera_included):
#         super().__init__(name, "Ethiopia", ingredients, preparation_time, cooking_method, nutritional_info)
#         self.injera_included = injera_included
# class NigerianRecipe(Recipe):
#     def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, is_spicy):
#         super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method, nutritional_info)
#         self.is_spicy = is_spicy
# # Instances
# moroccan_recipe = MoroccanRecipe("Coloured Rice",["rice", "onion", "olive oil", "spices"],45,"Boiled ","Nice for vitamins","Medium")
# print(moroccan_recipe)

# ethiopian_recipe = EthiopianRecipe("Boiled eggs",["eggs","water"],20,"protein","no spicies",True)
# print(ethiopian_recipe)

# nigerian_recipe = NigerianRecipe("Jollof Rice",["rice", "tomatoes", "onion", "pepper", "spices"],45,"Popular party dish",'is_spicy',True)
# print(nigerian_recipe)

class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_methods, nutritional_info):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_methods = cooking_methods
        self.nutritional_info = nutritional_info
    
    def timeForPreparation(self):
        if self.preparation_time >= 3:
            return "This coloured Rice takes a long time to prepare"
        else:
            return "This coloured Rice can be prepared within a reasonable amount of time"
    
    def __str__(self):
        return f"Name: {self.name}\ncountry: {self.country}\ningredients: {', '.join(self.ingredients)}\npreparation_time: {self.preparation_time} minutes\ncooking_method: {self.cooking_methods}\nnutrition_info: {self.nutritional_info}"

class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
        super().__init__(name, "Morocco", ingredients, preparation_time, cooking_method, nutritional_info)
        self.spice_level = spice_level
    def is_spiucy(self):
       if self.spice_level > 5:
          return f"The moroccanRecipe has a lot of spice"
       else:
          return f"The moroccanRecipe has no spice"

class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, injera_included):
        super().__init__(name, "Ethiopia", ingredients, preparation_time, cooking_method, nutritional_info)
        self.injera_included = injera_included

class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, is_spicy):
        super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method, nutritional_info)
        self.is_spicy = is_spicy
    def check_spice(self,food):
       if self.food== self.is_spicy:
          return f"nigerian food is bitter due to high level of spices"
       else:
          return f"{self.food} is not spicy"


moroccan_recipe = MoroccanRecipe("Coloured Rice",["rice", "onion", "olive oil", "spices"],45,"Boiled ","Nice for vitamins","Medium")
print(moroccan_recipe)

ethiopian_recipe = EthiopianRecipe("Boiled eggs",["eggs","water"],20,"protein","no spicies",True)
print(ethiopian_recipe)

nigerian_recipe = NigerianRecipe("Jollof Rice",["rice", "tomatoes", "onion", "pepper", "spices"],45,"Popular party dish",'is_spicy',True)
print(nigerian_recipe)


# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

class Species:
  def __init__(self, name, diet, lifespan, migration_pattern):
    self.name = name
    self.diet = diet
    self.lifespan = lifespan
    self.migration_pattern = migration_pattern
  
  def get_info(self):
    print(f"Name: {self.name}\nDiet: {self.diet}\nLifespan: {self.lifespan}\nMigration Pattern: {self.migration_pattern}")
    
  def is_extinct(self):
    if self.lifespan == 0:
      return True
    else:
      return False

class Predator(Species):
  def __init__(self, name, diet, lifespan, migration_pattern, hunting_style):
    super().__init__(name, diet, lifespan, migration_pattern)
    self.hunting_style = hunting_style
    
  def get_info(self):
    super().get_info()
    print(f"Hunting Style: {self.hunting_style}")
    
  def top_canivore(self):
    if self.diet == "Carnivore" and self.lifespan >= 10:
      return f"the carnivore animal has has a long lifespan"
    elif self.diet == "Carnivore" and self.lifespan <= 10:
      return f"the carnivore anmal has a short lifespan"
    else:
       return False

class Prey(Species):
  def __init__(self, name, diet, lifespan, migration_pattern, predator_avoidance):
    super().__init__(name, diet, lifespan, migration_pattern)
    self.predator_avoidance = predator_avoidance
    
  def get_info(self):
    super().get_info()
    print(f"Predator Avoidance: {self.predator_avoidance}")
    
  def is_prolific(self):
    if self.lifespan <= 5:
      return True
    else:
      return False



species1 = Species("Lion", "Carnivore", 15, "Non-migrant")
species1.get_info()

predator1 = Predator("Tiger", "Carnivore", 20, "Non-migrant", "Ambush")
predator1.get_info()


prey1 = Prey("Gazelle", "Herbivore", 5, "Migrant", "Speed")
prey1.get_info()



class Species:
   def __init__(self, name, diet, lifespan):
       self.name = name
       self.diet = diet
       self.lifespan = lifespan
   def endangered_species(self):
       if self.lifespan <= 50:
           return "Species is endangered"
       else:
           return "Species is extinct"
class Predator(Species):
   def __init__(self, name, diet, lifespan, hunting_method):
       super().__init__(name, diet, lifespan)
       self.hunting_method = hunting_method
   def dangerous(self):
       if self.hunting_method in ["stalk", "pounce", "chase"]:
           return f"Predator is carnivore and feeds on {self.diet}"
       else:
           return f"Predator is herbivore and feeds on {self.diet}"
class Prey(Species):
   def __init__(self, name, diet, lifespan):
       super().__init__(name, diet, lifespan)
   def migration(self, need):
       if need == "food":
           return f"{self.name} migration is seasonal"
       elif need == "reproduction":
           return f"{self.name} is migrating in July"
       
lion = Predator("Lion", "meat", 15, "chase")
print(lion.dangerous())
gazelle = Prey("Gazelle", "grass", 10)
print(gazelle.migration("food"))
elephant = Species("Elephant", "plants", 70)
print(elephant.endangered_species())
elephant = Prey("Elephant", "plants", 70)
print(elephant.migration("reproduction"))





# class Species:
#     def __init__(self, diet, typical_lifespan, migration_patterns):
#         self.diet = diet
#         self.typical_lifespan = typical_lifespan
#         self.migration_patterns = migration_patterns
        
#     def type_of_animal(self):
#         if self.diet == "herbivorous":
#             print("This animal is not a danger to other animals")
#         elif self.diet == "omnivorous":
#             print("This animal feeds on plants but also feeds on some animals")
#         else:
#             print("This animal is very dangerous to other animals and does not eat plants")

# class Predator(Species):
#     def __init__(self, diet, typical_lifespan, migration_patterns, number_of_canines, claws, venom, name):
#         super().__init__(diet, typical_lifespan, migration_patterns)
#         self.number_of_canines = number_of_canines
#         self.claws = claws
#         self.venom = venom
#         self.name = name
        
#     def fast_killers(self):
#         if self.venom:
#             print(f"The bite of a {self.name} kills within hours")
#         else:
#             print(f"The bite of a {self.name} is not deadly")
            
#     def method_of_killing(self):
#         pass

# class Prey(Species):
#         def __init__(self, diet, typical_lifespan, migration_patterns, defense_mechanisms, name):
#             super().__init__(diet, typical_lifespan, migration_patterns)
#             self.defense_mechanisms = defense_mechanisms
#             self.name = name

class Species:
    def __init__(self, diet, typical_lifespan, migration_patterns):
        self.diet = diet
        self.typical_lifespan = typical_lifespan
        self.migration_patterns = migration_patterns

    def type_of_animal(self):
        if self.diet == "herbivorous":
            print("This animal is not a danger to other animals")
        elif self.diet == "omnivorous":
            print("This animal feeds on plants but also feeds on some animals")
        else:
            print("This animal is very dangerous to other animals and does not eat plants")


class Predator(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns, number_of_canines, claws, venom, name):
        super().__init__(diet, typical_lifespan, migration_patterns)
        self.number_of_canines = number_of_canines
        self.claws = claws
        self.venom = venom
        self.name = name

    def fast_killers(self):
        if self.venom:
            print(f"The bite of a {self.name} kills within hours")
        else:
            print(f"The bite of a {self.name} is not deadly")

    def method_of_killing(self):
        print("This predator uses its sharp claws and teeth to attack and kill its prey.")


class Prey(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns, defense_mechanisms, name):
        super().__init__(diet, typical_lifespan, migration_patterns)
        self.defense_mechanisms = defense_mechanisms
        self.name = name

    def defense(self):
     if "camouflage" in self.defense_mechanisms:
            print(f"The {self.name} uses camouflage to blend with its surroundings and hide from predators.")
     else:
         print(f"The pray {self.name} cannot defend itself")

elephant = Species("herbivorous", 60, "non-migratory")
elephant.type_of_animal()

lion = Predator("carnivorous", 12, "non-migratory", 2, True, True, "lion")
lion.fast_killers()
lion.method_of_killing()

gazelle = Prey("herbivorous", 10, "migratory", ["camouflage"], "gazelle")
gazelle.defense()


# class Species:
#     def __init__(self, diet, typical_lifespan, migration_patterns):
#         self.diet = diet
#         self.typical_lifespan = typical_lifespan
#         self.migration_patterns = migration_patterns
#     def type_of_animal(self):
#         if self.diet == "herbivorous":
#             print("This animal is not a danger to other animals")
#         elif self.diet == "omnivorous":
#             print("This animal feeds on plants but also feeds on some animals")
#         else:
#             print("This animal is very dangerous to other animals and does not eat plants")
# class Predator(Species):
#     def __init__(self, diet, typical_lifespan, migration_patterns, type_of_teeth, claws, venom, name):
#         super().__init__(diet, typical_lifespan, migration_patterns)
#         self.type_of_teeth = type_of_teeth
#         self.claws = claws
#         self.venom = venom
#         self.name = name
#     def fast_killers(self):
#         if self.venom:
#             print(f"The bite of a {self.name} kills within hours")
#         else:
#             print(f"The bite of a {self.name} is not deadly")
#     def method_of_killing(self):
#         if "carnassial teeth" in self.type_of_teeth:
#             print(f"A {self.name} kills by slicing up their prey")
#         else:
#             print("This predator cannot shear their prey's meat after attacks")
# class Prey(Species):
#     def __init__(self, diet, typical_lifespan, migration_patterns, defense_mechanisms, name):
#         super().__init__(diet, typical_lifespan, migration_patterns)
#         self.defense_mechanisms = defense_mechanisms
#         self.name = name
#     def defense(self):
#      if "camouflage" in self.defense_mechanisms:
#             print(f"The {self.name} uses camouflage to blend with its surroundings and hide from predators.")
#      else:
#          print(f"The pray {self.name} cannot defend itself")
# # instances
# lion = Predator("carnivorous", 12, "non-migratory", ["carnassial teeth"], True, False, "Lion")
# gazelle = Prey("herbivorous", 10, "seasonal migration", ["speed", "herd behavior"], "Gazelle")
# lion.type_of_animal()
# lion.fast_killers()
# lion.method_of_killing()
# gazelle.type_of_animal()
# print(gazelle.defense_mechanisms)


# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.

class Artist:
    def __init__(self, name, country, style, instruments):
        self.name = name
        self.country = country
        self.style = style
        self.instruments = instruments
        self.performances = []

    def add_performance(self, performance):
        for p in self.performances:
            if p.start_time < performance.start_time + performance.duration and performance.start_time < p.start_time + p.duration:
                print("Artist already has a performance at this time.")
                return False
        self.performances.append(performance)
        return True

    def remove_performance(self, performance):
        if performance in self.performances:
            self.performances.remove(performance)
            return True
        else:
            print("Performance not found for this artist.")
            return False

    def update_info(self, name=None, country=None, style=None, instruments=None):
        if name:
            self.name = name
        if country:
            self.country = country
        if style:
            self.style = style
        if instruments:
            self.instruments = instruments


class Performance(Artist):
    def __init__(self, artist, start_time, duration):
        self.artist = artist
        self.start_time = start_time
        self.duration = duration
        self.stage = None

    def assign_stage(self, stage):
        if stage.capacity < len(stage.performances) + 1:
            print("Stage is at full capacity.")
            return False
        for p in stage.performances:
            if p.start_time < self.start_time + self.duration and self.start_time < p.start_time + p.duration:
                print("Performance overlaps with another performance on this stage.")
                return False
        self.stage = stage
        stage.performances.append(self)
        return True

    def unassign_stage(self):
        if self.stage:
            self.stage.performances.remove(self)
            self.stage = None
            return True
        else:
            print("Performance is not assigned to a stage.")
            return False

class SoloPerformance(Performance):
    def __init__(self, artist, start_time, duration):
        super().__init__(artist, start_time, duration)

    def __str__(self):
        return f"{self.artist.name} | {self.start_time} - {self.duration}"


class Stage(Artist):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.performances = []


# creating an instance of Artist class
artist1 = Artist("John", "USA", "Rock", ["Guitar", "Drums"])

# creating an instance of Performance class with artist1
performance1 = Performance(artist1, "2023-07-01 20:00:00", 120)

# creating an instance of Stage class
stage1 = Stage("Main Stage", 1000)


# artist = Artist("Femi Kuti", "Nigeria", "Afrobeat", ["Saxophone", "Trumpet"])
# performance = SoloPerformance(artist, "17:00", "1 hour")
# stage = Stage("Main Stage", 5) 
# performance.assign_stage(stage)
# artist.add_performance(performance)
# print(f"Artist: {artist.name}")
# for p in artist.performances:
#     print(p)
# performance.unassign_stage()
# artist.remove_performance(performance)


# class Artist:
#     def __init__(self, name, country, style, instruments):
#         self.name = name
#         self.country = country
#         self.style = style
#         self.instruments = instruments
#         self.performances = []

#     def add_performance(self, performance):
#         for p in self.performances:
#             if p.start_time < performance.start_time + performance.duration and performance.start_time < p.start_time + p.duration:
#                 print("Error: Artist already has a performance at this time.")
#                 return False
#         self.performances.append(performance)
#         return True

#     def remove_performance(self, performance):
#         if performance in self.performances:
#             self.performances.remove(performance)
#             return True
#         else:
#             print("Performance not found for this artist.")
#             return False

#     def update_info(self, name=None, country=None, style=None, instruments=None):
#         if name:
#             self.name = name
#         if country:
#             self.country = country
#         if style:
#             self.style = style
#         if instruments:
#             self.instruments = instruments

# class Performance:
#     def __init__(self, artist, start_time, duration):
#         self.artist = artist
#         self.start_time = start_time
#         self.duration = duration
#         self.stage = None

#     def assign_stage(self, stage):
#         if stage.capacity < len(stage.performances) + 1:
#             print("Stage is at full capacity.")
#             return False
#         for p in stage.performances:
#             # Check if the stage has overlapping performances
#             if p.start_time < self.start_time + self.duration and self.start_time < p.start_time + p.duration:
#                 print("Performance overlaps with another performance on this stage.")
#                 return False
#         self.stage = stage
#         stage.performances.append(self)
#         return True

#     def unassign_stage(self):
#         if self.stage:
#             self.stage.performances.remove(self)
#             self.stage = None
#             return True
#         else:
#             print("Performance is not assigned to a stage.")
#             return False

# class SoloPerformance(Performance):
#     def __init__(self, artist, start_time, duration):
#         super().__init__(artist, start_time, duration)
       



# # Create an artist
# artist = Artist("Femi Kuti", "Nigeria", "Afrobeat", ["Saxophone", "Trumpet"])
# artist.add_performance()

# # Create a solo performance for the artist
# performance = SoloPerformance(artist, "17:00", "1 hour")
# artist.add_performance()

# # Create a stage
# stage = Stage("Main Stage", 5)  # Assuming the stage capacity is 5

# # Assign the performance to the stage
# performance.assign_stage(stage)

# # Add the performance to the artist's list of performances
# artist.add_performance(performance)

# # Print the artist's performances
# print(f"Artist: {artist.name}")
# for p in artist.performances:
#     print(p)

# # Remove the performance from the stage
# performance.unassign_stage()

# # Remove the performance from the artist's list of performances
# artist.remove_performance(performance)


# artist1 = Artist("John Smith", "United States", "Rock", ["guitar", "vocals"])

# performance1 = Performance(artist1, "2023-07-01 20:00:00", 90)



# class Artist:
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country

#     def __str__(self):
#         return f"{self.name} ({self.country})"


# class Performance:
#     def __init__(self, artist, start_time, end_time):
#         self.artist = artist
#         self.start_time = start_time
#         self.end_time = end_time

#     def __str__(self):
#         return f"{self.artist} | {self.start_time} - {self.end_time}"


# class Stage:
#     def __init__(self, name):
#         self.name = name
#         self.performances = []

#     def add_performance(self, performance):
#         self.performances.append(performance)

#     def remove_performance(self, performance):
#         self.performances.remove(performance)

#     def get_all_performances(self):
#         return self.performances

#     def get_performances_by_artist(self, artist):
#         return [p for p in self.performances if p.artist == artist]

#     def __str__(self):
#         stage_info = f"Stage: {self.name}\n"
#         performances_info = "\n".join(str(p) for p in self.performances)
#         return stage_info + performances_info



# class Artist:
#     def __init__(self, artist_name, country, musical_style, instrument):
#         self.artist_name = artist_name
#         self.country = country
#         self.musical_style = musical_style
#         self.instrument = instrument

#     def display_music(self):
#         if self.artist_name == "Mercy" and self.country == "Kenya":
#             return f"{self.artist_name} is from {self.country} has {self.musical_style} style of music and uses {self.instrument} to play her music"
#         else:
#             return "None"


# artist = Artist("Mercy", "Kenya", "Afrobeat", "guitar")
# music_details = artist.display_music()
# print(music_details)




# Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def calculate_total_value(self):
#         return self.price * self.quantity

# # Creating multiple objects of Product class
# productA = Product('Laptop', 15000, 2)
# productB = Product('Phones', 10000, 2)
# productC = Product('Television', 18000, 2)

# # Calculating total value of all products
# total_value = productA.calculate_total_value() + productB.calculate_total_value() + productC.calculate_total_value()

# print(f'The total value of all products is {total_value}.')
class Flight:
    def __init__(self, id, destination, date):
        self.id = id
        self.destination = destination
        self.date = date

class FlightBooking:
    def __init__(self):
        self.flights = []
        self.bookings = {}

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.destination == destination and flight.date == date:
                available_flights.append(flight)
        return available_flights

    def reserve_seat(self, flight_id, passenger_name):
        if flight_id in self.bookings:
            self.bookings[flight_id].append(passenger_name)
        else:
            self.bookings[flight_id] = [passenger_name]

    def get_booking_confirmation(self, flight_id):
        if flight_id in self.bookings:
            passengers = self.bookings[flight_id]
            flight = next((flight for flight in self.flights if flight.id == flight_id), None)
            if flight:
                confirmation = f"Booking Confirmation\nFlight: {flight}\nPassengers: {', '.join(passengers)}"
                return confirmation
        return "No booking found for the given flight ID"


# Create an instance of FlightBooking
flight_booking = FlightBooking()

# Create some flights
flight1 = Flight(1, "New York", "2023-07-10")
flight2 = Flight(2, "London", "2023-07-12")
flight3 = Flight(3, "Paris", "2023-07-15")

# Add flights to the booking system
flight_booking.add_flight(flight1)
flight_booking.add_flight(flight2)
flight_booking.add_flight(flight3)

# Search for available flights
available_flights = flight_booking.search_flights("London", "2023-07-12")



# class FlightBooking:
#     def __init__(self):
#         self.flights = {}  # flights are stored in a dictionary

#     def search_flights(self, destination, date):
#         # search for available flights based on destination and date
#         # returns a list of available flights
#         available_flights = []
#         for flight in self.flights.values():
#             if flight.destination == destination and flight.date == date and not flight.is_full():
#                 available_flights.append(flight)
#         return available_flights

#     def reserve_seat(self, flight, customer):
#         # reserve a seat for a customer on a given flight
#         if not flight.is_full():
#             flight.add_passenger(customer)

#     def get_passenger_info(self, flight):
#         # get passenger information for a given flight
#         return flight.passengers

#     def generate_confirmation(self, flight, customer):
#         # generate a booking confirmation for a given flight and customer
#         confirmation_number = len(flight.passengers)  # use number of passengers as confirmation number
#         return f"Booking confirmation for flight {flight.number}\nConfirmation number: {confirmation_number}\nPassenger name: {customer.name}\nSeat number: {customer.seat_number}"

# class Flight:
#     def __init__(self, number, destination, date, capacity):
#         self.number = number
#         self.destination = destination
#         self.date = date
#         self.capacity = capacity
#         self.passengers = []

#     def is_full(self):
#         return len(self.passengers) == self.capacity

#     def add_passenger(self, customer):
#         self.passengers.append(customer)

# class Customer:
#     def __init__(self, name, seat_number):
#         self.name = name
#         self.seat_number = seat_number

# # create a new instance of FlightBooking
# booking_system = FlightBooking()

# # add some flights to the booking system
# flight1 = Flight("101", "New York", "2023-08-15", 50)
# flight2 = Flight("102", "London", "2023-08-17", 60)

# booking_system.flights[flight1.number] = flight1
# booking_system.flights[flight2.number] = flight2



# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def calculateTotalValue(self):
#         return self.price * self.quantity
    
#     def getInfo(self):
#         totalValue = self.calculateTotalValue()
#         return f"{self.name} - Total Value: {totalValue}"
    

# products = [
#     Product('Laptop', 15000, 2),
#     Product('Phones', 10000, 2),
#     Product('Television', 18000, 2)
# ]

# totalValue = 0
# for product in products:
#     totalValue += product.calculateTotalValue()
    
# print(f"The total value of all products is {totalValue}")


        








