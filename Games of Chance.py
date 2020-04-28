#codecademy game of chance project
import random

money = 100

def coin_flip(side, bet):
  global money
  if bet > money:
    print("you cant bet more than you have.\nyou have ${} left\n".format(money))
    return 0
  if bet < 1:
    print("You cant bet less than one dollar")
    return 0
  print("${} for {}.\n".format(bet, side))
  result = random.randint(1,2)
  if result == 1:
    result = "heads"
  if result == 2:
    result = "tails"
  if result == side:
    money = money + bet
    print("Yes! Coin flip resulted in {}. You won ${}!\nYou have ${} left\n".format(result, bet, money))
    return bet
  else:
    money = money - bet
    print("Sorry. Coin flip resulted in {} you lost ${}.\nYou have ${} left\n".format(result, bet, money))
    bet =-bet
    #print(str(bet))
  return bet

def cho_han(odds_even, bet):
  global money
  if bet > money:
    print("you cant bet more than you have.\nyou have ${} left\n".format(money))
    return 0
  if bet < 1:
    print("You cant bet less than one dollar")
    return 0
  di1 = random.randint(1,6)
  di2 = random.randint(1,6)
  dice_total = di1 + di2
  print(str(dice_total))
  if odds_even == "even":
    odds_even = 0
  else:
    odds_even = 1
  if dice_total % 2 == 0 and odds_even % 2 == 0:
    money = money + bet
    print("Cho Han. Yes! Dice total is an even number you win $", str(bet) + "\nYou now have $" + str(money) + ".\n")
      
  elif dice_total % 2 == 0 and odds_even % 2 != 0:
    money = money - bet
    print("Cho Han. Sorry. Dice total is even! you lost $" + str(bet) + "\nYou now have $" + str(money) + ".\n")
    bet =- bet
  elif dice_total % 2 != 0 and odds_even % 2 != 0:
    money = money + bet
    print("Cho Han. Yes. Dice total is odd! You win $", bet, "\n" + "You now have $" + str(money))
      
  else:
    money = money - bet
    print("Cho Han. Sorry. Dice total is odd. You lose $", bet, "\n" + "You now have $" + str(money) + ".")
    bet =- bet
  return bet
   
player1_money = 100
player2_money = 100  

def cards(betplayer1, betplayer2 ,player1="Dean" ,player2= "Dan"):
  global player1_money
  global player2_money
  if betplayer1 > player1_money or betplayer2 > player2_money:
    print("you cannot bet more money than you have {p1} has ${p1m} and {p2} has {p2m}".format(p1=player1,p2=player2,p1m=betplayer1,p2m=betplayer2))
    return 0,0
  if betplayer1 < 1 or betplayer2 < 1:
    print("you cannot bet less than one dollar")
    return 0,0
  print("{p1} bets ${p1m}.\n{p2} bets ${p2m}.\n".format(p1=player1, p1m=str(betplayer1),p2=player2, p2m=str(betplayer2)))
  card_deck = [2,3,4,5,6,7,8,9,"jack", "queen", "king", "ace"]
  card_deck_v = [2,3,4,5,6,7,8,9,10,11,12,13]
  player1_card = random.choice(card_deck)
  player2_card = random.choice(card_deck)
  print("{} has selected {}....\n" .format(player1,player1_card))
  print("{} has selected {}....\n".format(player2,player2_card))
  card_values = {key:value for key,value in zip(card_deck,card_deck_v)}
  if card_values[player1_card] > card_values[player2_card]:
      print("{p1} wins with {c1}. \n{p1} wins ${b1}.".format(c1=player1_card, p1=player1,b1=betplayer1))
      player1_money = player1_money + betplayer1
      player2_money = player2_money - betplayer2
  elif card_values[player1_card] == card_values[player2_card]:
    print("You both have the same card!")
  else:
      print("{p2} wins with {c2}. \n{p2} wins ${b2}.".format(c2=player2_card, p2=player2,b2=betplayer2))
      player2_money += betplayer2
      player1_money = player1_money - betplayer1
      print("{p1} has ${p1m} left.\n{p2} has ${p2m} left\n".format(p1=player1, p2=player2, p1m=player1_money, p2m=player2_money))
  return player1_money, player2_money
      
def roulette(bet, choice):
  global money
  wheel = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
  selection = random.randint(0,36)
  #selection = wheel[0]
  if bet > money:
    print("you cant bet more than you have.\nyou have ${} left\n".format(money))
    return 0
  if bet < 1:
    print("You cant bet less than one dollar")
    return 0
  print("Roulette. Your choice is ....." + str(choice) + " at $" + str(bet) + ".")
  print("selection = ",selection)
  if selection == 0:
    money = money - bet
    print("{} has come up you lose ${}.\n You now have ${}.".format(selection, bet, money))
    bet =- bet
    return bet
  elif choice == selection:
    money = money + (3 * bet)
    print("Roulette. Your number won! with {} selection!!!!!!!!!!!!!!!!!! you win ${}.\nYou now have ${}\n".format(print(str(choice)),str(bet),str(money)))
  
      
  elif choice is "even" and selection % 2 == 0:
    money = money + bet
    print("you won! evens came up!You have " + "$" + str(money) + "\n")
    bet += bet
  elif choice is "even" and selection % 2 != 0:
    money = money - bet
    print("Sorry, you lost, odds came up. You have " + "$" + str(money) + "\n")
    bet =- bet
  elif choice is "odd" and selection % 2 != 0:
    money = money + bet
    print("You won! odds came up. You have " + "$" + str(money) + "\n")
     
  elif choice is "odd" and selection % 2 == 0:
    money = money - bet
    print("Even came up you lost. You have " + "$" + str(money) + "\n")
    bet =- bet
  elif choice != selection:
    money = money - bet
    print("Sorry, your number didnt come up.You have " + "$" + str(money) + "\n")
    bet =- bet
  return bet
  
  
#Call your game of chance functions here
money += coin_flip("heads", -10)

money += cho_han("even", 30)

money += cho_han("odd", -11)

money += cho_han("even", 45)

p1m, p2m = cards(12, -56)

p1m,p2m = cards(10, 78)

money += roulette(34, "even")

money += roulette(22, "odd")

money += roulette(-28, 31)

money += roulette(77, 32)

money += roulette(45, 33)

money += roulette(-88, "odd")