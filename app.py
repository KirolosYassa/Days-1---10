import random

def day_1():
    city_name = input("""
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
""")

    pet_name = input("""
What's your pet's name?
""")

    print(f"Your band name could be {city_name} {pet_name}")
    

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
    
day_5()

# Complete Day 5 for loops and generating strong passwords in 100 days of code Python