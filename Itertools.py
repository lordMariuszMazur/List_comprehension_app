# Itertools practice
import itertools

ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
ranks = [str(rank) for rank in ranks]

print(ranks)  # prints all posible cards

suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
deck = [card for card in itertools.product(ranks, suits)]

for (index, card) in enumerate(deck):  # prints all posible cards with suits
    print(1 + index, card)
