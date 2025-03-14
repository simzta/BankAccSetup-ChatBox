import time
'''
Bank account class: Provides the user with options toe either sign up or log in to a bank account.
For each created user, the bank acc class stores their information and provides the ability to
call this data up when requested.

FUNCTIONS:
login: Takes a Username & Password, checks if username is in dictionary, if it is and the pass is correct
        the user is provided with all username-associated information. If it is not, the user is prompted
        to create an account

signup: The user is sent to create a User account, which will store in the Bank Account user dictionary,
        and can then be called up.

start: The start to the program, when the program is run the user gets to choose between signing up,
        logging in, or exiting.
'''

class BankAccounts:
    # The dictionary holding all users should be here (Username: User object)
    def __init__(self):
        self.userdc = {}
       

    def clear_screen(self):
        print("\n" * 100)


    # If user already has created an acc this is a way to access the data 
    def login(self):
        
        username = input("Enter your username: ")
        self.clear_screen()

        # Checks to see if username exists
        if username not in self.userdc:
            print("Username not found\nBack to main menu...")
            time.sleep(5)
            self.clear_screen()
            return None

        
        # Checks if password matches the username
        # If it matches return user object
        # If it does not match, prompt for user to enter new password
        # Repeat until password matches
        while True: 

            password = input("Enter your password: ")
            self.clear_screen()

            print("Checking password...")
            time.sleep(3)
            

            if (self.userdc[username].password == password):
                print("\nCorrect password!")
                time.sleep(3)
                self.clear_screen()

                return self.userdc[username] #return user object
            
            # If password doesnt match, print error statement
            else:
                print("\nIncorrect password\n")
                time.sleep(1)
                print("Trying again...")
                time.sleep(3)
                self.clear_screen()
            
         

    # Creates an instance of the user class, saving each user in the dictionary
    def signup(self):

        username = input("Enter your username: ") 
        self.clear_screen()

        # If username already exists, inform user
        if username in self.userdc:
            
            print("Username already exists\nBack to main menu...")
            time.sleep(5)
            self.clear_screen()
            return None
        
        # Create new user
        password = input("Enter your password: ")
        self.clear_screen()      
        
        print("Loading...")
        time.sleep(3)
        self.clear_screen()

        new_user = User(username, password)
        self.userdc[username] = new_user
        new_user.personal_information()
        new_user.choose_acc()
        
        print("Success!")
        time.sleep(5)
        self.clear_screen()
        return new_user



    #The starup to the program: Allows the user to choose whether they want to signin, signup, or exit
    def start(self):

        print("WELCOME TO THE BANK ACCOUNT SYSTEM\n")

        while True: 
            
            print("MAIN MANU\n-----------------------------------")
            options = ["Sign up", "Log in", "Exit"]
            for i, option in enumerate(options, 1):
                print(f'{i}) {option}')

            try:
                print("-----------------------------------")
                action = int(input("What would you like to do: "))
                self.clear_screen()

                if action == 1:
                    self.signup()

                elif action == 2:
                    user = self.login()

                    if user == None:
                        continue
                    else:
                        print("YOUR RETRIEVED INFORMATION")
                        user.display_info()
                        time.sleep(5)
                        
                        cont = input("\nPress enter to continue ")
                        self.clear_screen()

                elif action == 3:
                    print("GOODBYE")
                    break

                else:
                    print("Invalid option")

            except ValueError:
                print("Please enter a valid option")






'''
A User class: It creates a user in the BankAccounts system, and the information entered can then be recalled
This class will allow the user to signup and create a personal username and password linked to their information.

Personal information: Full name, Date of Birth, SSN, Home Adress, Phone number, Email, Initial deposit
The user then chooses their bank account type.
Bank account selection: Personal, Business, Investment

Depending on the BA Selection, there will be options for the specificalities of the account
If Personal: Checkings, Savings
If Business: Business Checkings, Business Savings, Merchant
If Investment: Individual Retirement, Brokerage, Health Savings 

When the User logs in with the correct usernamea and password, the function to show all information will be called
'''
class User:
    def __init__(self, username, password):
        #Creates the instance variables for this class
        self.username = username
        self.password = password
        self.name = None
        self.DoB = None
        self.SSN = None
        self.address = None
        self.phonenumber = None
        self.email = None
        self.initial_deposit = None
        self.account_type = None
        self.specific_account = None

    # Clears the terminal of all visible input
    def clear_screen(self):
        print("\n" * 100)

    # Prompts user to input all necessary personal information.
    # Stores the information in the corresponding instance variable
    def personal_information(self):
        
        print("Please accurately fill out all the required questions\n-----------------------------------")
        time.sleep(3)
        self.name = input(str("Full name: "))
        self.DoB = input(str("Date of Birth: "))
        self.SSN = input(str("Social Security Number: "))
        self.address = input(str("Residential Adress: "))
        self.phonenumber = input(str("Phone Number: "))
        self.email = input(str("Email: "))
        self.initial_deposit = input(str("Initial Deposit: "))
        print("-----------------------------------")
        print("Analyzing...")
        time.sleep(3)
        self.clear_screen()
    

    #The user must select and determine their 
    # 1. Bank Account Type
    # 2. Bank Account Category
    def choose_acc(self):
        print("In this section you will choose the specificalities of your bank account\n-----------------------------------")
        time.sleep(3)
        
        # Iterates through the types of bank accounts, showcasing them to user
        account_types = ["Personal", "Business", "Investment"]
        for i, option in enumerate(account_types, 1):
            print(f'{i}) {option}')
        
        # Promps user to choose their bank account
        # Stores choice as an index of the account_types array
        # Assigns Bank account type instance variable the value of the choice index
        account_type_choice = int(input("-----------------------------------\nChoose which account you would like to create: ")) - 1
        self.account_type = account_types[account_type_choice]
        self.clear_screen()

        # Depending on which account type chosen, present specific account options
        # If Personal acc: Checkings or Savings
        # If Business acc: Business Checkings, Business Savings, Merchant
        # If Investment: Individual Retirement, Brokerage, Health Savings 
        # Assigns a var options a specific value depending on the value of acc_types
        if self.account_type == "Personal":
            options = ["Checkings", "Savings"]
        elif self.account_type == "Business":
            options = [ "Business Checkings", "Business Savings" , "Merchant"]
        else:
            options = ["Individual Retirement", "Brokerage", "Health Savings"]
        
        # Iterates through options, showcases users' choices
        for i, option in enumerate(options, 1):
            print(f'{i}) {option}')

        # Prompts user to choose the specialized acc
        specific_acc_choice = int(input("-----------------------------------\nChoose which type of account you would like: ")) - 1
        self.specific_account = options[specific_acc_choice]
        self.clear_screen()

        print("Creating account...")
        time.sleep(3)
        self.clear_screen()

    # Displays all user that is attatched to a username when said username is inputted
    def display_info(self):
        print("Account Details\n")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.DoB}")
        print(f"Social Security Number: {self.SSN}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phonenumber}")
        print(f"Email: {self.email}")
        print(f"Account Type: {self.account_type}")
        print(f"Specific Account: {self.specific_account}")
        print(f"Initial Deposit: ${self.initial_deposit}")

# ------------------------------------------------------------------------------------------------------------------------
#RUN THE BANK SYSTEM
bank_system = BankAccounts()
bank_system.start()
















