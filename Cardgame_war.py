import random

values = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
    "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
    "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
}

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.suit + ' of ' + self.rank


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                createobj = Card(suit, rank)
                self.all_cards.append(createobj)
        random.shuffle(self.all_cards)
        random.shuffle(self.all_cards)
        random.shuffle(self.all_cards)

class Game:
    def __init__(self, p1, p2):
        deck = Deck()
        self.player1 = deck.all_cards[:26]
        self.player2 = deck.all_cards[26:]
        self.collector = []
        self.game_On = True
        self.count = 1
        i = 0
        j = 0
        while self.game_On:
            print(f"Round {self.count}")
            if len(self.player1) == 0:
                print(f"Player {p2} wins")
                self.game_On = False
                break
            if len(self.player2) == 0:
                print(f"Player {p1} wins")
                self.game_On = False
                break
            if len(self.player1) <= i:
                i = 0
                continue
            if len(self.player2) <= j:
                j = 0
                continue
            value_p1 = self.player1[i].value
            value_p2 = self.player2[j].value
            if value_p2 > value_p1:
                self.player2.append(self.player1[i])
                del self.player1[i]
                if len(self.collector) != 0:
                    self.player2.extend(self.collector)
                    self.collector = []
                if i != 0:
                    i -= 1
            elif value_p2 < value_p1:
                self.player1.append(self.player2[j])
                del self.player2[j]
                if len(self.collector) != 0:
                    self.player1.extend(self.collector)
                    self.collector = []
                if j != 0:
                    j -= 1
            else:  # value_p2 == value_p1
                self.collector.extend([self.player1[i], self.player2[j]])
                del self.player1[i]
                del self.player2[j]
                if i != 0:
                    i -= 1
                if j != 0:
                    j -= 1
            self.count += 1


p1 = input("Enter the player 1 name: ")
p2 = input("Enter the player 2 name: ")
g = Game(p1, p2)
