
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
        password = input("Enter your password: ")

        self.clear_screen()

        # Checks to see if username exists
        if username not in self.userdc:
            print("Username not found")
            return None

        # Checks if username is located in the user dictionary AND check if the password matches
        elif (username in self.userdc) and (self.userdc[username].password == password):
            print("USER INFORMATION\n")
            return self.userdc[username] #return user object
        
        # If password doesnt match, print error statement
        else:
            print("Password does not match ")
            self.clear_screen()
            return None
            
         

    # Creates an instance of the user class, saving each user in the dictionary
    def signup(self):

        username = input("Enter your username: ") 
       
        # If username already exists, inform user
        if username in self.userdc:
            print("Username already exists\nPlease log in")
            self.clear_screen()
            return None
        
        # Create new user
        password = input("Enter your password: ")
        self.clear_screen()      
          
        new_user = User(username, password)
        self.userdc[username] = new_user
        new_user.personal_information()
        new_user.choose_acc()
        
        print("Success!")
        self.clear_screen()
        return new_user



    #The starup to the program: Allows the user to choose whether they want to signin, signup, or exit
    def start(self):

        print("WELCOME TO THE BANK ACCOUNT SYSTEM\n-----------------------------------")

        while True: 
        
            options = ["Sign up", "Log in", "Exit"]
            for i, option in enumerate(options, 1):
                print(f'{i}) {option}')

            try:
                action = int(input("-----------------------------------\nWhat would you like to do: "))
                self.clear_screen()
                if action == 1:
                    self.signup()

                elif action == 2:
                    user = self.login()
                    print("YOUR RETRIEVED INFORMATION")
                    user.display_info()

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
        
        print("\nPlease accurately fill out all the required questions\n-----------------------------------")
        self.name = input(str("Full name: "))
        self.DoB = input(str("Date of Birth: "))
        self.SSN = input(str("Social Security Number: "))
        self.address = input(str("Residential Adress: "))
        self.phonenumber = input(str("Phone Number: "))
        self.email = input(str("Email: "))
        self.initial_deposit = input(str("Initial Deposit: "))
        self.clear_screen()
    

    #The user must select and determine their 
    # 1. Bank Account Type
    # 2. Bank Account Category
    def choose_acc(self):
        print("In this section you will choose the specificalities of your bank account\n-----------------------------------")
        
        # Iterates through the types of bank accounts, showcasing them to user
        account_types = ["Personal", "Business", "Investment"]
        for i, option in enumerate(account_types, 1):
            print(f'{i}) {option}')
        
        # Promps user to choose their bank account
        # Stores choice as an index of the account_types array
        # Assigns Bank account type instance variable the value of the choice index
        account_type_choice = int(input("Choose which account you would like to create: ")) - 1
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
        specific_acc_choice = int(input("Choose which type of account you would like: ")) - 1
        self.specific_account = options[specific_acc_choice]
        self.clear_screen()

    # Displays all user that is attatched to a username when said username is inputted
    def display_info(self):
        print("Account Details\n")
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.DoB}")
        print(f"SSN/Tax ID: {self.SSN}")
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





















# types_of_accounts = ("1) Personal" , "2) Business" ,"3) Investment & Retirement" )

# personal_acc = ["1) Checking Account" , "2) Savings Account" , ]
# business_acc = ["1) Business Checkings Account" , "2) Business Savings Account "]
# investment_retirement_acc = ["1) Individual Retirement Account" , "2) Health Savings Account"]

# user_choice = {
#     "Personal " :{"Type: ": ""}
#     "Business " :{"Type: ": ""}
#     "Investment and Retirement " :{"Type: ": ""}
# }

# print("Welcome! I can assist you in opening a bank account.")

# def user_help:() 
#     for accounts in types_of_accounts:
#         print(accounts)

#     user_choice ("What type of account are you looking for?")

# user_help()