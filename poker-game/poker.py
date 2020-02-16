import random
used_cards = []


class Cards:
    '''Class returns particular cards, hands of players and deck'''

    value_list = (14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
    suit_list = ('clubs', 'diamonds', 'hearts', 'spades')

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
        self.player_hand = []
        i = 0
        while i < 2:
            player_card = self.getRandomCard()
            if player_card not in used_cards:
                self.player_hand.append(player_card)
                i += 1
                used_cards.append(player_card)
        print(self.player_hand)
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
        self.temp_list_value = []
        self.temp_list_colors = []
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

    def whatSuit(self):
        if self.isPoker(): return {9: 'Poker'}
        elif self.isFourOfKind(): return {8: 'Four of kind'}
        elif self.isFullHouse(): return {7: 'Full House'}
        elif self.isFlush(): return {6: 'Flush'}
        elif self.isStraight(): return {5: 'Straight'}
        elif self.isThreeOfKind(): return {4: 'Three Of Kind'}
        elif self.isTwoPairs(): return {3: 'Two Pairs'}
        elif self.isPair(): return {2: 'Pair'}
        else: return {1: 'Nothing'}

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

    def isPoker(self):
        values = self.isFlush()
        if values:
            for i in range(0, len(values) - 4):
                straight_list = []
                counter = 0
                for j in range(0, 4):
                    if (values[i + j]) - 1 == values[i + j + 1]:
                        counter += 1
                        straight_list.append(values[i + j])
                        continue
                    else:
                        break
                if counter == 4:
                    straight_list.append(values[i + 4])
                    return straight_list

    def isStraight(self):
        inside_list = sorted(self.temp_list_value, reverse=True)
        for i in range(0, 3):
            straight_list = []
            counter = 0
            for j in range(0, 4):
                if (inside_list[i+j]) - 1 == inside_list[i+j+1]:
                    counter += 1
                    straight_list.append(inside_list[i+j])
                    continue
                else:
                    break
            if counter == 4:
                straight_list.append(inside_list[i + 4])
                return straight_list

    def isFourOfKind(self):
        for i in self.value_dict:
            if self.value_dict[i] == 4:
                return i

    def isFullHouse(self):
        three_cards = 0
        two_cards = 0
        full_house_list = []
        for i in self.value_dict:
            if self.value_dict[i] == 3:
                three_cards = i
                full_house_list.append(three_cards)
            elif self.value_dict[i] == 2 and two_cards:
                if i > two_cards: i = two_cards
            elif self.value_dict[i] == 2:
                two_cards = i
        if three_cards and two_cards:
            full_house_list.append(two_cards)
            return full_house_list

    def isFlush(self):
        flush_value_list = []
        iteration = 0
        for i in self.colors_dict:
            if self.colors_dict[i] >= 5:
                for j in self.temp_list_colors:
                    if j == i:
                        flush_value_list.append(self.temp_list_value[iteration])
                    iteration += 1
                return sorted(flush_value_list, reverse=True)

    def isThreeOfKind(self):
        for i in self.value_dict:
            if self.value_dict[i] == 3:
                return i
        return False

    def isTwoPairs(self):
        two_pairs_list = []
        two_cards = False
        two_cards_2 = False
        for i in self.value_dict:
            if self.value_dict[i] == 2 and two_cards_2:
                two_cards = True
                two_pairs_list.append(i)
            if self.value_dict[i] == 2 and not two_cards_2:
                two_cards_2 = True
                two_pairs_list.append(i)
        if two_cards and two_cards_2:
            return sorted(two_pairs_list, reverse=True)

    def isPair(self):
        for i in self.value_dict:
            if self.value_dict[i] == 2:

                return i
        return False


def compare_five_cards(playerOneCardList, playerTwoCardsList):
    for i in range(6, 1, -1):
        if playerOneCardList.temp_list_value[i] == playerTwoCardsList.temp_list_value[i]:
            continue
        else:
            if playerOneCardList.temp_list_value[i] > playerTwoCardsList.temp_list_value[i]:
                print('Player One won!!!')
            elif playerOneCardList.temp_list_value[i] < playerTwoCardsList.temp_list_value[i]:
                print('Player Two won!!!')
            else:
                print('Error!!!')
            break


playerOneCards = Cards()
playerTwoCards = Cards()

deck = Cards()

current_deck = deck.getDeck()
print('Deck: {}'.format(current_deck))
playerOne = Suits(playerOneCards.getPlayerHand(), current_deck)
playerTwo = Suits(playerTwoCards.getPlayerHand(), current_deck)
playerOneSuit = playerOne.whatSuit()
playerTwoSuit = playerTwo.whatSuit()
print('Player One: {}'.format(list(playerOneSuit.values())[0]))
print('Player Two: {}'.format(list(playerTwoSuit.values())[0]))
player_one_seven_cards = playerOne.temp_list_value
player_two_seven_cards = playerTwo.temp_list_value
player_one_seven_cards_colors = playerOne.temp_list_colors
player_two_seven_cards_colors = playerTwo.temp_list_colors


player_one_score = list(playerOneSuit.keys())[0]
player_two_score = list(playerTwoSuit.keys())[0]

if player_one_score > player_two_score:
    print('Player One won!!!')
elif player_one_score < player_two_score:
    print('Player Two won!!!')
else:

    if player_one_score == 9:
        player_one_poker = playerOne.isPoker()
        player_two_poker = playerTwo.isPoker()

        if player_one_poker[0] > player_two_poker[0]:
            print('Player One won!!!')
        elif player_one_poker[0] < player_two_poker[0]:
            print('Player Two won!!!')
        elif player_one_poker[0] == player_two_poker[0]:
            print('Draw!!!')
        else:
            print('Poker error')

    if player_one_score == 8:
        player_one_four_of_kind = playerOne.isFourOfKind()
        player_two_four_of_kind = playerTwo.isFourOfKind()

        if player_one_four_of_kind > player_two_four_of_kind:
            print('Player One won!!!')
        elif player_one_four_of_kind < player_two_four_of_kind:
            print('Player Two won!!!')
        elif player_one_four_of_kind == player_two_four_of_kind:
            player_one_kicker = sorted([x for x in player_one_seven_cards if x is not player_one_four_of_kind], reverse=True)[0]
            player_two_kicker = sorted([x for x in player_two_seven_cards if x is not player_two_four_of_kind], reverse=True)[0]
            if player_one_kicker > player_two_kicker:
                print('Player One won!!!')
            elif player_one_kicker < player_two_kicker:
                print('Player Two won!!!')
            elif player_one_kicker == player_two_kicker:
                print('Draw!!!')

    if player_one_score == 7:
        player_one_full_house = playerOne.isFullHouse()
        player_two_full_house = playerTwo.isFullHouse()

        if player_one_full_house[0] > player_two_full_house[0]:
            print('Player One won!!!')
        elif player_one_full_house[0] < player_two_full_house[0]:
            print('Player Two won!!!')
        elif player_one_full_house[0] == player_two_full_house[0]:
            if player_one_full_house[1] > player_two_full_house[1]:
                print('Player One won!!!')
            elif player_one_full_house[1] < player_two_full_house[1]:
                print('Player Two won!!!')
            else:
                print('Draw!!!')

    if player_one_score == 6:
        player_one_flush = playerOne.isFlush()
        player_two_flush = playerTwo.isFlush()
        print(player_one_flush)
        print(player_two_flush)
        for i in range (0, 5):
            if player_one_flush[i] > player_two_flush[i]:
                print('Player One won!!!')
                break
            elif player_one_flush[i] < player_two_flush[i]:
                print('Player Two won!!!')
                break
            elif player_one_flush[i] == player_two_flush[i]:
                if i == 4:
                    print('Draw!!!')
            else:
                print('Error Flush')

    if player_one_score == 5:
        player_one_straight = playerOne.isStraight()
        player_two_straight = playerTwo.isStraight()
        print('Player One straight: {}'.format(player_one_straight))
        print('Player Two straight: {}'.format(player_two_straight))
        if player_one_straight[0] > player_two_straight[0]:
            print('Player One won!!!')
        elif player_one_straight[0] < player_two_straight[0]:
            print('Player Two won!!!')
        else:
            print('Draw!!!')

    if player_one_score == 4:
        player_one_three_of_kind = playerOne.isThreeOfKind()
        player_two_three_of_kind = playerTwo.isThreeOfKind()
        if player_one_three_of_kind > player_two_three_of_kind:
           print('Player One won!!!')
        elif player_one_three_of_kind < player_two_three_of_kind:
            print('Player Two won!!!')
        else:
            player_one_seven_cards = playerOne.temp_list_value
            player_two_seven_cards = playerTwo.temp_list_value
            player_one_kickers = sorted([x for x in player_one_seven_cards if x is not player_one_three_of_kind], reverse=True)
            player_two_kickers = sorted([x for x in player_two_seven_cards if x is not player_two_three_of_kind], reverse=True)
            if player_one_kickers[0] > player_two_kickers[0]:
                print('Player One won!!!')
            elif player_one_kickers[0] < player_two_kickers[0]:
                print('Player Two won!!!')
            else:
                if player_one_kickers[1] > player_two_kickers[1]:
                    print('Player One won!!!')
                elif player_one_kickers[1] < player_two_kickers[1]:
                    print('Player Two won!!!')
                else:
                    print('Draw!!!')

    if player_one_score == 3:
        player_one_pairs = playerOne.isTwoPairs()
        player_two_pairs = playerTwo.isTwoPairs()
        if player_one_pairs[0] > player_two_pairs[0]:
            print('Player One won!!!')
        elif player_one_pairs[0] < player_two_pairs[0]:
            print('Player Two won!!!')
        elif player_one_pairs[1] > player_two_pairs[1]:
            print('Player One won!!!')
        elif player_one_pairs[1] < player_two_pairs[1]:
            print('Player Two won!!!')
        else:
            player_one_seven_cards = playerOne.temp_list_value
            player_two_seven_cards = playerTwo.temp_list_value
            player_one_kicker = sorted([x for x in player_one_seven_cards if x not in player_one_pairs], reverse=True)[0]
            player_two_kicker = sorted([x for x in player_two_seven_cards if x not in player_two_pairs], reverse=True)[0]
            if player_one_kicker > player_two_kicker:
                print('Player One won!!!')
            elif player_one_kicker < player_two_kicker:
                print('Player Two won!!!')
            elif player_one_kicker == player_two_kicker:
                print('Draw!!!')
            else:
                print('Error two pairs ')

    if player_one_score == 2:
        if playerOne.isPair() > playerTwo.isPair():
            print('Player One won!!!')
        elif playerOne.isPair() < playerTwo.isPair():
            print('Player Two won!!!')
        else:
            compare_five_cards(playerOne, playerTwo)
    if player_one_score == 1:
        compare_five_cards(playerOne, playerTwo)



