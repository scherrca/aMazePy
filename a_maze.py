# Import appropriate libraries
import random

# Define a start function to prompt the user to start the game
def start():
  # Ask the user if they would like to enter the maze
  print("Would you like to see if you can get through the maze?")
  answer = input("Enter 'Yes' or 'No' ")
  # If the user answers yes:
  if answer == "Yes":
    # Move the user to the lobby
    lobby()
  # If the user answers no:
  elif answer == "No":
    # Display a message to the user acknowledging their "no" response
    print("Fine. Be that way.")
  # If the user does not answer yes or no:
  else:
    # Display a message acknowledging an incorrect input, and start the maze
    print("I have no idea what you just said, so I'm going to have you just play it anyway.")
    lobby()

# Define a function for the values and actions of the "Lobby" room
def lobby():
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a cavernous lobby."
  "Exits: there is a door to the North and a door to the East.\n"
  "In this maze you can also teleport to a random room.")
  # Prompt the user and read in their respnse
  answer = input("Go: Enter 'North,' East' or 'Teleport.' ")
  # If the user answers "North," call the "unicorns" function to "move" the user to that room.
  if answer == "North":
    unicorns()
  # If the user answers "East," call the "cats" function to "move" the user to that room.
  elif answer == "East":
    cats()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  elif answer == "Teleport":
    teleport()
  # Otherwise, if the user answers something else, responsd with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    lobby()

# Define a function for the values and actions of the "Unicorn" room
def unicorns():
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a unicorn lair! You are surrounded by pretty, pretty unicorns."
  "Exits: there is a door to the West, a door to the South, and a door to the East.")
  # Prompt the user and read in their respnse
  answer = input("Go: Enter 'West,' 'East,' 'South,' or 'Teleport.' ")
  #If the user answers "West," call the "dragons" function to "move" the user to that room.
  if answer == "West":
    dragons()
  #If the user answers "East," call the "honey" function to "move" the user to that room.
  elif answer == "East":
    honey()
  #If the user answers "South," call the "lobby" function to "move" the user to that room.
  elif answer == "South":
    lobby()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  elif answer == "Teleport":
    teleport()
  # Otherwise, if the user answers something else, responsd with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    unicorns()

# Define a function for the when a user selects "steak"
def steak():
  # Display a message to the user notifying them that they have successfully exited the maze
  # and return from the function.
  print("\n\nYou've made the dragons very happy! One of them guides you through"
  "the dragon herd towards the South door. You go through the South door, and you're free!")
  return

# Define a function for the values and actions of the "Dragons" room
def dragons():
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a pit of dragons!\n"
  "There are two treasure chests on the ground. one is labeled 'Mead' and one is labeled 'Steak.'"
  "\nThe dragons are fierce, but they give you the sad puppy dog eyes when you get near close"
  " to the chests.\nYou notice that a dragon claw couldn't open the chests, but a human hand"
  " probably could."
  "Exists: there is a door to the East, and a door to the South, but a dragon is blocking it.")
  # Prompt the user and read in their respnse
  answer = input("Go: Enter 'Mead,' 'Steak,' 'East,' or 'Teleport' ")
  #If the user answers "East," call the "unicorns" function to "move" the user to that room.
  if answer == "East":
    unicorns()
  # If the user answers "Steak", call the "steak" function
  elif answer == "Steak":
    steak()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  elif answer == "Teleport":
    teleport()
  # If the user answers "Mead", prompt them to choose another option
  elif answer == "Mead":
    print("\n\nGreat. Now the dragons are drunk. They play silly drinking games then fall asleep.\n"
    "Your only option is to Retreat or try to find one that's still awake and offer him/her Steak")
    response = input("Go: enter 'East' or 'Steak.' ")
    if response == "East":
      unicorns()
    if response == "Steak":
      steak()
  # Otherwise, if the user answers something else, responsd with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    dragons()

# Define a function for the values and actions of the "Honey" room
def honey():
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: oh dear god NOOOOO! You've stumbled into a room full of honey badgers!\n"
  "And this time, they DO give a sh*t. About eating your face!"
  "Exits: Sprint towards a door and hope they don't chase you! There is a door to the West "
  "and one to the South")
  # Prompt the user and read in their respnse
  answer = input("Go: enter 'West,' 'South,' or 'Teleport' ")
  #If the user answers "West," call the "unicorns" function to "move" the user to that room.
  if answer == "West":
    unicorns()
  #If the user answers "South," call the "cats" function to "move" the user to that room.
  elif answer == "South":
    cats()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  elif answer == "Teleport":
    teleport()
  # Otherwise, if the user answers something else, responsd with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    cats()

# Define a function for the values and actions of the "Cats" room
def cats():
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a room full of pretty, pretty kitties! Who all hate you.\n"
  "So much grumpy cat."
  "Exits: there is a door to the West or a door to the North")
  # Prompt the user and read in their respnse
  answer = input("Go: enter 'West' or 'North' or 'Teleport' ")
  #If the user answers "West," call the "lobby" function to "move" the user to that room.
  if answer == "West":
    lobby()
  #If the user answers "North," call the "honey" function to "move" the user to that room.
  elif answer == "North":
    honey()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  elif answer == "Teleport":
    teleport()
  # Otherwise, if the user answers something else, responsd with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    cats()

# Create an array of functions that contain each of the room functions
rooms = [lobby, dragons, unicorns, honey, cats]

# Define a function for "teleport" that randomly selects an index of the rooms array
# and calls the function contained in that index.
def teleport ():
  rooms[random.randint(0, 4)]()

# Call the start function to start the maze
start()