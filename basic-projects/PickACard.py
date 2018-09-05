import random

#setting variables
suits = ['hearts', 'spades', 'diamonds', 'clubs']
cards = ['ace', 'two', 'three', 'four', 'five',
         'six', 'seven', 'eight', 'nine',
         'ten', 'jack', 'queen', 'king']
compSuit = random.choice(suits)
compCard = random.choice(cards)
pickSuits = "Pick a suit: hearts, spades, diamonds, clubs: "
pickCards = "Pick a card: ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king: "
yourSuit = input(pickSuits).lower()
yourCard = input(pickCards).lower()

guesses = 10

if(guesses <= 0):
     print("You ran out of guesses, game over!")
     exit
     
#Begin logic of program
while((yourSuit and yourCard != '') and guesses > 0):
     if((yourSuit == compSuit) and (yourCard == compCard)):
          print("You got it! ", compCard, " of ", compSuit)
          break
     else:
          guesses -= 1
          print("Wrong! You have ", guesses, " guesses left.")
          if((yourSuit == compSuit) and (yourCard != compCard) and (guesses > 0)):
               print("Suit was correct, card was not.")
               yourCard = input(pickCards).lower()
          elif((yourSuit != compSuit) and (yourCard == compCard) and (guesses > 0)):
               print("Card was correct, suit was not.")
               yourSuit = input(pickSuits).lower()
          elif((yourSuit != compSuit) and (yourCard != compCard) and (guesses > 0)):
               print("Neither the suit, nor the card were correct.")
               yourSuit = input(pickSuits).lower()
               yourCard = input(pickCards).lower()
          else:
               if(guesses <= 0):
                    print("You ran out of guesses, game over!")
                    break
