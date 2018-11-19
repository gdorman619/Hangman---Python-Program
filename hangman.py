import random

def replace_str_index(text,index=0,replacement=''):
    
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

list_of_hangman_answers = ['boston','break the walls down']

number_of_hangman_answers_in_list = len(list_of_hangman_answers)

character_guesses = []

random_index_in_hangman_list = random.randint(0,number_of_hangman_answers_in_list - 1)

hangman_answer = list_of_hangman_answers[random_index_in_hangman_list]

hangman_answer = hangman_answer.upper().strip()

right_char_list_indexes = []

blank_char_list_indexes = []

#print(hangman_answer)

answer_guessed_so_far = '_' * len(hangman_answer)

counter = 0

for char in hangman_answer:

	if char.isspace():

		blank_char_list_indexes.append(counter)

	counter = counter + 1

for i in blank_char_list_indexes:

			answer_guessed_so_far = replace_str_index(answer_guessed_so_far,i,' ')

number_of_wrong_attempts_left = 7

while number_of_wrong_attempts_left !=0:

	print (f'Current letters guessed correctly so far: {answer_guessed_so_far}')
	
	print(f'Please make a guess by typing in one character of the alphabet. You have {number_of_wrong_attempts_left - 1} wrong attempts left.  ',end = "")

	char_guessed = input()

	if len(char_guessed) !=1 or char_guessed.isalpha() == False:
		
		print("Invalid entry!")
		
		continue

	char_guessed = char_guessed.upper().strip()

	if char_guessed in character_guesses:

		print("You already chose this character and can't choose it again.")
		
		continue

	if char_guessed in hangman_answer:

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
			
			exit()

	
	else:
		
		number_of_wrong_attempts_left = number_of_wrong_attempts_left - 1

		if number_of_wrong_attempts_left == 0:
			
			print('You lose! Game over!')
			
			exit()
		
		print(f'You chose a wrong character.')