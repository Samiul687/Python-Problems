from collections import Counter


class PokerHand(object):
    result = ["Loss", "Tie", "Win"]
    cards = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, hand):
        self.values = sorted(
            [self.CARDS.index(i) for i in hand[::3]],
            reverse=True)
        self.counted = Counter(self.values)
        self.suits = set(hand[1::3])
        self.most = sorted(
            self.counted.most_common(),
            key=lambda x: (x[1], x[0]),
            reverse=True)
        self.rank = self.rank()

    def rank(self):
        flush = len(self.suits) == 1
        s = sorted(
            range(min(self.values), max(self.values) + 1),
            reverse=True)
        straight = self.values == s
        counts = [c for _, c in self.most]

        if flush and straight:
            return 9, self.values
        if 4 in counts:
            return 8, self.most
        if 3 in counts and 2 in counts:
            return 7, self.most
        if flush:
            return 6, self.values
        if straight:
            return 5, self.values
        if 3 in counts:
            return 4, self.most
        if counts[0] == 2 and counts[1] == 2:
            return 3, self.most
        if 2 in counts:
            return 2, self.most
        return 1, self.values

    def compare_with(self, other):
        if self.rank > other.rank:
            return 'Win'
        elif self.rank < other.rank:
            return 'Loss'
        return 'Tie'
