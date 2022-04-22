import random
#Command Line BlackJack

print("Welcome to Command Line Blackjack. Enter \"hit\" or \"h\" to hit, or \"stand\" or \"s\" to stand.")

#Create card deck as a dictionary with values assigned to each card
deck = {
    "2 of Hearts": 2, "2 of Diamonds": 2, "2 of Clubs": 2, "2 of Spades": 2, 
    "3 of Hearts": 3, "3 of Diamonds": 3, "3 of Clubs": 3, "3 of Spades": 3, 
    "4 of Hearts": 4, "4 of Diamonds": 4, "4 of Clubs": 4, "4 of Spades": 4,  
    "5 of Hearts": 5, "5 of Diamonds": 5, "5 of Clubs": 5, "5 of Spades": 5, 
    "6 of Hearts": 6, "6 of Diamonds": 6, "6 of Clubs": 6, "6 of Spades": 6, 
    "7 of Hearts": 7, "7 of Diamonds": 7, "7 of Clubs": 7, "7 of Spades": 7, 
    "8 of Hearts": 8, "8 of Diamonds": 8, "8 of Clubs": 8, "8 of Spades": 8, 
    "9 of Hearts": 9, "9 of Diamonds": 9, "9 of Clubs": 9, "9 of Spades": 9,
    "10 of Hearts": 10, "10 of Diamonds": 10, "10 of Clubs": 10, "10 of Spades": 10, 
    "Jack of Hearts": 10, "Jack of Diamonds": 10, "Jack of Clubs": 10, "Jack of Spades": 10, 
    "Queen of Hearts": 10, "Queen of Diamonds": 10, "Queen of Clubs": 10, "Queen of Spades": 10,
    "King of Hearts": 10, "King of Diamonds": 10, "King of Clubs": 10, "King of Spades": 10, 
    "Ace of Hearts": 11, "Ace of Diamonds": 11, "Ace of Clubs": 11, "Ace of Spades": 11,
    }


#Create empty dictionaries for player's cards and dealer's cards
player_cards = {}
dealer_cards = {}

#Count the number of wins each player has
player_wins = 0
dealer_wins = 0


#Function to deal the cards
def deal_cards():

    #Player and dealer each receive 2 random cards from the deck
    player_card_1 = random.choice(list(deck.items()))
    dealer_card_1 = random.choice(list(deck.items()))
    player_card_2 = random.choice(list(deck.items()))
    dealer_card_2 = random.choice(list(deck.items()))

    #Remove cards that are dealt from the deck
    deck.pop(player_card_1[0], None)
    deck.pop(player_card_2[0], None)
    deck.pop(dealer_card_1[0], None)
    deck.pop(dealer_card_2[0], None)

    #The player's and dealer's cards are added to their hands, which are dictionaries
    player_cards[player_card_1[0]] = player_card_1[1]
    player_cards[player_card_2[0]] = player_card_2[1]
    dealer_cards[dealer_card_1[0]] = dealer_card_1[1]
    dealer_cards[dealer_card_2[0]] = dealer_card_2[1]

    #Print who has drawn which cards
    print("Player draws: " + str(list(player_cards)) + " Total points: " + str(sum(player_cards.values())))
    print("Dealer draw: " + str(list(dealer_cards)[0]) + " & Unknown.")



#Function to ask if the player wants to play another hand after the end of each round
def play_again():

    #The card deck is reset to a full deck
    deck = {
    "2 of Hearts": 2, "2 of Diamonds": 2, "2 of Clubs": 2, "2 of Spades": 2, 
    "3 of Hearts": 3, "3 of Diamonds": 3, "3 of Clubs": 3, "3 of Spades": 3, 
    "4 of Hearts": 4, "4 of Diamonds": 4, "4 of Clubs": 4, "4 of Spades": 4,  
    "5 of Hearts": 5, "5 of Diamonds": 5, "5 of Clubs": 5, "5 of Spades": 5, 
    "6 of Hearts": 6, "6 of Diamonds": 6, "6 of Clubs": 6, "6 of Spades": 6, 
    "7 of Hearts": 7, "7 of Diamonds": 7, "7 of Clubs": 7, "7 of Spades": 7, 
    "8 of Hearts": 8, "8 of Diamonds": 8, "8 of Clubs": 8, "8 of Spades": 8, 
    "9 of Hearts": 9, "9 of Diamonds": 9, "9 of Clubs": 9, "9 of Spades": 9,
    "10 of Hearts": 10, "10 of Diamonds": 10, "10 of Clubs": 10, "10 of Spades": 10, 
    "Jack of Hearts": 10, "Jack of Diamonds": 10, "Jack of Clubs": 10, "Jack of Spades": 10, 
    "Queen of Hearts": 10, "Queen of Diamonds": 10, "Queen of Clubs": 10, "Queen of Spades": 10,
    "King of Hearts": 10, "King of Diamonds": 10, "King of Clubs": 10, "King of Spades": 10, 
    "Ace of Hearts": 11, "Ace of Diamonds": 11, "Ace of Clubs": 11, "Ace of Spades": 11,
    }

    #Ask if the player would like to play again
    ask_to_play = input("Would you like to play again? Yes or no? ").lower()
 
    #If the player enter no or n, then the game is over and it prints the final score
    if ask_to_play == "no" or ask_to_play == "n":
        print("Final Score - Player: " + str(player_wins) + ", Dealer: " + str(dealer_wins))
        return "Goodbye."

    #If the player enters yes or y, then the game is played again
    elif ask_to_play == "yes" or ask_to_play == "y":
        return play_hand()
    
    #If the player enters anything other than yes, y, no, or n, then it ask them to respond again
    else:
        print("Sorry, I didn't understand. ")
        return play_again()



#Function to determine who wins
def winner():
    global player_wins
    global dealer_wins

    #If the player goes over 21, they bust and the dealer wins. The dealer's win count goes up by 1. Their hands are cleared and the player is asked to play again.
    if sum(player_cards.values()) > 21:
        print("Bust! Dealer wins!")
        dealer_wins += 1
        print("Player wins: " + str(player_wins) + ". Dealer wins: " + str(dealer_wins))
        player_cards.clear()
        dealer_cards.clear()
        return play_again()

    #If both the dealer and player have 21 or less, then if the dealer has more points the dealer wins, if the player has more points the player wins. If they have the same points then it's a push (aka a tie)
    if sum(dealer_cards.values()) <= 21 and sum(player_cards.values()) <= 21:

        if sum(dealer_cards.values()) > sum(player_cards.values()):
            print("Dealer cards: " + str(list(dealer_cards)) + " Total: " + str(sum(dealer_cards.values())) + ". Dealer wins.")
            dealer_wins += 1
            print("Player wins: " + str(player_wins) + ". Dealer wins: " + str(dealer_wins))
            player_cards.clear()
            dealer_cards.clear()
            return play_again()

        elif sum(dealer_cards.values()) == sum(player_cards.values()) and sum(player_cards.values()) != 0:
            print("Dealer cards: " + str(list(dealer_cards)) + " Total: " + str(sum(dealer_cards.values())) + ". Push")
            print("Player wins: " + str(player_wins) + ". Dealer wins: " + str(dealer_wins))
            player_cards.clear()
            dealer_cards.clear()
            return play_again()

        elif sum(dealer_cards.values()) < sum(player_cards.values()):
            print("Dealer cards: " + str(list(dealer_cards)) + " Total: " + str(sum(dealer_cards.values())) + ". You win.")
            player_wins += 1
            print("Player wins: " + str(player_wins) + ". Dealer wins: " + str(dealer_wins))
            player_cards.clear()
            dealer_cards.clear()
            return play_again()

        else:
            return "Goodbye."

    elif sum(dealer_cards.values()) > 21 and sum(player_cards.values()) <= 21:
        print("Dealer cards: " + str(list(dealer_cards)) + " Total: " + str(sum(dealer_cards.values())) + ". Dealer busts. You win.")
        player_wins += 1
        print("Player wins: " + str(player_wins) + ". Dealer wins: " + str(dealer_wins))
        player_cards.clear()
        dealer_cards.clear()
        return play_again()

    elif sum(dealer_cards.values()) <= 21 and sum(player_cards.values()) > 21:

        print("Bust! Dealer wins!")
        dealer_wins += 1
        print("Player wins: " + str(player_wins) + ". Dealer wins: " + str(dealer_wins))
        player_cards.clear()
        dealer_cards.clear()
        return play_again()

    

#This function runs through the dealer's drawing process after the player is done drawing 
def dealer_draw():

    #If the dealer has less than 17 points, they hit and that card is removed from the deck
    if sum(dealer_cards.values()) < 17:
        dealer_hit = random.choice(list(deck.items()))
        dealer_cards[dealer_hit[0]] = dealer_hit[1]
        deck.pop(dealer_hit[0])
        return dealer_draw()

    #If the dealer goes over 21 and does not have an Ace, then the function for deciding a winner is returned (in this case, the dealer busts)
    elif sum(dealer_cards.values()) > 21 and "Ace of Spades" not in dealer_cards.keys() and "Ace of Hearts" not in dealer_cards.keys() and "Ace of Diamonds" not in dealer_cards.keys() and "Ace of Clubs" not in dealer_cards.keys():
        return winner()

    #If the dealer gets 21, the function for deciding the winner is returned
    elif sum(dealer_cards.values()) == 21:
        return winner()

    #If a dealer has an Ace in their hand and goes over 21, the Ace's value gets adjusted down to 1
    elif sum(dealer_cards.values()) > 21 and ("Ace of Spades", 11) in dealer_cards.items():
        dealer_cards["Ace of Spades"] = 1
        print("Dealer cards: " + str(list(dealer_cards.keys())) + " Total: " + str(sum(dealer_cards.values())))
        return dealer_draw()

    elif sum(dealer_cards.values()) > 21 and ("Ace of Hearts", 11) in dealer_cards.items():
        dealer_cards["Ace of Hearts"] = 1
        print("Dealer cards: " + str(list(dealer_cards.keys())) + " Total: " + str(sum(dealer_cards.values())))
        return dealer_draw()

    elif sum(dealer_cards.values()) > 21 and ("Ace of Diamonds", 11) in dealer_cards.items():
        dealer_cards["Ace of Diamonds"] = 1
        print("Dealer cards: " + str(list(dealer_cards.keys())) + " Total: " + str(sum(dealer_cards.values())))
        return dealer_draw()

    elif sum(dealer_cards.values()) > 21 and ("Ace of Clubs", 11) in dealer_cards.items():
        dealer_cards["Ace of Clubs"] = 1
        print("Dealer cards: " + str(list(dealer_cards.keys())) + " Total: " + str(sum(dealer_cards.values())))
        return dealer_draw()
    
    #If the dealer has 17 or more, they stop hitting and the function to decide the winner is returned
    elif sum(dealer_cards.values()) >= 17:
        return winner()



#Play the hand
def play_hand():

    #First, the cards are dealt
    deal_cards()
    
    #Function to choose whether to hit or stand
    def hit_stand():
        hit_or_stand = input("Hit or stand? ").lower()

        if hit_or_stand == "stand" or hit_or_stand == "s":
            return dealer_draw()

        elif hit_or_stand == "hit" or hit_or_stand == "h":
            new_card = random.choice(list(deck.items()))
            player_cards[new_card[0]] = new_card[1]
            deck.pop(new_card[0])
            print("Player cards: " + str(list(player_cards.keys())) + " Total: " + str(sum(player_cards.values())))
            return player_choice()

        elif hit_or_stand != "hit" and hit_or_stand != "stand":
            print("Sorry, I didn't catch that.")
            return hit_stand()
                    
        else:
            return winner()

        return player_choice()


    #Play through the various possible scenarios
    def player_choice():
        
        #If the player has less than 21, then they choose to hit or stand
        if sum(player_cards.values()) < 21:
            return hit_stand()

        #If the player goes over 21 and does not have an Ace in their hand, the player busts
        elif sum(player_cards.values()) > 21 and "Ace of Spades" not in player_cards.keys() and "Ace of Hearts" not in player_cards.keys() and "Ace of Diamonds" not in player_cards.keys() and "Ace of Clubs" not in player_cards.keys():
            return winner()

        #If a player has gone over 21 and the Ace in their hand already has a value of 1, they bust
        elif sum(player_cards.values()) > 21 and ("Ace of Spades", 1) in player_cards.items() or ("Ace of Hearts", 1) in player_cards.items() or ("Ace of Diamonds", 1) in player_cards.items() or ("Ace of Clubs", 1) in player_cards.items():
            return winner()

        #This may superfluous to the first if statement in the function
        #elif sum(player_cards.values()) < 21 and ("Ace of Spades", 1) in player_cards.items() or ("Ace of Hearts", 1) in player_cards.items() or ("Ace of Diamonds", 1) #in player_cards.items() or ("Ace of Clubs", 1) in player_cards.items():
        #    return hit_stand()

        #If the player has 21, then the dealer draws
        elif sum(player_cards.values()) == 21:
            return dealer_draw()

        #If the player goes over 21 and has an Ace in their hand, the Ace's value becomes 1 and the player chooses whether to hit or stand
        elif sum(player_cards.values()) > 21 and ("Ace of Spades", 11) in player_cards.items():
            player_cards["Ace of Spades"] = 1
            print("Player cards, Ace adjusted down to 1: " + str(list(player_cards.keys())) + " Total: " + str(sum(player_cards.values())))
            return hit_stand()

        elif sum(player_cards.values()) > 21 and ("Ace of Hearts", 11) in player_cards.items():
            player_cards["Ace of Hearts"] = 1
            print("Player cards, Ace adjusted down to 1: " + str(list(player_cards.keys())) + " Total: " + str(sum(player_cards.values())))
            return hit_stand()

        elif sum(player_cards.values()) > 21 and ("Ace of Diamonds", 11) in player_cards.items():
            player_cards["Ace of Diamonds"] = 1
            print("Player cards, Ace adjusted down to 1: " + str(list(player_cards.keys())) + " Total: " + str(sum(player_cards.values())))
            return hit_stand()

        elif sum(player_cards.values()) > 21 and ("Ace of Clubs", 11) in player_cards.items():
            player_cards["Ace of Clubs"] = 1
            print("Player cards, Ace adjusted down to 1: " + str(list(player_cards.keys())) + " Total: " + str(sum(player_cards.values())))
            return hit_stand()

    
    return player_choice()


#Start playing
print(play_hand())

