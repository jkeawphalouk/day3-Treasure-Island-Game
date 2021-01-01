print("Welcome to Treasure Island\n")
userAns = input("Left or right?")
if userAns == "right":
  print("Game Over")
else:
  userAns = input("swim or wait?")
  if userAns == "swim":
    print("Game Over")
  else:
    userAns = input("Which Door? Blue, Red, or Yellow?")
    if userAns == "Red" or "Blue":
      print("Game Over")
    else: 
      print("You Win!")