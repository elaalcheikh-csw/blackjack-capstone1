import random
from replit import clear
from art import logo

def deal_card():
  cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score, computer_score):
  
  if user_score == computer_score:
    return "Draw "
  elif user_score > 21 and computer_score > 21:
    return " You lose "
  elif computer_score == 0:
    return " user Lose "
  elif user_score == 0:
    return " user Win "
  elif computer_score > 21:
    return " You win "  
  elif user_score > 21:
    return " You lose "
  elif user_score > computer_score:
    return "You win "
  else:
    return "You lose "
def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  game not end = False
  while game not end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if user_score == 0 or computer_score == 0 or user_score > 21:
     the game ends = True
    else:
      opinion_user = input("put 'A' to get another card, put 'P' to pass: ")
      if  opinion_user == "A":
        user_cards.append(deal_card())
      elif user_score < 17:
        print("Your cards are less than 17.  draw a card")
        user_cards.append(deal_card())
      else:
        the game ends = True
  while computer_score not equal to  0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(compare(user_score, computer_score))
while input("Do you want to restart the game? Type 'A' or 'P'==A ")
  clear()
  play_again()