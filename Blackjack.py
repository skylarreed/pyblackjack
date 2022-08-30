# Blackjack Project #
from art import logo
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = False

while play == False:
    if input('\nWould you like to play blackjack ("y" or "n"): ') == "y":
        chosen = []
        dealer = []
        chosen.append(cards[random.randint(0, 12)])
        chosen.append(cards[random.randint(0, 12)])
        print(f"Your cards are {chosen}")
        dealer.append(cards[random.randint(0,12)])
        print(f"\nThe Dealer's first card is {dealer[0]}")
        if input("\nWould you like to draw another card? ('y' or 'n'): ") == "y":
            chosen.append(cards[random.randint(0, 12)])
            if sum(chosen) > 21:
                print(f"You busted! Your cards were: {chosen}")
            else:
                print(f"Your cards are now: {chosen}")
                if input("\nWould you like to draw another card? ('y' or 'n'): ") == "y":
                    chosen.append(cards[random.randint(0, 12)])
                    if sum(chosen) > 21:
                        print(f"You busted! Your cards were: {chosen}")
                    else:
                        print(f"Your cards are now: {chosen}")
        while sum(dealer) < 17:
            dealer.append(cards[random.randint(0,12)])
        if sum(dealer) > 21 and sum(chosen) < 22:
            print(f"\nYou Win! The dealer pulled: {dealer}. \nYou pulled: {chosen}")
        if sum(dealer) < 22 and sum(chosen) < 22:
            if sum(dealer) > sum(chosen):
                print(f"\nDealer wins. Dealers cards were {dealer}. \nYour cards were {chosen}.")
            else:
                print(f"\nYou win. Your cards were {chosen}. \nDealers cards were {dealer}.")
    else:
        play = True
        break