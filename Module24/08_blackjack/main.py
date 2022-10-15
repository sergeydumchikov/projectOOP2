import random
class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.number_of_points = 0

    def add_card(self, card):
        self.cards_in_hand.append(card)

    def sum_points(self):
        summ = 0
        for (i, n) in self.cards_in_hand:
            if i.isdigit():
                summ += int(i)
            elif i == 'Ace':
                summ += 11
            else:
                summ += 10
        self.number_of_points = summ

    def info(self):
        print('NAME: {}\nCARDS: {}\nPOINTS: {}\n'.format(
            self.name, self.cards_in_hand, self.number_of_points
        ))


class Deck:
    deck = []

    def __init__(self, deck):
        self.deck = deck

    def give_card(self):
        new_card = self.deck[0]
        self.deck.pop(0)
        return new_card

    def shuffle(self):
        random.shuffle(self.deck)
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
colors = ['Spades', 'Hearts', 'Crosses', 'Diamonds']
my_deck = []
for card in cards:
    for color in colors:
        ap_card = card, color
        my_deck.append(ap_card)

new_deck = Deck(my_deck)
player_1 = Player('Sergey')
computer = Player('Comp')
new_deck.shuffle()
for _ in range(2):
    player_1.add_card(new_deck.give_card())
    computer.add_card(new_deck.give_card())

while True:
    new_deck.shuffle()
    player_1.sum_points()
    computer.sum_points()
    player_1.info()
    computer.info()
    if player_1.number_of_points > 21:
        print('СГОРЕЛ')
        break
    elif computer.number_of_points > 21:
        print('Ты победил')
        break
    ques = input('Еще? 1 - ДА\n 2 - НЕТ\n::::')
    if ques == '1':
        player_1.add_card(new_deck.give_card())
        computer.add_card(new_deck.give_card())
    elif ques == '2':
        if player_1.number_of_points > computer.number_of_points:
            winner = player_1.name
        elif player_1.number_of_points == computer.number_of_points:
            winner = 'НИЧЬЯ'
        else:
            winner = computer.name
        print('Победитель - {}'.format(winner))
        break
