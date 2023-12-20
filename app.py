import random
import os
from words_of_hangman import words
from words_of_hangman import hangman_stages

def day_1():
    city_name = input("""
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
""")

    pet_name = input("""
What's your pet's name?
""")

    print(f"Your band name could be {city_name} {pet_name}")
    
    
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

def day_2():
    total_bill = float(input("""Welcome to the tip calculator!
What was the total bill? """))

    number_of_people = float(input("""
How much tip would you like to give? 10, 12, or 15? """))

    percentage_of_tip = float(input("""
How many people to split the bill? """))
    
    payment_of_each_person = ( (total_bill) + ( total_bill * ( percentage_of_tip/100 ) ) ) /number_of_people 
    payment_of_each_person = float(payment_of_each_person)
    print(f"Each person should pay: ${str(payment_of_each_person)} ")
    
    
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

def day_4():
    user_choice = int(input("""What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. 
"""))
    
    computer_choice = random.randint(0, 2)
    
    hand_shapes = [
        """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

        """,
        """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

        """,
        """
    ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

        """
        
    ]
   
    if user_choice < 0 or computer_choice > 2:
        return
    
    print(hand_shapes[user_choice])
    print("Computer chose:\n")
    print(hand_shapes[computer_choice])
    
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif user_choice == 0 and computer_choice == 1:
        print("You Lose!")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win!")
    elif user_choice == 1 and computer_choice == 2:
        print("You Lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win!")

    
    
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

def day_5():
    
    password_list = []
    
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    symbols = ["{", "}", "[", "]", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=", ":", "'", ";", "/", "?", ">", "<", "|", "~", "`", ",", "."]
    
    print("Welcome to the PyPassword Generator!")
    required_letters = int(input("""
How many letters would you like in your password? 
"""))
    required_symbols = int(input("""
How many symbols would you like? 
"""))
    required_numbers = int(input("""
How many numbers would you like? 
"""))
    
    for i in range(required_letters):
        password_list.append(random.choice(letters))
    
    for i in range(required_symbols):
        password_list.append(random.choice(symbols))
    
    
    for i in range(required_numbers):
        password_list.append(random.randint(0, 9))
    
    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    
    password = ""
    for letter in password_list:
        password += str(letter) 
        
    print(f"Your password is: {password}")
    
    
    
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

def day_7_hangman():
    
    hangman_word = random.choice(words)
    
    def make_word_like_list(word):
        
        word_list = []
        
        for letter in word:
            word_list.append(letter)
            
        return word_list
    
    hangman_word = make_word_like_list(hangman_word)
    stage_count = 0
    guessed_word_list = [[] for i in range(len(hangman_word))]

    checked_correct_letters = len(hangman_word)
    
    for i in range(len(hangman_word)):
        guessed_word_list[i] = "_"
    
    def show_stage_and_guess_a_letter(stage_count, passed, wrong_guessed_letter, win_status):
        os.system('cls')
            
        print("""
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                    |___/    
    """)
        
        guessed_word = ""
        if not passed:
            print(f"You guessed {wrong_guessed_letter}, that's not in the word. You lose a life.")
            

        for i in range(len(hangman_word)):
            guessed_word = guessed_word + guessed_word_list[i] + " "
            
        print(guessed_word)
        
        if win_status:
            print("You Win.")

        print(hangman_stages[stage_count])


    passed = True
    wrong_guessed_letter = ""
    
    while stage_count < 5:
        
        show_stage_and_guess_a_letter(stage_count= stage_count, passed = passed, wrong_guessed_letter = wrong_guessed_letter, win_status = False)
        
        guessed_letter = input("Guess a letter: ")
        guessed_letter_status = False
        
        for i in range(len(hangman_word)):
            if guessed_letter in hangman_word:
                if guessed_letter in guessed_word_list:
                    continue
                
                for i in range(len(hangman_word)):
                    if guessed_letter == hangman_word[i]:
                        guessed_word_list[i] = guessed_letter
                        checked_correct_letters -= 1
                        
                guessed_letter_status = True
                # guessed_word_list[i] = hangman_word[i]
        
        if guessed_letter_status:
            if checked_correct_letters == 0:
                show_stage_and_guess_a_letter(stage_count= stage_count, passed = True, wrong_guessed_letter = "", win_status = True)
                return
        else:
            show_stage_and_guess_a_letter(stage_count= stage_count, passed = False, wrong_guessed_letter = guessed_letter, win_status = False)
            stage_count += 1
        
    
day_7_hangman()
# Complete Day 5 for loops and generating strong passwords in 100 days of code Python