import numpy as np

def ingest(data_call, data_card):
    calls = np.loadtxt(data_call, delimiter=',', dtype=int)
    with open(data_card) as f:
        card_count = sum(line.isspace() for line in f)
    all_cards = np.loadtxt(data_card, dtype=int)
    cards = np.array_split(all_cards,card_count,axis=0)
    return calls, cards


if __name__ == "__main__":
    calls, cards = ingest("input_calls_short.txt", "input_short.txt")
    print(cards[0])