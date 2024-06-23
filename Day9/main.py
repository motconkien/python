from art import logo

print(logo)
bid_record = {}

def find_highest_bidder(bid_record):
    highest_bid = 0
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${bid_amount}")

while True:
    name = input("What is your name? ").strip()
    amount = int(input("What is your bid? $"))
    result= input("Are there any other bidders? Type 'yes' to continue or 'no'.\n").lower()
    bid_record[name] = amount
    if result == "no":
        find_highest_bidder(bid_record)
        break
    