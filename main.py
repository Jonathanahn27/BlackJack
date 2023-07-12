import random
import time

def random_gen():
    size = 311
    random_number = random.randrange(0,size)
    size = size - 1
    return random_number

def create_deck():
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    tempdeck = []

    for suit in suits:
        for rank in ranks:
            card = f"{rank} of {suit}"
            tempdeck.append(card)

    return tempdeck

def card_value(card):
    cardlist = card.split()
    face = cardlist[0]
    if (face == "Ace"):
        return 10 #needs to be changed later
    elif(face == "King" or face == "Queen" or face == "Jack"):
        return 10
    else:
        return int(face)


def blackjack(balance,deck):
    bet = int(input("How much would you like to bet? "))
    if (bet > balance):
        while (bet > balance):
            bet = int(input("Insufficient funds, try again: "))
    
    if (balance - bet == 0):
        print("All in!")


    print("Thank you (your new balance is: " + str(balance - bet) + ")")
    print("\nshuffling and dealing cards... \n")
    time.sleep(3)

    randomnum1 = random_gen()
    firstcard = deck[randomnum1]
    del deck[randomnum1]

    randomnum2 = random_gen()
    dealersfirst = deck[randomnum2]
    del deck[randomnum2]


    print("++++++++++++++  You drew a " + firstcard + "  ++++++++++++++\n")
    time.sleep(1)
    print("--------------  House drew a card  --------------\n")
    time.sleep(1)

    print("dealing cards...\n")
    time.sleep(3)

    randomnum3 = random_gen()
    secondcard = deck[randomnum3]
    del deck[randomnum3]
    
    randomnum4 = random_gen()
    dealerssecond = deck[randomnum4]
    del deck[randomnum4]

    print("++++++++++++++  You drew a " + secondcard + "  ++++++++++++++\n")
    time.sleep(2)
    print("--------------  House drew a " + dealerssecond + "  --------------  \n")
    time.sleep(2)

    hand = []
    hand.append(firstcard)
    hand.append(secondcard)

    househand = []
    househand.append(dealersfirst)
    househand.append(dealerssecond)

    playervalue = play(hand,deck)

    print("------  House has a " + dealersfirst + "and a " + dealerssecond + "  ------\n")
    time.sleep(2)
    end = houseplay(househand, playervalue,deck)

    if (end == "won"):
        return balance + bet
    elif (end == "lost"):
        return balance - bet
    elif (end == "draw"):
        return balance

def houseplay(hand,playervalue,deck):
    value = 0
    for card in hand:
        value = value + card_value(card)

    while (value < playervalue) and (value < 22):
        randomnum = random_gen()
        newcard = deck[randomnum]
        del deck[randomnum]
        print("--------------House drew a " + newcard + "  --------------\n")
        time.sleep(1.5)
        value = value + card_value(newcard)
    if (value > 21):
        print("$$$$$$$$$$$$$$  House busted, you win!  $$$$$$$$$$$$$$\n")
        return "won"
    elif(value < 22):
        print(",,,,,,,,,  House won  ,,,,,,,,,\n")
        return "lost"
    elif(value == playervalue):
        print(",,,,,,,,,,  You and House drew  ,,,,,,,,,,")
        return "draw"

def play(hand, deck):
    value = 0
    for card in hand:
        value = value + card_value(card)
    while value < 22:
        dec = input("Would you like to hit or stay? ")
        print("\n")
        if (dec == "hit"):
            time.sleep(1)
            randomnum = random_gen()
            newcard = deck[randomnum]
            del deck[randomnum]
            print("++++++++++++++  You drew a " + newcard + "++++++++++++++  \n")
            value = value + card_value(newcard)
            if(value == 21):
                print("~~~~~~~~~~~~~~~~~  Blackjack!  ~~~~~~~~~~~~~~~~~ \n")
                return value

        else:   
            return value
        
    print(".............  You busted, you lose  .............\n")
    return -1


def newdeck():
    deck = create_deck()
    count = 5
    while (count > 5):
        newdeck = create_deck()
        deck = deck + newdeck
        count = count - 1
    return deck

def main():
    deck = create_deck()
    balance = int(input("Hello, please deposit money for your balance: "))
    count = 5
    while (count > 0): 
        new_deck = create_deck()
        deck = deck + new_deck
        count = count - 1
    while (balance > 0):
        balance = blackjack(balance, deck)
        print("Your new balance is: " + str(balance))
        cont = input("Would you like to continue playing?")
        if (cont == "no"):
            print("You deposited: " + str(balance))
            break
        else:
            deck = newdeck()

if __name__ == "__main__":
    main()
