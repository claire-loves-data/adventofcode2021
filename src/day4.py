import numpy as np


def read_input(filename):
    called = []
    cards = []
    with open(filename) as fp:
        called = [int(a) for a in fp.readline().rstrip().split(",")]
        cards = []
        currentcard = []
        count = 0
        for line in fp.readlines():
            if line != "\n":
                currentcard.append([int(a) for a in line.rstrip().split()])
                count += 1
            if count == 5:
                cards.append(np.array(currentcard))
                currentcard = []
                count = 0
    cards = np.array(cards)
    return called, cards


def check_win(cards):
    for i, card in enumerate(cards):
        if check_one_card(card):
            return i
    return None


def check_one_card(card):
    if -5 in np.sum(card, axis=0):
        return True
    elif -5 in np.sum(card, axis=1):
        return True
    else:
        return False


def run_bingo(called, cards):
    for n in called:
        cards = call_number(n, cards)
        val = check_win(cards)
        if val is not None:
            # -1 to 0
            card = cards[val].clip(min=0)
            return np.sum(card) * n


def call_number(num, cards):
    cards[np.where(cards == num)] = -1
    return cards


def discard_winners(cards):
    to_delete = []
    for i, card in enumerate(cards):
        if check_one_card(card):
            to_delete.append(i)

    return np.delete(cards, to_delete, 0)


def call_and_discard(called, cards):
    if len(cards) == 1:
        for n in called:
            call_number(n, cards)
            if check_one_card(cards[0]):
                return n, cards[0]
    else:
        n = called.pop(0)
        cards = call_number(n, cards)
        cards = discard_winners(cards)
        return call_and_discard(called, cards)


def let_squid_win(called, cards):
    n, card = call_and_discard(called, cards)
    card = card.clip(min=0)
    return np.sum(card) * n


if __name__ == "__main__":
    called, cards = read_input("data/day4input.txt")
    print(run_bingo(called, cards))
    print(let_squid_win(called, cards))
