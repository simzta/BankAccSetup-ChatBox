
types_of_accounts = ["1) Personal" , "2) Business" ,"3) Investment & Retirement" ]
personal_acc = [1 "1) Checking Account" , "2) Savings Account" , ]
business_acc = ["1) Business Checkings Account" , "2) Business Savings Account "]
investment_retirement_acc = ["1) Individual Retirement Account" , "2) Health Savings Account"]

user_choice = {
    "Personal " :{"Type: ": ""}
    "Business " :{"Type: ": ""}
    "Investment and Retirement " :{"Type: ": ""}
}

print("Welcome! I can assist you in opening a bank account.")

def user_help:() 
    for accounts in types_of_accounts:
        print(accounts)

    user_choice ("What type of account are you looking for?")

user_help()