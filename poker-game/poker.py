import random
used_cards = []


class Cards:
    '''Class returns particular cards, hands of players and deck'''

    value_list = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
    suit_list = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self.player_hand = []

    def getRandomCard(self):
        card = []  # one card e.g ['spades', 'A']
        rand_suit = random.choice(self.suit_list)
        rand_value = random.choice(self.value_list)
        card.append(rand_suit)
        card.append(rand_value)
        return card

    def getPlayerHand(self):
        i = 0
        while i < 2:
            player_card = self.getRandomCard()
            if player_card not in used_cards:
                self.player_hand.append(player_card)
                i += 1
                used_cards.append(player_card)
        return self.player_hand  # two cards, entire hand like [['spades', 'A'], ['diamonds', 'A']]

    def getDeck(self):
        deck = []  # list of 5 cards deck [['hearts', 9],['diamonds', 'K'],['clubs', 'J'],['clubs', 'A'],['clubs', 'Q']]
        i = 0
        while i < 5:
            deck_card = self.getRandomCard()
            if deck_card not in used_cards:
                deck.append(deck_card)
                i += 1
                used_cards.append(deck_card)
        return deck


class Suits:
    temp_list_value = []
    temp_list_colors = []

    def __init__(self, player_hand, deck_class):
        self.player_hand = player_hand
        self.deck = deck_class
        for i in self.deck:
            self.temp_list_value.append(i[1])
            self.temp_list_colors.append(i[0])
        for i in self.player_hand:
            self.temp_list_value.append(i[1])
            self.temp_list_colors.append(i[0])
        self.value_dict = self.valueSuits()
        self.colors_dict = self.colorSuits()
        print(self.value_dict)
        print(self.colors_dict)

    def colorSuits(self):
        dict_of_colors = {}
        for i in self.temp_list_colors:
            dict_of_colors.update({i: self.temp_list_colors.count(i)})
        return dict_of_colors

    def valueSuits(self):
        dict_of_values = {}
        for i in self.temp_list_value:
            dict_of_values.update({i: self.temp_list_value.count(i)})
        return dict_of_values

    def isFourOfKind(self):
        for i in self.value_dict:
            if self.value_dict[i] == 4:
                return True
        return False

    def isFullHouse(self):
        three_cards = False
        two_cards = False
        for i in self.value_dict:
            if self.value_dict[i] == 3:
                three_cards = True
            if self.value_dict[i] == 2:
                two_cards = True
        if three_cards and two_cards:
            return True
        else:
            return False

    def isFlush(self):
        for i in self.colors_dict:
            if self.colors_dict[i] == 5:
                return True
        return False

    def isTreeOfKind(self):
        for i in self.value_dict:
            if self.value_dict[i] == 3:
                return True
        return False

    def isTwoPairs(self):
        two_cards = False
        two_cards_2 = False
        for i in self.value_dict:
            if self.value_dict[i] == 2 and two_cards_2:
                two_cards = True
            if self.value_dict[i] == 2:
                two_cards_2 = True
        if two_cards and two_cards_2:
            return True
        else:
            return False

    def isPair(self):
        for i in self.value_dict:
            if self.value_dict[i] == 2:
                return True
        return False


playerOneCards = Cards().getPlayerHand()
playerTwoCards = Cards().getPlayerHand()
print('First Player Cards: {}  Second Player Cards: {}'.format(playerOneCards, playerTwoCards))
deck = Cards().getDeck()
print('Current Deck: {}'.format(deck))
print('Used Cards: {}'.format(used_cards))

deck = [['diamonds', 1], ['diamonds', 7], ['diamonds', 6], ['hearts', 8], ['spades', 4]]
x = [['diamonds', 9], ['diamonds', 2]]
suit = Suits(x, deck).isFlush()

print(suit)
