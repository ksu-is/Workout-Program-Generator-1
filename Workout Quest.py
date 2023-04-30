import random
import json
import os

class Player:
	def __init__(self, name):
		self.name = name
		self.level = 1
		self.strength = 10
		self.stamina = 10
		self.experience = 0

	def level_up(self):
		self.level += 1
		self.strength += 4
		self.stamina += 2
		print(f'Congratulations, you leveled up to level {self.level}!')

	def show_stats(self):
		print(f'Name: {self.name}')
		print(f'Level: {self.level}')
		print(f'Strength: {self.strength}')
		print(f'Stamina: {self.stamina}')
		print(f'Experience: {self.experience}')

exercises = ['Push-ups', 'Sit-ups', 'Squats', 'Lunges', 'Plank', 'Quit']

def select_exercise():
	return random.choice(exercises)

def load_player(name):
	if not os.path.exists('players.json'):
		return None

	with open('players.json', 'r') as file:
		players = json.load(file)

	if name in players:
		player_data = players[name]
		player = Player(name)
		player.level = player_data['level']
		player.strength = player_data['strength']
		player.stamina = player_data['stamina']
		player.experience = player_data['experience']
		return player
	return None

def save_player(player):
	if os.path.exists('players.json'):
		with open('players.json', 'r') as file:
			players = json.load(file)
	else:
		players = {}

	players[player.name] = {
		'level': player.level,
		'strength': player.strength,
		'stamina': player.stamina,
		'experience': player.experience
	}

	with open('players.json', 'w') as file:
		json.dump(players, file)

def start_game():
	name = input('Enter your name: ')
	player = load_player(name)

	if player:
		print(f'Welcome back, {player.name}!')
		choice = input('Do you want to continue (C) or delete and start over (D)? ').lower()
		if choice == 'd':
			player = Player(name)
	else:
		player = Player(name)

	while True:
		player.show_stats()

		print('\nWhich exercise would you like to do today?')
		for i, exercise in enumerate(exercises):
			print(f'{i + 1}. {exercise}')

		choice = input('> ')

		if choice.isdigit() and int(choice) in range(1, len(exercises) + 1):
			exercise = exercises[int(choice) - 1]
			if exercise == 'Quit':
				break
			reps = int(input(f'How many reps of {exercise} do you want to do? '))
			print(f'You chose to do {reps} reps of {exercise}!')

			if exercise == 'Push-ups':
				experience = reps
				strength = 0.33 * reps
				stamina = 0.1 * reps
			elif exercise == 'Sit-ups':
				experience = reps
				strength = 0.25 * reps
				stamina = 0.1 * reps
			elif exercise == 'Squats':
				experience = reps
				strength = 0.2 * reps
				stamina = 0.1 * reps
			elif exercise == 'Lunges':
			  experience = reps
			  strength = 0.2 * reps
			  stamina = 0.05 * reps
			elif exercise == 'Plank':
					experience = reps
					strength = 0.1 * reps
					stamina = 0.2 * reps
			player.experience += experience
			player.strength += strength
			player.stamina += stamina
			if player.experience >= 10 * player.level:
					player.level_up()
			elif choice.lower() == 'quit':
				break
			else:
				print('Invalid choice.')

			save_player(player)
			print(f'Thanks for playing, {player.name}!')
			
start_game()
