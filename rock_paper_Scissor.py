import random
def get_choices():
  
 options = [ "rock", "paper","scissors"]

 zoya_choice=random.choice(options)
 print("zoya choose", zoya_choice)

 computer_choice=random.choice(options)
 print(" computer choose", computer_choice)
 choice={"user" : zoya_choice, "computer":computer_choice}
 return choice

def get_winner(user, computer):
  if user == computer:
    return "its a tie"
    
  elif user =="rock":
    if computer == "scissors":
      return "rock smashes scissor you win!"
    else:
      return "paper covers rock you lose!"
      
      
  elif user =="scissor":
      if computer == "rock":
        return "rock smashes scissor you lose!"
      else:
        return "scissor cuts the paper you win"

  
  else:
      if computer == "rock":
        return "paper cover rock  you win!"
      else:
        return " scissor cuts the paper you lose!"

choice=get_choices()
result=get_winner(choice ["user"],choice["computer"])
print(result)