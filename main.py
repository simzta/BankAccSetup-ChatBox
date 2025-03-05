
# Bank account class which starts the program: It hold the login and signup options
# The data recieved from the User class for every user saves: the username is added into a dictionary
# This data can later be called up when using the "Sign in" option and providing a username & password
class BankAccounts:
    # The dictionary holding all users should be here
    # The function should contain the indicated users' password and username.
    def __init__(self, username, password):
        self.userdc = {}
        self.username = None
        self.password = None

    # If user already has created an acc this is a way to access the data 
    def log_in(username, password):

    # A user can be sent to create an account if they do not have an existing account
    def sign_up(username):

















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