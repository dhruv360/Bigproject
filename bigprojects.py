# create a game called rock, paper, scissors
# import random
# def computer_choice():
#     choices =['rock','paper','scissor']
#     return random.choice(choices)
# def User_choice():
#     User_choice=input('Enter rock,paper,scissor: ').lower()
#     while User_choice not in ['rock','paper','scissor']:
#       print('Invalid pick. Please pick again')
#       User_choice=input('Enter rock,paper,scissor: ').lower()
#     return User_choice
# def rules(User_choice,omputer_choice) :
#    if User_choice == computer_choice:
#       return "It's a tie !"
#    elif (User_choice == 'rock' and computer_choice == 'scissor')or(User_choice == 'paper' and computer_choice == 'rock')or(User_choice== 'sissor' and computer_choice == 'paper'):
#          return "You win !"
#    else: return 'You lose !'
# def play():
#    print("Welcome players let's play [Rock | Paper | Scissor]:")   
#    user_choice = User_choice()
#    Computer_choice = computer_choice()
#    print(f'You choose:{user_choice}')
#    print(f'computer choose:{Computer_choice}')
#    result=rules(Computer_choice,user_choice)
#    print(result)
# if __name__=='__main__'   :
#    play()

# # Age generator ------
# from datetime import datetime   #[from] import specific part of [datetime]-> module 
#                                 #[datetime] class is used to handle and manipulate dates and times.((It's in string form))
#                                 #                            ^^^^^^     ^^^^^^^^^^ ^^^^^     ^^^^^^          ^^^^^^^^^^^
# def calculate_age(birth_date):
#     """Calculate age based on the birth date."""
#     today = datetime.today()
#     age = today.year - birth_date.year    #  access specific time foe year use->  [.year] same for [.day]&[.month]
#     if (today.month, today.day) < (birth_date.month, birth_date.day):
#         age -= 1
#     return age

# def main():     #[birth_date_str] use to change birth date into datetime based to interpreted it-
#                 #-because "21-04-2006" date are often in string form, when we type our birthdate it's string form in[input]function-
#                 #-so we use [birth_date_str] to change into datetime object for calculations
#     print("Welcome to the Age Generator App!")
#     birth_date_str = input("Enter your date of birth (DD-MM-YYYY): ")  

#     try:
#         birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
#         age = calculate_age(birth_date)
#         print(f"You are {age} years old.")
#     except ValueError:
#         print("Invalid date format. Please use YYYY-MM-DD.")
    
# if __name__ == "__main__":
#     main()

# # -----Age generator in simpler code------
# from datetime import datetime
# DOB = input("Enter your birth_date (DD-MM-YYYY): ")
# try:
#     DOB= datetime.strptime(DOB, "%d-%m-%Y")
#     today = datetime.today()
#     age = today.year - DOB.year 
#     print(f"You are {age} years old.")
# except ValueError:
#     print("Invalid date format. Use DD_MM_YYYY.")
