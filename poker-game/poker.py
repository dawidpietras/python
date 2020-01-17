import random
used_cards = []


class Cards:

    value_list = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
    suit_list = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self.player_hand = []

    def getRandomCards(self):
        player_hand = []
        i = 0
        while i < 2:
            rand_suit = random.choice(self.suit_list)
            rand_value = random.choice(self.value_list)

            if rand_value not in used_cards and rand_suit not in used_cards:
                self.player_hand.append(rand_suit)
                self.player_hand.append(rand_value)
                i += 1
        used_cards.append(player_hand)
        return self.player_hand


playerOneCards = Cards().getRandomCards()
playerTwoCards = Cards().getRandomCards()
print('First Player Cards: {}  Second Player Cards: {}'.format(playerOneCards, playerTwoCards))
print(used_cards)
