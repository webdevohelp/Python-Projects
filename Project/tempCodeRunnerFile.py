
# Cards
#Suit, Rank of cards, Value of Cards

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    def __str__(self):
        return self.rank + " of " + self.suit + " and the value is " + str(self.value)

two_hearts = Card("Hearts","Jack")
three_of_clubs = Card("Clubs","Three")
print(two_hearts.value > three_of_clubs.value)