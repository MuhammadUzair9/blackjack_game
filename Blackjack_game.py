## Rules 

##first you pick 2 cards if your sum is equals to 21 you win if your sum is greater than 21 you lose if your sum is less than 21 you can pick another
##if your score is less than computer score you lose if your score is greater than computer score you win
# after you choice your third card if your sum is greater than 21 you lose if your sum is less tha computer cards sum you loose and you can also pick another card
# if your sum is equals to computer sum than its a draw



import sys
import random
while True:
  
  choice=input("do you want to play a game of blackjack type y or n ")
  cards = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  your_cards = []
  first_card=random.choice(cards)
  second_card=random.choice(cards)
  your_cards.append(first_card)
  your_cards.append(second_card)
  score = sum(your_cards)
  computer_cards = []
  computer_first_card= random.choice(cards)
  computer_second_card= random.choice(cards)
  computer_cards.append(computer_first_card)
  computer_cards.append(computer_second_card)
  computer_score  = sum(computer_cards)
  if choice == "y":
    print(f"your cards are {your_cards} and your score is {score}")
    print(f"computer first card is {computer_first_card}")
    if score == 21 :
      print("you win you have a black jack")
      sys.exit()
    elif score > 21:
      print("you lose you went over 21")
    
        
  con = input("do you want to pick another card type yes or no ")
  while True:
    
    if con == "yes":
        third_card = random.choice(cards)
        your_cards.append(third_card)
        score = sum(your_cards)
        print(f"your cards are {your_cards} and your score is {score}")
        print(f"computer final hand is {computer_cards} and computer score is {computer_score}")
    
        if score > 21:
          print(f"you lose your score is {score} you went over 21")
          # sys.exit()
          # print(f"computer final hand is {computer_cards} and computer score is {computer_score}")
      
        elif computer_score > score:
           print(f"you losse your score is {score} less than computer score {computer_score}")
        elif computer_score < score:
          print(f"you win your score is {score} greater than computer score {computer_score}")
        elif computer_score == score:
          print(f"its a draw you score {scoer} and computer score is {computer_score} equal")
        elif computer_cards == 21:
          print(f"you lose computer has a black jack {computer_cards}")
    if  con == "yes":
      con = input("do you want to pick another card type yes or no ")
    elif con == "no":
      break
  if con == "no" :
      print(f"your final hand is {your_cards} and you final score id {score}")
      print(f"computer final hand is {computer_cards} and computer score is {computer_score}")
      if computer_score > score:
        print(f"you losse computer {score} greater than your score {score}")
      elif computer_score < score:
        print(f"you win your score {score} is greater than computer score {score}")
      elif computer_score == score:
        print("its a draw")
      elif computer_score > 21:
        print("you win com scored more than 21")
  user_input = input("Do you want to restart? (yes/no): ")
  if user_input.lower() != "yes":
    print("you have successfully exited the game")
    break