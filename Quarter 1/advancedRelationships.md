# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
Class 1: Music

Class 2: Audio Player

# What problem or limitation exists in your current design?
A constraint in my existing design is the unidirectional visibility between the audio player and music classes. While the player manages and executes the music objects, the music class remains entirely unaware of the player context. This one-way relationship makes it difficult for a track to know its own playback state, such as whether it is currently playing or paused, forcing the audio player to exclusively manage all state data

## Inheritance Relationship
Parent: Music

Child: Premium Music

Explanation: The parent class Music defines standard attributes like title, artist, and duration for general audio tracks. The child class Premium Music inherits all these core properties but extends functionality to include preview restrictions and access validations, acting as  a specialized type of music track requiring an active subscription asset profile.
## Inheritance UML
![Inheritance](Images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation

Explanation: The relationship between audioplayer and music is an aggregation because it represents a weak "HAS-A" architectural binding. The audio player stores, references, and queues the tracks inside a playlist array, but the track objects are created independently and can continue to exist in memory even if the player instance itself is deleted
## Advanced UML Diagram
![Advanced UML](Images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](Images/advancedTestRun.png)
## Object Diagram
![Objects](Images/advancedObjectDiagram.png)

## Reflection
### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
I chose this relationship because a premium song is still a song at its core. It needs the same basic details like a title, artist, and duration, but it just adds subscription rules. Therefore, premium music is a specific type of music. This setup perfectly matches how real streaming apps separate free and paid tracks
### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance stopped me from writing the same code twice for the title, artist, and duration variables. The child class automatically gets the parent's string print method by calling super()._str_(). This saved space and kept the code clean
### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
The relationship is aggregation because songs can exist without the music player. A track is an independent file that stays saved in memory even if the player application is closed or deleted. The player simply holds a list of these tracks to play them. Since the tracks can live on without the player, it is a weak relationship
### What is the difference between Association from Part III and the advanced relationship you implemented?
A basic association is just a loose link where two objects talk to each other as equals. The advanced aggregation relationship I used creates a clear hierarchy. It shows that the audio player is a container that organizes and controls a list of songs. This makes the code structure more professional and organized
### How does your design follow the DRY principle?
My design follows the DRY principle by keeping all common song variables in one parent class. If I want to add a basic feature to all songs later, I only have to change it in that one spot. I do not need to copy and paste changes into multiple class files. This creates a single source of truth for the system
