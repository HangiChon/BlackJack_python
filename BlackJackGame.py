from BLJK_Classes_Funcs import main_classes_funcs
from IPython.display import clear_output

P_chips = main_classes_funcs.Chips()
playing = True
name = input("Enter your name and press enter.")

while True:


	# Print an opening statement
	print(f"{name}, Welcome to BlackJack Game!")
	
	# Create & shuffle the deck, deal two cards to each player
	my_deck = main_classes_funcs.Deck()
	my_deck.shuffle()
	Player = main_classes_funcs.Hand()
	Dealer = main_classes_funcs.Hand()
	Player.add_card(my_deck.deal())
	Dealer.add_card(my_deck.deal())
	Player.add_card(my_deck.deal())
	Dealer.add_card(my_deck.deal())
	#playing = False
	
	# Set up the Player's chips
	#P_chips = Chips()
	#D_chips = Chips()
	
	# Prompt the Player for their bet
	main_classes_funcs.take_bet(P_chips)
	
	# Show cards (but keep one dealer card hidden)
	main_classes_funcs.show_some(Player,Dealer)
	print(f'Player value = {Player.value}')
	
	while playing:
		
		if Player.value == 21:
			main_classes_funcs.player_wins(Player,Dealer,P_chips)
			clear_output()
			main_classes_funcs.show_all(Player,Dealer)
			print("\nPlayer hits BlackJack!")
			break
			
		#hit_or_stand(my_deck,Player) global boolean error so procedural approach needed as below:

		p = input(f"{name}, Press 'h' to hit or 's' to stand. ")

		main_classes_funcs.show_some(Player,Dealer)
		print(f'Player value = {Player.value}')
		
		if p[0].lower() == 'h':
			main_classes_funcs.hit(my_deck,Player)

			if Player.value < 21:
				main_classes_funcs.show_some(Player,Dealer)
				print(f'Player value = {Player.value}')
				continue
				
			elif Player.value == 21:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.player_wins(Player,Dealer,P_chips)
				print("\nPlayer hits BlackJack!")
				break
				
			elif Player.value > 21:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.player_busts(Player,Dealer,P_chips)
				break

		elif p[0].lower() == 's':
			playing = False
			print("\n***Dealer's Turn!")
		
	while not playing:  
		
		if Dealer.value == 21 and Player.value == 21:
			main_classes_funcs.player_wins(Player,Dealer,P_chips)
			print("\nBoth hit BlackJack!")
			break
		
		elif Dealer.value == 21 and Player.value != 21:
			main_classes_funcs.dealer_wins(Player,Dealer,P_chips)
			print("\nDealer hit BlackJack!")
			break
			
		clear_output()
		main_classes_funcs.show_all(Player,Dealer)
		#print("\n***Dealer's Turn!")
		
		a = input("Dealer, Press 'h' to hit or 's' to stand. ")
		if a[0].lower() == 'h':
			main_classes_funcs.hit(my_deck,Dealer)

			if Dealer.value < 17:
				continue

			elif Dealer.value == 21:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.dealer_wins(Player,Dealer,P_chips)
				print("\nDealer hits BlackJack!")
				break

			elif Dealer.value <= 21 and Dealer.value > Player.value:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.dealer_wins(Player,Dealer,P_chips)
				break

			elif Dealer.value <= 21 and Dealer.value < Player.value:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.player_wins(Player,Dealer,P_chips)
				break

			elif Dealer.value > 21:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.dealer_busts(Player,Dealer,P_chips)
				break

			elif Player.value == Dealer.value:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.push(Player,Dealer)
				break
				
		elif a[0].lower() == 's':
			
		
			#hit_or_stand(my_deck,Dealer)

			if Dealer.value < 17:
				continue

			elif Dealer.value == 21:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.dealer_wins(Player,Dealer,P_chips)
				print("\nDealer hits BlackJack!")
				break

			elif Dealer.value <= 21 and Dealer.value > Player.value:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.dealer_wins(Player,Dealer,P_chips)
				break

			elif Dealer.value <= 21 and Dealer.value < Player.value:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.player_wins(Player,Dealer,P_chips)
				break

			elif Dealer.value > 21:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.dealer_busts(Player,Dealer,P_chips)
				break

			elif Player.value == Dealer.value:
				clear_output()
				main_classes_funcs.show_all(Player,Dealer)
				main_classes_funcs.push(Player,Dealer)
				break
	
	
	print(f"\nPlayer's total chips: {P_chips.total}")
	playing = False


	again = input("Would you like to play again? (y/n)")

	if again[0].lower() == 'y':
		if P_chips.total == 0:
			clear_output()
			print("We give you 100 chips!")
			P_chips.total = 100
			playing = True
			continue
		
		elif P_chips.total != 0:
			clear_output()
			playing = True
			continue
			
		continue

	elif again[0].lower() == 'n':
		print("Thanks for playing!")
		break

	break