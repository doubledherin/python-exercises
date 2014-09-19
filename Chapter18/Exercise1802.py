"""
Exercise 18.2. Write a Deck method named sort that uses the list 
method 'sort' to sort the cards in a Deck. 

sort uses the __cmp__ method we defined to determine sort order.
"""
import random

class Card(object):
	"""Represents a playing card."""

	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
					'Queen', 'King']

	def __init__(self, suit=0, rank=2): 	# the 2 of clubs
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "%s of %s" % (Card.rank_names[self.rank], 
							 Card.suit_names[self.suit])

	def __cmp__(self, other):
		tup1 = self.rank, self.suit
		tup2 = other.rank, other.suit
		return cmp(tup1, tup2)

class FullDeck(object):
	"""Represents a deck of 52 cards"""
	
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def __str__(self):
		result = []
		for card in self.cards:
			result.append(str(card))
		return '\n'.join(result)

	def pop_card(self, i=-1):
		return self.cards.pop(i)

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def sort(self):
		self.cards.sort()


queen_of_diamonds = Card(1, 12)
jack_of_diamonds = Card(1, 11)
deck = FullDeck()

if __name__ == '__main__':
	print queen_of_diamonds.suit, queen_of_diamonds.rank
	print queen_of_diamonds
	print cmp(queen_of_diamonds, jack_of_diamonds)  # 1
	print deck
	deck.shuffle()
	print deck
	deck.sort()
	print deck

