print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction_choice = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if direction_choice == "left":
  lake_choice = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()

  if lake_choice == "wait":
    door_choice = input("You arrive at the island unharmed. There is a house with 3 doors: orange, red, and yellow. Which color do you choose? ").lower()

    if door_choice == "yellow":
      print("You found the treasure! You Win!")
    elif door_choice == "red":
      print("It's a room full of fire. Game Over.")
    elif door_choice == "orange":
      print("It's a room full of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("Game Over.")    
else:
  print("Game Over.")    

