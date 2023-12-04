import random
from Art import logo

cards_user = []
cards_computer = []
card_list_num = {
    0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: "J", 10: "Q", 11: "K", 12: "A"
}

for value in [9, 10, 11, 12]:
    card_list_num[value] = 10

def card_computer_generat():
    card = random.choice(list(card_list_num.keys()))
    cards_computer.append(card)
    return card_list_num[card]

def card_user_generat():
    card = random.choice(list(card_list_num.keys()))
    cards_user.append(card)
    return card_list_num[card]

def check_sum(sum_cards_user, sum_cards_computer):
    if sum_cards_computer >= 17:
        sum_cards_computer += card_computer_generat()
    elif sum_cards_computer < 21:
        sum_cards_computer += card_computer_generat()

print(logo)
beggining = input("Do you want to play a game of Blackjack? Type yes or no:\n")
if beggining.lower() == 'yes':
    sum_card_user = card_user_generat() + card_user_generat()
    print(f"Your cards: {cards_user}, current score: {sum_card_user}")

    sum_card_computer = card_computer_generat() + card_computer_generat()
    print(f"Computer's first card: {cards_computer[0]}")

    while sum_card_user < 21:
        next_card = input("Type 'yes' to get another card, type 'no' to pass:\n")
        if next_card.lower() == 'yes':
            sum_card_user += card_user_generat()
            print(f"Your cards: {cards_user}, current score: {sum_card_user}")
            check_sum(sum_card_user, sum_card_computer)
            print(f"Computer's s: {cards_computer},current score:{sum_card_computer}")
        else:
            break

    if sum_card_user > 21:
        print("You went over. You lose!")
    elif sum_card_computer > 21:
        print("Computer went over. You win!")
    elif sum_card_user > sum_card_computer:
        print("You win!")
    elif sum_card_user < sum_card_computer:
        print("You lose!")
    else:
        print("It's a draw!")
else:
    print("Goodbye!")