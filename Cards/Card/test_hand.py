from cards import Card, Deck, play_war_game
from Hand import Hand


class TestHand:

	# Test that a hand is initialized properly.
	def testHandInit(self):
		card_list = [] # create a list of cards
		for n in range(5):
			card_list.append(Card()) # create 5 cards and add to the card_list
		hand = Hand(card_list) # the Card class takes the list as its params
		assert hand.cards == card_list
		assert isinstance(hand, Hand)

	# Test that add_card( ) and remove_card( ) behave as specified
	def testAddAndRemove(self):
		card_list = []
		for n in range(5):
			card_list.append(Card())
		hand = Hand(card_list)
		card = Card()

		# test add_card()
		hand_add = hand.add_card(card) # add the card
		assert card in hand.cards # check if the card is in the list

		# test remove_card()
		hand_remove = hand.remove_card(card) # remove the card
		assert card not in hand.cards # check if the card is still in the list
        

	# Test that draw( ) works as specified. Test side effects as well.
	def testDraw(self):
		card_list = []
		for n in range(5):
			card_list.append(Card())
		hand = Hand(card_list) # create a hand
		len_hand = len(hand.cards) # record the number of cards in hand before using draw()
		deck = Deck() # create a deck
		len_deck = len(deck.cards) # record the number of cards in deck before using draw()

		# test draw()
		hand.draw(deck)
		assert len(hand.cards) == len_hand + 1 # one card should be added to the hand

		# test the side effect
		assert len(deck.cards) == len_deck - 1 # the deck should be depleted by one card
