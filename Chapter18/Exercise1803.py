"""
Exercise 18.3
Write a Deck method called deal_hands that takes two parameters, the number of
hands and the number of cards per hand, and that creates new Hand objects, deals 
the appropriate number of cards per hand, and returns a list of Hand objects.
"""

import random

class Card(object):
	"""Represents a playing card."""

	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [ None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
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
	"""Represents a deck of 52 cards."""
	
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

	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())

	def deal_hands(self, num_hands=0, num_cards=0):
		hands =[]
		for i in range(num_hands):
			hand = Hand('hand%s' % i)
			for j in range(num_cards):
				hand.add_card(self.pop_card())
			hands.append(hand)
		return hands

class Hand(FullDeck):
	"""Represents a hand of cards"""

	def __init__(self, label=''):
		self.cards = []
		self.label = label





queen_of_diamonds = Card(1, 12)
jack_of_diamonds = Card(1, 11)
deck = FullDeck()
hand = Hand('new hand')

if __name__ == '__main__':
	deck.shuffle()
	hands = deck.deal_hands(4, 7)
	for hand in hands:
		print hand.label + '\n', hand
