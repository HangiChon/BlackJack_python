import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
		  'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

### Class Definitions, to be run only when imported ###

if __name__ == '__main__':
	print('')

else:
	#print('being imported')
	import random

	suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
	ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
	values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
			  'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

	class Card:
		
		def __init__(self, suit, rank):
			self.suit = suit
			self.rank = rank
			self.value = values[rank]
			
		
		def __str__(self):
			return f"{self.rank} of {self.suit}"
	
	
	class Deck:
		
		def __init__(self):
			self.deck = []  						# start with an empty list
			for suit in suits:
				for rank in ranks:
					self.deck.append(Card(suit,rank))
		
		def __str__(self):
			card_comp = '' 							# start with an empty string
			count += 1     							# to illustrate card count
	
			for card in self.deck:
				card_comp += count.__str__() + ' ' + card.__str__() + '/n'
				count += 1
	
			return card_comp
	
		def shuffle(self):
			random.shuffle(self.deck)
			
		def deal(self):
			single_card = self.deck.pop()
			return single_card  					# recommended to assign self.deck.pop() to a variable for return 
													# instead of returning self.deck.pop() itself
	
	
	class Hand:
	
		def __init__(self):
			self.cards = []  						# start with an empty list as in the Deck class
			self.value = 0	 						# start with zero
			self.aces = 0	 						# additional attribute to keep track of aces
	
		def add_card(self,card):
			self.cards.append(card)
			self.value += values[card.rank]    		# card = Card(), card is an instance of 'class Card' passed as an argument of add_card
													# by adding .rank to indicate that card belongs to class Card
													# https://stackoverflow.com/questions/19993795/how-would-i-access-variables-from-one-class-to-another
			if card.rank == 'Ace':
				self.aces += 1
		'''return card.__str__() to see what card comes in'''
	
		def adjust_for_ace(self):              	# not if, use while?
			while self.value > 21 and self.aces: 	# and self.aces = when self.aces is true?
				self.value -= 10                 	# ace already in hand used as 11, now to 1
				self.aces -= 1                   	# in case of having 2 aces, use 1
	
	
	class Chips:
	
		def __init__(self):							# def __init__(self, total=100)
			self.total = 100						# 	self.total = total
			self.bet = 0 							#	self.bet = 0				
													# this will allow us pass in on override value when obj is created
													# rather than wait until later to change it
		def win_bet(self):
			self.total += self.bet
	
		def lose_bet(self):
			self.total -= self.bet
	
	
	### Function Definitions ###
	
	def take_bet(chips):                            			# to test, it must be take_bet(Chips()), in game it will be
																# player_chips = Chips() then, take_bet(player_chips)
		while True:
			try:
				chips.bet = int(input('How many chips would you like to bet? '))
			except ValueError:
				print('Sorry, a bet must be an integer!')
			else:
				if chips.bet > chips.total:
					print("Sorry, your bet can't exceed ", chips.total)
				else:
					break
	
	
	def hit(deck,hand): 										# hit(deck=Deck(),hand=Hand()) to test
	
		hand.add_card(deck.deal())
		hand.adjust_for_ace()
	
	
	def hit_or_stand(deck,hand):
	
		global playing
	
		while True:
			result = input("Enter 'h' to hit or 's' to stand! ")
	
			if result[0].lower() == 'h':						# result[0] in case entered 'hit' or 'stand', attention to lower()
				hit(deck,hand)
	
			elif result[0].lower() == 's':
				print("Player stands, Dealer's turn!")
				playing = False
	
			else:
				print("Please enter correctly!")
				continue

			break

	
	
	# displaying card 
	
	''' simply write show functions rather than going procedural, like values > or < 17 then show'''
	def show_some(player,dealer):								# showing only dealer's second card -> dealer.cards[1] / sep -> separated by
	    print("\nDealer's hand: \n")							# Asterisk * symbol is used to print every item in collection
	    print("'hidden card'", dealer.cards[1], sep='\n')  		# showing only first dealer's card / sep -> separated by	# if you want to concatenate str version of each cards added,
	    print("\nPlayer's hand: \n", *player.cards, sep='\n')	# you need to print dealer.cards[1].__str__() for each index added
	    														# dealer.cards[0].__str__() can be used to check if 1st card is properly hidden
	def show_all(player,dealer):
	    print("\nDealer's hand: \n", *dealer.cards, sep='\n')
	    print("Dealer's total value: ", dealer.value, '\n')
	    print("Player's hand: \n", *player.cards, sep='\n')
	    print("Player's total value: ", player.value)
	
	
	# handle end of game scenarios								Don't put any condition as > 21, < 21. Simply show what each function outputs
	def player_busts(player,dealer,chips):
	    print(f"\n***Player busts with {player.value}")
	    chips.lose_bet()   
	
	def player_wins(player,dealer,chips):
	    print("\n***Player wins!")
	    chips.win_bet()
	
	def dealer_busts(player,dealer,chips):
	    print(f"\n***Dealer busts with {dealer.value}")
	    chips.win_bet()
	    
	def dealer_wins(player,dealer,chips):
	    print("\n***Dealer wins!")
	    chips.lose_bet()
	    
	def push(player,dealer):
	    print("\n***Player and Dealer tie, it's a push!")
	