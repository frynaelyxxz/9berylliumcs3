class Animal: #This is the parent class
    def __init__(self, name): #This is the constructor method for the Animal class. It initializes the name attribute of the animal.
        self.name = name #This makes a public attribute called name and this can be accessed and edited outside the class
    def eat(self): #This is a method that prints the eating behavior of the animal. It can be overridden by subclasses to provide specific eating behaviors for different animals.
        print(f"{self.name} eats") #This prints the eating behavior of the animal. It can be overridden by subclasses to provide specific eating behaviors for different animals.
    def make_sound(self): #This is a method that prints the sound made by the animal. It can be overridden by subclasses to provide specific sounds for different animals.
        print(f"{self.name} makes a sound.") #This prints the sound made by the animal. It can be overridden by subclasses to provide specific sounds for different animals. 

class Lion(Animal): #This defines a new class named Lion and it inherits from the Animal class
    def eat(self): #This is a method that prints the eating behavior of the lion. It overrides the eat method of the parent class Animal to provide a specific eating behavior for lions.
        print(f"{self.name} eats fresh meat.") #This prints the eating behavior of the lion. It overrides the eat method of the parent class Animal to provide a specific eating behavior for lions.
    def make_sound(self): #This is a method that prints the sound made by the lion. It can be overridden by subclasses to provide specific sounds for different animals.
        print(f"{self.name} roars loudly!") #This prints the sound made by the lion. It can be overridden by subclasses to provide specific sounds for different animals.

class Elephant(Animal): #This defines a new class named Elephant and it inherits from the Animal class
    def eat(self): #This is a method that prints the eating behavior of the elephant. It overrides the eat method of the parent class Animal to provide a specific eating behavior for elephants.
        print(f"{self.name} eats grass and fruits.") #This prints the eating behavior of the elephant. It overrides the eat method of the parent class Animal to provide a specific eating behavior for elephants.
    def make_sound(self): #This is a method that prints the sound made by the elephant. It can be overridden by subclasses to provide specific sounds for different animals.
        print(f"{self.name} trumpets!") #This prints the sound made by the elephant. It can be overridden by subclasses to provide specific sounds for different animals.
        
class Monkey(Animal): #This defines a new class named Monkey and it inherits from the Animal class
    def eat(self): #This is a method that prints the eating behavior of the monkey. It overrides the eat method of the parent class Animal to provide a specific eating behavior for monkeys.
        print(f"{self.name} eats bananas.") #This prints the eating behavior of the monkey. It overrides the eat method of the parent class Animal to provide a specific eating behavior for monkeys.
    def make_sound(self): #This is a method that prints the sound made by the monkey. It can be overridden by subclasses to provide specific sounds for different animals.
        print(f"{self.name} chatters!") #This prints the sound made by the monkey. It can be overridden by subclasses to provide specific sounds for different animals.
        
L = Lion("Simba") #This creates an instance of the Lion class with the name "Simba"
E = Elephant("Dumbo") #This creates an instance of the Elephant class with the name "Dumbo"
M = Monkey("George") #This creates an instance of the Monkey class with the name "George"

L.make_sound() #This calls the make_sound method of the Lion class, which prints the sound made by the lion.
L.eat() #This calls the eat method of the Lion class, which prints the eating behavior of the lion.
print("-----") #This prints a separator line for better readability of the output.

E.make_sound() #This calls the make_sound method of the Elephant class, which prints the sound made by the elephant.
E.eat() #This calls the eat method of the Elephant class, which prints the eating behavior of the elephant.
print("-----") #This prints a separator line for better readability of the output.

M.make_sound() #This calls the make_sound method of the Monkey class, which prints the sound made by the monkey.
M.eat() #This calls the eat method of the Monkey class, which prints the eating behavior of the monkey.
print("-----") #This prints a separator line for better readability of the output.