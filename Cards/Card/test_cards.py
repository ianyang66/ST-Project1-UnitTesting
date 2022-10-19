
from cards import Card, Deck, play_war_game

class TestCard:

	# this is a "test"
	def test_create(self):
		card = Card()
		assert card.suit == "Diamonds"
		assert card.rank +1 == 3

	# Test that if you create a card with rank 12, its rank will be "Queen"
	def testCreateQueen(self):
		card = Card(rank = 12)
		assert card.rank == "Queen"

	# Test that if you create a card with rank 1, its rank will be "Ace"
	def testCreateAce(self):
		card = Card(rank = 1)
		assert card.rank == "Ace"

	# Test that if you create a card instance with rank 3, its rank will be 3
	def testCreateRank3(self):
		card = Card(rank = 3)
		assert card.rank == 3

	# Test that if you create a card instance with suit 1, it will be suit "Clubs"
	def testCreateSuitClubs(self):
		card = Card(suit = 1)
		assert card.suit == "Clubs"

	# Test that if you create a card instance with suit 2, it will be suit "Hearts"
	def testCreateSuitHearts(self):
		card = Card(suit = 2)
		assert card.suit == "Hearts"

	# Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	def testSuitNames(self):
		card = Card()
		assert card.suit_names == ["Diamonds","Clubs","Hearts","Spades"]

	# Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
	def testCardString1(self):
		card = Card(suit = 2, rank = 7)
		assert card.__str__() == "7 of Hearts"

	# Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"
	def testCardString2(self):
		card = Card(suit = 3, rank = 13)
		assert card.__str__() == "King of Spades"

	# Test that if you create a deck instance, it will have 52 cards in its cards instance variable
	def testDeckCards(self):
		deck = Deck()
		assert len(deck.cards) == 52

	# Test that if you invoke the pop_card method on a deck, it will return a card instance.
	def testPopCardInstance(self):
		deck = Deck()
		card = deck.pop_card()
		assert isinstance(card, Card)

	# Test that if you invoke the pop_card method on a deck, the deck has one fewer cards in it afterwards.
	def testPopCardFewer(self):
		deck = Deck()
		deck.pop_card()
		assert len(deck.cards) < 52

	# Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple assertions!)
	def testReturnValue(self):
		return_value = play_war_game(True)
		assert type(return_value) == tuple
		assert len(return_value) == 3
		assert type(return_value[0]) == str


	# (and 14)  Write at least 2 additional tests (not repeats of the above described tests). Make sure to include a descriptive message in these two so we can easily see what you are testing!
	def testShuffle1(self):
		deck = Deck() # create a deck
		deck.shuffle() # shuffle the deck
		assert isinstance(deck, Deck) # check if the deck is still an instance of Deck

	def testShuffle2(self):
		deck = Deck() # create a deck
		len_of_deck = len(deck.cards) # record the number of cards in deck before using shuffle()
		deck.shuffle() # shuffle the deck
		assert len(deck.cards) == len_of_deck # check if the number of cards in deck changes


