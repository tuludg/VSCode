from auction_art import logo
import os

print(logo)
bidders = {}
any_bidders = "yes"

# TODO-1.: Create a while loop that stores every bid in a dic and cleares the terminal after each bid
while any_bidders != "no":
    
    name = input("What is your name?: ")
    bid = int(input("Whats is your bid?: "))
    bidders[name] = bid
    
    any_bidders = input("Are there any other bidders? 'yes' or 'no'").lower()
    os.system('cls')
    
name = ""
bid = 0

# TODO-2. loop through the dic to identify the winner
for key, money in bidders.items():
    
    if money > bid:
        name = key
        bid = money

print(f"The winner is {name} with a bid of {bid}")
    

