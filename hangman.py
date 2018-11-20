import random

def replace_str_index(text,index=0,replacement=''):
    
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def start_hangman_game(number_of_wrong_attempts_left,hangman_answer,answer_guessed_so_far):

	right_char_list_indexes = []

	character_guesses = []

	while number_of_wrong_attempts_left !=0:

		print (f'Current letters guessed correctly so far: {answer_guessed_so_far}   (You have {number_of_wrong_attempts_left - 1} wrong attempts left.)')
		
		print()

		print(f'Please make a guess by typing in one character of the alphabet (A to Z) and then press the "Enter" key on the keyboard:  ',end = "")

		char_guessed = input()

		if len(char_guessed) !=1 or char_guessed.isalpha() == False:

			print()
			
			print("Invalid entry!")

			print()
			
			continue

		char_guessed = char_guessed.upper().strip()

		if char_guessed in character_guesses:

			print()

			print(f'I am sorry, you already chose the character "{char_guessed}" and can not choose it again.')
			
			print()

			continue

		if char_guessed in hangman_answer:

			print()

			print(f'You guessed the letter "{char_guessed}" correctly.')

			print()

			counter = 0

			for char in hangman_answer:

				if char_guessed == char:

					right_char_list_indexes.append(counter)

				counter = counter + 1

			for i in right_char_list_indexes:

				answer_guessed_so_far = replace_str_index(answer_guessed_so_far,i,hangman_answer[i])

			character_guesses.append(char_guessed)

			if answer_guessed_so_far == hangman_answer:

				print()

				print(f'Congratulations! You won the game by filling in the characters of the following text: "{hangman_answer}"')

				print()
				
				return
		
		else:
			
			character_guesses.append(char_guessed)

			number_of_wrong_attempts_left = number_of_wrong_attempts_left - 1

			if number_of_wrong_attempts_left == 0:

				print()
				
				print('You lost the game! Better luck next time!')

				print()
				
				return
			
			print()

			print(f'I am sorry, the letter "{char_guessed}" is not present.')

			print()


def generate_hangman_answer(list_of_hangman_answers):

	number_of_hangman_answers_in_list = len(list_of_hangman_answers)

	random_index_in_hangman_list = random.randint(0,number_of_hangman_answers_in_list - 1)

	hangman_answer = list_of_hangman_answers[random_index_in_hangman_list]

	hangman_answer = hangman_answer.upper().strip()

	return hangman_answer

def insert_blank_where_blank_into_answer_guessed_so_far(hangman_answer):

	blank_char_list_indexes = []

	answer_guessed_so_far = '*' * len(hangman_answer)

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

	print()

	print('Welcome to Hangman! Press any key (except "Q" and then press the "Enter" key to quit the program) and then press the "Enter" key on the keyboard to start a new game:   ', end="")

	char_chosen = input()

	print()

	char_chosen = char_chosen.upper().strip()

	if char_chosen == 'Q':

		exit()

	list_of_hangman_answers = ["boston","break the walls down","abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]

	real_hangman_answer = generate_hangman_answer(list_of_hangman_answers)

	real_answer_guessed_so_far = insert_blank_where_blank_into_answer_guessed_so_far(real_hangman_answer)

	start_hangman_game(6,real_hangman_answer,real_answer_guessed_so_far)