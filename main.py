class Room:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices

    def display(self):
        print(self.description)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice.description}")

    def get_choice(self):
        while True:
            choice = input("Enter your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.choices):
                return int(choice)
            else:
                print("Invalid choice. Please enter a valid option.")

# Define the rooms
room1 = Room("You wake up in a dark room. There is a door to your right and left.", ["Go left", "Go right"])
room2 = Room("You find yourself on a balcony overlooking a dense forest.", ["Go back", "Jump off"])
room3 = Room("You are in a library filled with ancient books. There is a ladder to your right.", ["Climb the ladder", "Go back"])
room4 = Room("You climb the ladder and find a hidden attic. There is a chest in the corner.", ["Open the chest", "Go back"])
room5 = Room("You jump off the balcony and land in the forest. There is a path leading deeper.", ["Follow the path", "Go back"])
room6 = Room("You open the chest and find a map. There is a marked location.", ["Investigate the location", "Ignore it"])
room7 = Room("You follow the path and encounter a wild animal.", ["Fight", "Run away"])
room8 = Room("You investigate the location and find a hidden treasure.", ["Take the treasure", "Leave it"])
room9 = Room("You fight the animal and win. You find a key in its den.", ["Take the key", "Leave it"])
room10 = Room("You run away from the animal and find yourself lost in the forest.", ["Try to find your way back", "Keep going"])
room11 = Room("You take the treasure and become rich. Congratulations, you won the game!", [])
room12 = Room("You take the key and return to the room. The key fits a locked door.", ["Open the door", "Leave it"])
room13 = Room("You open the door and find a secret passage. It leads to a hidden treasure.", ["Take the treasure", "Leave it"])
room14 = Room("You find your way back to the room. You're safe, for now.", ["Rest", "Keep exploring"])
room15 = Room("You keep going and find a hidden village. They welcome you as their leader. Congratulations, you won the game!", [])

# Define the connections between rooms
room1.choices[0] = room2
room1.choices[1] = room3
room2.choices[0] = room1
room2.choices[1] = room5
room3.choices[0] = room4
room3.choices[1] = room1
room4.choices[0] = room6
room4.choices[1] = room3
room5.choices[0] = room7
room5.choices[1] = room2
room6.choices[0] = room8
room6.choices[1] = "You ignore the map and continue your adventure."
room7.choices[0] = room9
room7.choices[1] = room10
room8.choices[0] = room11
room8.choices[1] = "You leave the treasure and continue your adventure."
room9.choices[0] = room12
room9.choices[1] = "You leave the key and continue your adventure."
room10.choices[0] = room14
room10.choices[1] = room15
room12.choices[0] = room13
room12.choices[1] = "You leave the door and continue your adventure."
room13.choices[0] = room11
room13.choices[1] = "You leave the treasure and continue your adventure."
room14.choices[0] = "You rest and regain your strength. Continue your adventure."
room14.choices[1] = room1

# Start the game
current_room = room1
while True:
    current_room.display()
    if isinstance(current_room.choices[0], Room):
        choice = current_room.get_choice()
        current_room = current_room.choices[choice - 1]
    else:
        print(current_room.choices[0])
        break
