# TASK 3 - Use the https://deckofcardsapi.com/ to create a BLACKJACK game:
# You generate/shuffle a deck. You use that deck to play the game.

import requests
from thefuzz import fuzz

server_response_deck: requests.Response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

if server_response_deck.ok:
    json_data_deck: dict = server_response_deck.json()

player_score: int = 0
casino_score: int = 0


def draw_card():
    card: requests.Response = requests.get(f"https://deckofcardsapi.com/api/deck/"
                                            f"{json_data_deck['deck_id']}/draw/?count=1")
    if card.ok:
        json_data_card: dict = card.json()
        card_value = json_data_card["cards"][0]["value"]

        if card_value == "ACE":
            card_value = 1
        elif card_value == "KING" or card_value == "QUEEN" or card_value == "JACK":
            card_value = 10
        else:
            card_value = int(card_value)

        return card_value


intro = "Game starts with two drawn cards. Your goal is ot beat the casino. You win when your points are more than " \
        "the points of the casino, but less than 21. Have fun playing..."
print(intro)

card: int = draw_card()
player_score += card
card: int = draw_card()
player_score += card

card: int = draw_card()
casino_score += card
card: int = draw_card()
casino_score += card

print(player_score)

play: str = input("Do you want to keep playing?: a) Hit me b) Stop ")
while fuzz.ratio(play, "stop") <= 70:
    card: int = draw_card()
    player_score += card
    card: int = draw_card()
    casino_score += card
    print(player_score)
    play: str = input("Do you want to keep playing?: a) hit me b) stop ")

print(f" Casino score is {casino_score}.")

if casino_score < player_score <= 21:
    print("You win! ")

else:
    print("You lose! The casino win! ")
