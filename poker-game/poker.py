import random
used_cards = []


class Cards:
    '''
    Class returns particular cards, hands of players and deck
    '''

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
    pass


playerOneCards = Cards().getPlayerHand()
playerTwoCards = Cards().getPlayerHand()
print('First Player Cards: {}  Second Player Cards: {}'.format(playerOneCards, playerTwoCards))
deck = Cards().getDeck()
print('Current Deck: {}'.format(deck))
print('Used Cards: {}'.format(used_cards))

