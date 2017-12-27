
import random
from random import shuffle

class Deck:

    ranks = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"}

    suits = {"\u2660","\u2661","\u2662","\u2663"}

    def __init__(self):
        "initialize deck of 52 cards"
        self.deck = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append((rank,suit))
        
    
    def point(self):
        card = self.deck.pop()
        if card[0] in {"2","3","4","5","6","7","8","9","10"}:
            D = {card: int(card[0])}
        elif card[0] in {"J","Q","K"}:
            D = {card: 10}
        elif card[0] == "A":
            D = {card: random.randrange(1,12,10)}
        return D
        

    def shuffle(self):
        shuffle(self.deck)



deck = Deck()

def blackjack():
    flag = True
    result = True
    while flag:
        if result:
            deck.shuffle()
            player = {}
            computer = {}
            for i in range(2):
                player.update(deck.point())
                computer.update(deck.point())
            global player
            global computer
            print('player:',player)
            print('computer:',list(computer)[-1])
            player_deal()
            print()
            computer_deal()
            print()
            compare()
            print()
        
        answer = input("Do you want to play again? ")
        if answer.lower() == "yes":
            flag = True
            result = True
        elif answer.lower() == "no":
            print("Thank you for playing")
            flag = False
            result = True
        else:
            print("please print yes or no ")
            result = False

      
def player_deal():
    flag = True
    while flag:
        Answer = input("Hit or stand? ")
        if Answer.lower() == "hit":
            player.update(deck.point())
            print(player)
        elif Answer.lower() == "stand":
            flag = False
        else:
            print("Please print hit or stand")
    
    print("player")
    for i in player.keys():
        print(i,end="  ")

    print(point_pla())

def computer_deal():
    point_com()
    if point_com() > 17:
        print("computer")
        for i in list(computer):
            print(i,end="  ")
        print(point_com())
    
    else:
        while point_com() < 17:
            computer.update(deck.point())
            point_com()
        print("computer")
        for i in list(computer):
            print(i,end="  ")
        point_com()
        print(point_com())


def point_com():
    point_computer = 0
    for card in computer:
        point_computer += computer[card]
    return point_computer

def point_pla():
    point_player = 0
    for card in player:
        point_player += player[card]
    return point_player    

def compare():
    if point_pla() > 21:
        print("Busted!")
        print("Computer wins!")
    elif point_pla() <= 21:
        if point_com() > 21:
            print("YOU WIN!")
        elif abs(point_pla()-21) < abs(point_com()-21):
            print("YOU WIN!!")
        elif abs(point_pla()-21) > abs(point_com()-21):
            print("Computer wins!")
        elif point_pla() == point_com():
            print("play even")
    else:
        print("Computer wins!")

blackjack()

if __name__ == "__main__":
    game = GameController()
    game.start()
    
