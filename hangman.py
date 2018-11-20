import random

def replace_str_index(text,index=0,replacement=''):
    
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def start_hangman_game(number_of_wrong_attempts_left,hangman_answer,answer_guessed_so_far):

	right_char_list_indexes = []

	character_guesses = []

	while number_of_wrong_attempts_left !=0:

		print (f'Current letters guessed correctly so far: {answer_guessed_so_far}')
		
		print(f'Please make a guess by typing in one character of the alphabet (A to Z) and then press the "Enter" key on the keyboard (You have {number_of_wrong_attempts_left - 1} wrong attempts left):  ',end = "")

		char_guessed = input()

		if len(char_guessed) !=1 or char_guessed.isalpha() == False:
			
			print("Invalid entry!")
			
			continue

		char_guessed = char_guessed.upper().strip()

		if char_guessed in character_guesses:

			print(f'I am sorry, you already chose the character "{char_guessed}" and can not choose it again.')
			
			continue

		if char_guessed in hangman_answer:

			print(f'You guessed the letter "{char_guessed}" correctly.')

			counter = 0

			for char in hangman_answer:

				if char_guessed == char:

					right_char_list_indexes.append(counter)

				counter = counter + 1

			for i in right_char_list_indexes:

				answer_guessed_so_far = replace_str_index(answer_guessed_so_far,i,hangman_answer[i])

			character_guesses.append(char_guessed)

			if answer_guessed_so_far == hangman_answer:

				print(f'Congratulations! You won the game by filling in the characters of the following text: "{hangman_answer}"')
				
				return
		
		else:
			
			character_guesses.append(char_guessed)

			number_of_wrong_attempts_left = number_of_wrong_attempts_left - 1

			if number_of_wrong_attempts_left == 0:
				
				print('You lost the game! Better luck next time!')
				
				return
			
			print(f'I am sorry, the letter "{char_guessed}" is not present.')


def generate_hangman_answer(list_of_hangman_answers):

	number_of_hangman_answers_in_list = len(list_of_hangman_answers)

	random_index_in_hangman_list = random.randint(0,number_of_hangman_answers_in_list - 1)

	hangman_answer = list_of_hangman_answers[random_index_in_hangman_list]

	hangman_answer = hangman_answer.upper().strip()

	return hangman_answer

def insert_blank_where_blank_into_answer_guessed_so_far(hangman_answer):

	blank_char_list_indexes = []

	answer_guessed_so_far = '_' * len(hangman_answer)

	counter = 0

	for char in hangman_answer:

		if char.isspace():

			blank_char_list_indexes.append(counter)

		counter = counter + 1

	for i in blank_char_list_indexes:

		answer_guessed_so_far = replace_str_index(answer_guessed_so_far,i,' ')

	return answer_guessed_so_far


start_game = True

while start_game is True:

	print('Welcome to Hangman! Press any key (except "Q" and then press the "Enter" key to quit the program) and then press the "Enter" key on the keyboard to start a new game:   ', end="")

	char_chosen = input()

	char_chosen = char_chosen.upper().strip()

	if char_chosen == 'Q':

		exit()

	list_of_hangman_answers = ['boston','break the walls down']

	real_hangman_answer = generate_hangman_answer(list_of_hangman_answers)

	real_answer_guessed_so_far = insert_blank_where_blank_into_answer_guessed_so_far(real_hangman_answer)

	start_hangman_game(7,real_hangman_answer,real_answer_guessed_so_far)