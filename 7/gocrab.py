import fileinput
import numpy as np


def ingest(data):
    crabsub = []
    for line in fileinput.input(files = data):
        disance = line.rstrip()
    crabsub = disance.split(',')
    npcrab = np.asarray(crabsub, dtype=np.int)
    return npcrab


def used_gas(move):
    total = 0
    for x in range(0, move + 1):
        total += x
    return total  


def gas(data):
    g_total = 0
    g_used = 0
    median = int(np.mean(data))
    print(median)
    for x in np.nditer(data):
        g_used = abs(x - median)
        g_total += used_gas(g_used.astype(int))
    return g_total


if __name__ == "__main__":
    data = ingest("input.txt")
    print(gas(data))
