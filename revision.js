class AncestralStories{
    constructor(length,moralLessons,ageGroup,title,language){
        this.length=length;
        this.moralLessons=moralLessons;
        this.ageGroup=ageGroup;
        this.title=title;
        this.language=language;
    }
    translateStory(newLanguage){
        if(this.language !== newLanguage){
            return this.language = newLanguage
        }
        else{
            return this.language
        }
    }
    addStoryToDatabase() {
        let database = []
            if(!database.includes(this.title)){
                database.push(this);
                console.log(database);
            }
            else{
                console.log("This story already exists in storage");
            }
        }
      }
class StoryTeller extends AncestralStories{
    constructor(length,moralLessons,ageGroup,title,language,name){
        super(length,moralLessons,ageGroup,title,language)
        this.name=name;
    }
    tellstory(){
        console.log(`This is a story called ${this.title}, it teaches ${this.ageGroup} about ${this.moralLessons}`);
    }
}
let story1 = new AncestralStories("long","courage","children","The Lion King","English");
let story2 = new AncestralStories("short","hardwork","teenagers","Vuna Ulichopanda","Kiswahili")
console.log(story1);
console.log(story1.translateStory("Kiswahili"));
story1.addStoryToDatabase()
let abunwasi = new StoryTeller("long","bravery","Young Adults","Adventures of Kinjikitile","Mijikenda","Abunwasi");
console.log(abunwasi);
abunwasi.tellstory()




// class Recipe {
//     constructor(name, country, ingredients, prep_time, cooking_method, nutrition_info) {
//         this.name = name;
//         this.country = country;
//         this.ingredients = ingredients;
//         this.prep_time = prep_time;
//         this.cooking_method = cooking_method;
//         this.nutrition_info = nutrition_info;
//     }
// }

// class MoroccanRecipe extends Recipe {
//     constructor(name, ingredients, prep_time, cooking_method, nutrition_info) {
//         super(name, "Moroccan", ingredients, prep_time, cooking_method, nutrition_info);
//     }
// }

// class EthiopianRecipe extends Recipe {
//     constructor(name, ingredients, prep_time, cooking_method, nutrition_info) {
//         super(name, "Ethiopian", ingredients, prep_time, cooking_method, nutrition_info);
//     }
// }

// class NigerianRecipe extends Recipe {
//     constructor(name, ingredients, prep_time, cooking_method, nutrition_info) {
//         super(name, "Nigerian", ingredients, prep_time, cooking_method, nutrition_info);
//     }
// }

// const recipe1 = new Recipe("Jollof Rice", "Nigerian", ["Rice", "Tomatoes", "Pepper", "Onions", "Chicken"], 60, "Boiling/Stir-frying", {"Calories": 200, "Fat": 5});
// console.log(recipe1)

// const moroccan_recipe = new MoroccanRecipe("Harira", ["Lentils", "Tomatoes", "Chickpeas", "Coriander", "Lemon"], 30, "Boiling", {"Calories": 250, "Fat": 3})
// console.log(moroccan_recipe)
// const ethiopian_recipe = new EthiopianRecipe("Injera", ["Flour", "Water", "Salt"], 60, "Fermentation", {"Calories": 150, "Fat": 2})
// console.log(ethiopian_recipe)

// const nigerian_recipe = new NigerianRecipe("Egusi Soup", ["Egusi", "Meat", "Fish", "Vegetables", "Pepper"], 90, "Boiling", {"Calories": 300, "Fat": 8})
// console.log(nigerian_recipe)


class Recipe{
    constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo){
        this.ingredients=ingredients;
        this.preparationtime=preparationtime;
        this.cookingmethod=cookingmethod;
        this.nutritionalinfo=nutritionalinfo;
    }
    timeForPreparation(){
        if(this.preparationtime>=3){
            console.log("this cuisine takes a long time to prepare")
        }
        else{
            console.log("This cuisine can be prepared within a reasonable amount of time");
        }
    }
}
 class MoroccanRecipe extends Recipe{
    constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,flavorings){
        super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
        this.flavorings = flavorings;
    }
 }
 class EthiopianRecipe extends Recipe{
    constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,typeOfOilUsed){
        super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
        this.typeOfOilUsed = typeOfOilUsed;
    }
 }
 class NigerianRecipe extends Recipe{
    constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,chilliesUsed){
        super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
        this.chilliesUsed = chilliesUsed;
 }
}

const recipe1 = new Recipe(["Rice", "Tomatoes", "Pepper", "Onions", "Chicken"],60, "Boiling/Stir-frying","cabohydtrates");
console.log(recipe1)

const moroccan_recipe = new MoroccanRecipe(["Lentils", "Tomatoes", "Chickpeas", "Coriander", "Lemon"], 30, "Boiling","Proteina","Cumin")
console.log(moroccan_recipe)
const ethiopian_recipe = new EthiopianRecipe(["Flour", "Water", "Salt"], 60, "Fermentation", "Proteins", "Fresh fry")
console.log(ethiopian_recipe)

const nigerian_recipe = new NigerianRecipe(["mushroom", "Meat", "Fish", "Vegetables", "Pepper"], 90, "dry-fry","Fight Germs", "Red chillie")
console.log(nigerian_recipe)

// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.

// class Species {
//     constructor(diet, typicalLifespan, migrationPatterns) {
//       this.diet = diet;
//       this.typicalLifespan = typicalLifespan;
//       this.migrationPatterns = migrationPatterns;
//     }
  
//     typeOfAnimal() {
//       if (this.diet === "herbivorous") {
//         console.log("This animal is not a danger to other animals");
//       } else if (this.diet === "omnivorous") {
//         console.log("This animal feeds on plants but also feeds on some animals");
//       } else {
//         console.log("This animal is very dangerous to other animals and does not eat plants");
//       }
//     }
//   }
  
//   class Predator extends Species {
//     constructor(diet, typicalLifespan, migrationPatterns, numberOfCanines, claws, venom, name) {
//       super(diet, typicalLifespan, migrationPatterns);
//       this.numberOfCanines = numberOfCanines;
//       this.claws = claws;
//       this.venom = venom;
//       this.name = name;
//     }
  
//     fastKillers() {
//       if (this.venom === true) {
//         console.log(`The bite of a ${this.name} kills within hours`);
//       } else {
//         console.log(`The bite of a ${this.name} is not deadly`);
//       }
//     }
  
//     methodOfKilling() {
//       console.log("This predator uses its sharp claws and teeth to attack and kill its prey.");
//     }
//   }
  
//   class Prey extends Species {
//     constructor(diet, typicalLifespan, migrationPatterns, defenseMechanisms, name) {
//       super(diet, typicalLifespan, migrationPatterns);
//       this.defenseMechanisms = defenseMechanisms;
//       this.name = name;
//     }
  
//     defense() {
//       console.log(`The ${this.name} uses ${this.defenseMechanisms} to protect itself from predators.`);
//     }
//   }
  
//   const elephant = new Species("herbivorous", 60, "non-migratory");
// elephant.typeOfAnimal(); // This animal is not a danger to other animals

// const lion = new Predator("carnivorous", 12, "non-migratory", 2, true, true, "lion");
// lion.fastKillers(); // The bite of a lion kills within hours
// lion.methodOfKilling(); // This predator uses its sharp claws and teeth to attack and kill its prey.

// const gazelle = new Prey("herbivorous", 8, "migratory", "speed and agility", "gazelle");
// gazelle.defense(); // The gazelle uses speed and agility to protect itself from predators.



// class Species{
//     constructor(diet,typicalLifespan,migrationPatterns){
//         this.diet =diet;
//         this.typicalLifespan = typicalLifespan;
//         this.migrationPatterns = migrationPatterns;
//     }
//     typeOfAnimal(){
//         if(this.diet === "herbivorous"){
//             console.log("This animal is not a danger to other animals");
//         }
//         else if(this.diet === "omnivorous"){
//             console.log("This animal feeds on plants but also feeds on aome animals");
//         }
//         else{
//             console.log("This animal is very dangerous to other animals and does not eat plants");
//         }
//     }
// }
// class Predator extends Species{
//     constructor(diet,typicalLifespan,migrationPatterns,numberOfCanines,claws,venom,name){
//     super(diet,typicalLifespan,migrationPatterns)
//         this.numberOfCanines = numberOfCanines;
//         this.claws = claws;
//         this.venom = venom;
//         this.name = name;
//     }
//     fastKillers(){
//         if(this.venom === true){
//             console.log(`The bite of a ${this.name} kills within hours`);
//         }
//         else{
//             console.log(`The bite of a ${this.name} is not deadly`);
//         }
//     }
//     methodOfKilling(){
//         if(this.clawa==sharp){
//             console.log("This predator uses its sharp claws to attack and kill its prey.");
//         }
//         else{
//             console.log("This predator uses its sharp claws to attack and kill its prey.");

//         }
//         }
//     }

// class Prey extends Species{
//     constructor(diet,typicalLifespan,migrationPatterns,defenseMechanisms,name){
//     super(diet,typicalLifespan,migrationPatterns)
//         this.defenseMechanisms = defenseMechanisms;
//         this.name = name;
//     }
// }

// class Species{
//     constructor(diet,typicalLifespan,migrationPatterns){
//         this.diet =diet;
//         this.typicalLifespan = typicalLifespan;
//         this.migrationPatterns = migrationPatterns;
//     }
//     typeOfAnimal(){
//         if(this.diet === "herbivorous"){
//             console.log("This animal is not a danger to other animals");
//         }
//         else if(this.diet === "omnivorous"){
//             console.log("This animal feeds on plants but also feeds on aome animals");
//         }
//         else{
//             console.log("This animal is very dangerous to other animals and does not eat plants");
//         }
//     }
// }
// class Predator extends Species{
//     constructor(diet,typicalLifespan,migrationPatterns,typeOfTeeth,claws,venom,name){
//     super(diet,typicalLifespan,migrationPatterns)
//         this.typeOfTeeth = typeOfTeeth;
//         this.claws = claws;
//         this.venom = venom;
//         this.name = name;
//     }
//     fastKillers(){
//         if(this.venom === true){
//             console.log(`The bite of a ${this.name} kills within hours`);
//         }
//         else{
//             console.log(`The bite of a ${this.name} is not deadly`);
//         }
//     }
//     methodOfKilling(){
//         if(this.typeOfTeeth.includes("carnassial teeth")){
//             console.log(`A ${this.name} kills by slicing up their prey`);
//         }
//         else{
//             console.log("This predator cannot shear their prey's meat after attacks");
//         }
//     }
// }
// class Prey extends Species{
//     constructor(diet,typicalLifespan,migrationPatterns,defenseMechanisms,name){
//     super(diet,typicalLifespan,migrationPatterns)
//         this.defenseMechanisms = defenseMechanisms;
//         this.name = name;
//     }
// }


class Species{
    constructor(diet,typicalLifespan,migrationPatterns){
        this.diet =diet;
        this.typicalLifespan = typicalLifespan;
        this.migrationPatterns = migrationPatterns;
    }
    typeOfAnimal(){
        if(this.diet === "herbivorous"){
            console.log("This animal is not a danger to other animals");
        }
        else if(this.diet === "omnivorous"){
            console.log("This animal feeds on plants but also feeds on aome animals");
        }
        else{
            console.log("This animal is very dangerous to other animals and does not eat plants");
        }
    }
}
class Predator extends Species{
    constructor(diet,typicalLifespan,migrationPatterns,typeOfTeeth,claws,venom,name){
    super(diet,typicalLifespan,migrationPatterns)
        this.typeOfTeeth = typeOfTeeth;
        this.claws = claws;
        this.venom = venom;
        this.name = name;
    }
    venomousKillers(){
        if(this.venom === true && this.typeOfTeeth.includes('fangs')){
            console.log("This animal is venomous");
        }
        else{
            console.log("This animals is not venomous");
        }
    }
    methodOfKilling(){
        if(this.typeOfTeeth.includes("carnassial teeth")){
            console.log(`A ${this.name} kills by slicing up their prey`);
        }
        else if(this.claws === true){
            console.log(`A ${thid.name} kills by tearing up their prey.`);
        }
        else if(this.venom === true){
            console.log(`A ${this.name} kills using venom`);
        }
        else{
            console.log("this animal might be harmless");
        }
    }
    }
class Prey extends Species{
    constructor(diet,typicalLifespan,migrationPatterns,defenseMechanisms,name){
    super(diet,typicalLifespan,migrationPatterns)
        this.defenseMechanisms = defenseMechanisms;
        this.name = name;
    }
    likelihoodOfSurvival(){
            if(this.defenseMechanisms.length >2){
                console.log("The likelihood of this animal surviving is quite high");
            }
            else{
                console.log("The likelihood of this animal surviving is quite low");
            }
        }
    }



    // class Product {
    //     constructor(name, price, quantity) {
    //         this.name = name;
    //         this.price = price;
    //         this.quantity = quantity;
    //     }
    
    //     calculateTotalValue() {
    //         return this.price * this.quantity;
    //     }
    // }
    
    // // Creating multiple objects of Product class
    // let productA = new Product('Laptop', 15000, 2)
    // let productB = new Product('Phones', 10000, 2)
    // let productC = new Product('Television', 18000, 2)
    
    // // Calculating total value of all products
    // let totalValue = productA.calculateTotalValue() + productB.calculateTotalValue() + productC.calculateTotalValue();
    
    // console.log(`The total value of all products is ${totalValue}`)
    



    class Product {
        constructor(name, price, quantity) {
          this.name = name;
          this.price = price;
          this.quantity = quantity;
        }
      
        calculateTotalValue() {
          return this.price * this.quantity;
        }
      
        getInfo() {
          const totalValue = this.calculateTotalValue();
          return `${this.name} - Total Value: ${totalValue}`;
        }
      }
      
      let products = [
        new Product('Laptop', 15000, 2),
        new Product('Phones', 10000, 2),
        new Product('Television', 18000, 2)
      ];
      
      let totalValue = 0;
      for (let i = 0; i < products.length; i++) {
        totalValue += products[i].calculateTotalValue();
      }
      
      console.log(`The total value of all products is ${totalValue}`);
    //   # 6. Implement a class called Student with attributes for name, age, and grades (a
    //     # list of integers). Include methods to calculate the average grade, display the
    //     # student information, and determine if the student has passed (average grade >=
    //     # 60). Create objects for the Student class and demonstrate the usage of these
    //     # methods.
      
      class Student{
        constructor(name,age,grades){
            this.name=name;
            this.age=age;
            this.grades=grades;
        }
        averageGrade(){
            let total=0;
            for(g in this.grades){
                total+=g;
                console.log(total);
            }
            let average=total/(this.grades.length)
            console.log(average);
        }
        displayInfo(){
           console.log(`This student's name is ${this.name} and they are ${this.age} years old and they have an average grade of ${this.averageGrade()}`);
        }
        passMark(){
            if(this.averageGrade()>=60){
                console.log("The student has passed");
            }
            else{
                "The student has failed"
            }
        }
    }
    let John=new Student("John",23,[80,85,74,90])
    John.averageGrade()
    John.displayInfo()
    John.passMark()
    