# Author: Cait Scherr
# Text Adventure Maze
# 7/16/2015

# Import appropriate libraries
import random

# Assign values to the "backpack" list
pack = ["cactus", "catnip", "sandwich", "sword", "honey"]

# Define a start function to prompt the user to start the game
def start():
  # Ask the user if they would like to enter the maze
  print("Would you like to see if you can get through the maze?")
  answer = input("Enter 'Yes' or 'No' ").lower()
  # If the user answers yes:
  if answer == "yes":
    # Welcome the user and explain the maze
    welcome()
  # If the user answers no:
  elif answer == "no":
    # Display a message to the user acknowledging their "no" response
    print("Fine. Be that way.")
  # If the user does not answer yes or no:
  else:
    # Display a message acknowledging an incorrect input, and welcome the user to the maze
    print("I have no idea what you just said, so I'm going to have you just play it anyway.")
    welcome()

# Welcome the user, explain the maze, and move them to the lobby
def welcome():
  print("\n\nWelcome to the a-MAZE-ing Magical Monster Maze!\n"
  "There are 5 rooms in this maze, each is full of something that can help you, hurt you... or ignore you\n"
  "(hint there are cats).\n\n"
  "You will be given a choice of choosing an exit and/or using something in your arsenal.\n"
  "You will also be given the option of teleporting to a random room.\n"
  "Your arsenal: you are carrying only your wits and an awkward wheely backpack.\n"
  "Your wheely backpack contains a cactus, catnip, a sandwich, the sword of Griffindor, and a jar of honey.\n")
  lobby()

# Set a boolean variable to track whether or not an item is in the pack
bool_item = False

# Define the "pack_item" function to allow users to access their items, 
# or tell them that they have already used it
def pack_item(item):
  # Access global variables
  global pack
  global bool_item
  # If the item is in the list, set the boolean value to true,
  # remove the item and display a custom message to the user
  if item in pack:
    pack.remove(item)
    bool_item = True
    print(message)
 # Otherwise, display a message notifying the user that there is no item
  else:
    print("Nooooo! You already used your", item, "Let's just move on then.")

# Create a generic message for the user eating the sandwich
sandwich_mes = "\nNow you have super sandwich powers! Just kidding, but you feel better now, right?\n"
"Now let's go somewhere."

# Create a generic message for the user using the catnip
catnip_mes = "\nWell, they do love catnip... but unfortunately, it's flakey and you're covered in it!\n"
"Your only choice is to run away! Teleport, activated!\n"

# Define a function for the values and actions of the "Lobby" room
def lobby():
  # Include "message" global variable
  global message
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a cavernous lobby.\n"
  "Exits: there is a door to the North and a door to the East.\n")
  # Prompt the user and read in their respnse
  answer = input("Go: Enter 'North,' East', 'Teleport' or 'sandwich' to eat your sandwich: ").lower()
  # If the user answers "North," call the "unicorns" function to "move" the user to that room.
  if answer == "north":
    unicorns()
  # If the user answers "East," call the "cats" function to "move" the user to that room.
  elif answer == "east":
    cats()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  elif answer == "teleport":
    teleport()
  # If the user answers "sandwich," remove it from their pack and start the room again
  elif answer == "sandwich":
    message = sandwich_mes
    pack_item("sandwich")
    lobby()
  # Otherwise, if the user answers something else, responsd with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    lobby()

# Define a function for the values and actions of the "Unicorn" room
def unicorns():
  # Include "message" global variable
  global message
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a unicorn lair! You are surrounded by pretty, pretty unicorns.\n"
  "Exits: there are lots of exits, but too many darn unicorns in between you and the doors.")
  # Prompt the user and read in their respnse
  answer = input("Go: Enter 'Teleport,''honey' or 'catnip' to offer to the unicorns,\n"
  "'sword' to attack the unicorns or 'sandwich' to eat your sandwich: ").lower()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  if answer == "teleport":
    teleport()
  # If the user answers "sandwich," remove it from their pack and start the room again
  elif answer == "sandwich":
    message = sandwich_mes
    pack_item("sandwich")
    unicorns()
  # If the user answers "honey", remove it from their pack and start the room again
  elif answer == "honey":
    message = "\nGross. Now the unicorns are all sticky. Let's try this again.\n"
    pack_item("honey")
    unicorns()
  # If the user answers "catnip", remove it from their pack and allow them to choose a direction
  elif answer == "catnip":
    message = "\nEveryone knows unicorns love catnip! The unicorns let you pass.\n"
    pack_item("catnip")
    # If the item was still in the pack:
    if bool_item == True:
      # Prompt the user to enter a direction
      answer = input("Enter 'West', 'East', or 'South'\n").lower()
      # If the user answers "West," call the "dragons" function to "move" the user to that room.
      if answer == "west":
        dragons()
      #If the user answers "East," call the "honey" function to "move" the user to that room.
      elif answer == "east":
        honey()
      #If the user answers "South," call the "lobby" function to "move" the user to that room.
      elif answer == "south":
        lobby()
  # If the user answers "sword", end the maze
  elif answer == "sword":
    message = "\nWhat? Who attacks unicorns??\n"
    "Also, they have their own swords. On their faces, so- you lose this one.\n"
    "Death by unicorn- did not see that coming!\n"
    pack_item("sword")
    if bool_item == True:
      return
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
  # Include "message" global variable
  global message
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a pit of dragons!\n"
  "There are two treasure chests on the ground. one is labeled 'Mead' and one is labeled 'Steak.'"
  "\nThe dragons are fierce, but they give you the sad puppy dog eyes when you get near close"
  " to the chests.\nYou notice that a dragon claw couldn't open the chests, but a human hand"
  " probably could."
  "Exits: there is a door to the East, and a door to the South, but a dragon is blocking it.")
  # Prompt the user and read in their respnse
  answer = input("Go: Enter 'Mead,' 'Steak,' 'sword' to attack, 'sandwich' to eat your sandwich,\n"
    "'honey' to offer to the dragons, 'East,' or 'Teleport': ").lower()
  #If the user answers "East," call the "unicorns" function to "move" the user to that room.
  if answer == "east":
    unicorns()
  # If the user answers "Steak", call the "steak" function
  elif answer == "steak":
    steak()
  # If the user answers "Teleport" call the "teleport" function to move the user to a 
  # random room.
  elif answer == "teleport":
    teleport()
  # If the user answers "sandwich," remove it from their pack and start the room again
  elif answer == "sandwich":
    message = sandwich_mes
    pack_item("sandwich")
    dragons()
  # If the user answers "Mead", prompt them to choose another option
  elif answer == "mead":
    print("\n\nGreat. Now the dragons are drunk. They play silly drinking games then fall asleep.\n"
    "Your only option is to Retreat or try to find one that's still awake and offer him/her Steak")
    answer = input("Go: enter 'East' or 'Steak.' ").lower()
    if answer == "east":
      unicorns()
    if answer == "steak":
      steak()
  elif answer == "honey":
    message = "\nHow SWEET of you. Dragons are impressed- they love honey,\n"
    "and they happily lead you to the South door, where you see daylight- you're free! Well done!\n"
    pack_item("honey")
    if bool_item == True:
      return
  elif answer == "sword":
    message = "\nYikes. Wrong choice. There are... a LOT of dragons.\n" 
    "They breathe so much fire your sword melts.\n"
    "Sorry- you don't make it this time!\n"
    pack_item("sword")
    # If the item was still in the pack, exit the program
    if bool_item == True:
      return
  # Otherwise, if the user answers something else, responds with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    dragons()

# Define a function for the values and actions of the "Honey" room
def honey():
  # Include "message" global variable
  global message
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: oh dear god NOOOOO! You've stumbled into a room full of honey badgers!\n"
  "And this time, they DO give a sh*t. About eating your face!"
  "Exits: they're blocking the doors!\n")
  # Prompt the user and read in their respnse
  answer = input("Go: enter 'Teleport' or offer them 'honey' or 'catnip': ").lower()
  if answer == "catnip":
    message = catnip_mes
    pack_item("catnip")
    # If the item was still in the pack, call the teleport function
    if bool_item == True:
      teleport()
  if answer == "honey":
    message = "\nmmm honey badgers love honey! They aren't going to help you,\n"
    "but at least now they're all distracted and you can make a run for the door!\n"
    pack_item("honey")
    # If the item was still in the pack, prompt the user to choose a direction
    if bool_item == True:
      answer = input("Enter 'West' or 'South': ").lower()
      #If the user answers "West," call the "unicorns" function to "move" the user to that room.
      if answer == "west":
        unicorns()
      #If the user answers "South," call the "cats" function to "move" the user to that room.
      elif answer == "south":
        cats()
      # If the user answers "Teleport" call the "teleport" function to move the user to a 
      # random room.
  elif answer == "teleport":
    teleport()
  # If the user answers "sandwich," remove it from their pack and start the room again
  elif answer == "sandwich":
    message = sandwich_mes
    pack_item("sandwich")
    honey()
  # Otherwise, if the user answers something else, responsd with an error message and
  # repeat the prompt.
  else:
    print("whaaat?? Please enter your answer again.")
    cats()

# Define a function for the values and actions of the "Cats" room
def cats():
  # Include "message" global variable
  global message
  # Display a message to the user describing the room, the exits, and their "go" options
  print("\n\nYou are in: a room full of pretty, pretty kitties! Who all hate you.\n"
  "So much grumpy cat."
  "Exits: they are blocking all exits!")
  # Prompt the user and read in their respnse
  answer = input("Go: enter 'Teleport' or offer them 'catnip', 'sword' or 'cactus': ").lower()
  #If the user answers "West," call the "lobby" function to "move" the user to that room.
  if answer == "catnip":
    message = catnip_mes
    pack_item("catnip")
    # If the item was still in the pack, call the teleport function
    if bool_item == True:
      teleport()
  if answer == "cactus":
    message = "\nThat's grumpy cat's best friend! All the grumpy kitties go hang with cactus\n"
    "and let you pass.\n"
    pack_item("cactus")
    # If the item was still in the list, prompt the user to choose a direction
    if bool_item == True:
      answer = input("Enter 'West' or 'North': ").lower()
    if answer == "west":
      lobby()
    #If the user answers "North," call the "honey" function to "move" the user to that room.
    elif answer == "north":
      honey()
    # If the user answers "Teleport" call the "teleport" function to move the user to a 
    # random room.
  elif answer == "teleport":
    teleport()
  # If the user answers "sandwich," remove it from their pack and start the room again
  elif answer == "sandwich":
    message = sandwich_mes
    pack_item("sandwich")
    cats()
  elif answer == "sword":
    message = "\nThe sword reflects little spots of lights onto the floor that send the cats\n"
    "into a frenzy! They won't help you, but they're distracted enough to let you pass.\n"
    pack_item("sword")
    # If the item was still in the list, prompt the user to choose a direction
    if bool_item == True:
      answer = input("Enter 'West' or 'North' to escape").lower()
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