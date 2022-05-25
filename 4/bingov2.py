import numpy as np

def ingest(data_call, data_card):
    all_card = np.genfromtxt(data_card, dtype=int)
    indy_cards = np.array_split(all_card,3)
    open(data_call, "r")
    shot_call = np.genfromtxt(data_call, delimiter=',', dtype=int)
    return shot_call, indy_cards


if __name__ == "__main__":
    calls, cards = ingest("/home/tomw/adventofcode/4/input_calls_short.txt", "/home/tomw/adventofcode/4/input_short.txt")
    print(cards[0])
    print(calls)

