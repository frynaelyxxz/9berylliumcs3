class Publication: #this defines a new class called Publication
    def __init__(self, title, author): #This is the constructor method for the Publication class. It initializes the title and author attributes of the publication.
        self.__title = title #This makes a private attribute called title and this can only be edited inside the class
        self.__author = author #This makes a private attribute called author and this can only be edited inside the class
        
    def get_author(self): #This is a getter method for the author
        return self.__author #This returns the value of the private attribute author
    def get_title(self): #This is a getter method for the title
        return self.__title #This returns the value of the private attribute title
    def set_author(self, author): #This is a setter method for the author
        self.__author = author #This sets a new value for the private attribute author
    def set_title(self, title): #This is a setter method for the title
        self.__title = title #This sets a new value for the private attribute title
   
    def display(self): #This method displays the title and author of the publication
        print(f"Title: {self.__title}") #This prints the title of the publication
        print(f"Author: {self.__author}") #This prints the author of the publication
        
class Book(Publication): #`This defines a new class named Book and it inherits from the Publication class
    def __init__(self, title, author, pages): #This is a construtor method for the class Book
        super().__init__(title, author) #This calls the constructor of the parent class Publication to initialize the title and author attributes
        self.__pages = pages #This makes a private attlribute called pages and this can obly be changes inside the class
    
    def get_pages(self): #This is a getter method for the pages
        return self.__pages #This returns the value of the private attribute pages
    def set_pages(self, pages): #Setter method for the pages
        if pages > 0: #This checks if the number of pages is positive
            self.__pages = pages #If the number of pages is positive, it sets the value of the private attribute pages
        else: #If the number of pages is negative, it prints a warning message
            print("The number of pages must be positive") #This prints the warning message if the number of pages is negative
            
    def display(self): #This method displays the title, author, and number of pages of the book
        super().display() #This calls the display method of the parent class Publication to display the title and author
        print(f"Number of Pages: {self.__pages}") #This prints the number of pages of the book
            
class Magazine(Publication): #This defines a new class named Magazine and it inherits from the Publication class
    def __init__(self, title, author, issue): #This is a constructor method for the class Magazine
        super().__init__(title, author) #This calls the constructor of the parent class Publication to initialize the title and author attributes
        self.__issue = issue #This makes a private attribute names issue
    
    def get_issue(self): #This is a getter method for the issue
        return self.__issue #This returns the value of the private attribute issue
    def set_issue(self, issue): #This is a setter method for the issue
        if issue > 0: #This checks if the issue number is positive
            self.__issue = issue #If the issue number is positive then it sets the value of the private attribute issue
        else: #If the issue number is negative, it prints a warning message
            print("The issue number must be positive") #This prints the warning message if the issue number is negative
            
    def display(self): #This method displays the title, author, and issue number of the magazine
        super().display() #This calls the display method of the parent class Publication to display the title and author
        print(f"Issue Number: {self.__issue}") #This prints the issue number of the magazine
        
p1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") #This creates an instance of the Publication class with the title "Journal of Experimental Psychology" and the author "Ratchiff, R. & Van Dongen, H."
b1 = Book("The Hobbit", "J.R.R. Tolkien", 310) #This creates an instance of the Book class with the title "The Hobbit", the author "J.R.R. Tolkien", and 310 pages
m1 = Magazine("National Geographic", "Various Authors", 202) #This creates an instance of the Magazine class with the title "National Geographic", the author "Various Authors", and issue number 202

print("Publication Information: ") #This prints the header for the publication information
p1.display() #This prints the title and author of the publication
print() #This prints a blank line
print("\nBook Information: ") #This prints the header for the book information
b1.set_pages(-310) #This attempts to set the number of pages of the book to -310, which is invalid because it's a negative number and will trigger a warning message
b1.display() #This prints the title, author, and number of pages of the book
print() #This prints a blank line
print("\nMagazine Information: ") #This prints the header for the magazine information
m1.display() #This prints the title, author, and issue number of the magazine