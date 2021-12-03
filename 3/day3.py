import fileinput
import pandas as pd


def ingest(info):
    data = []
    for line in fileinput.input(files = info):
        data.append(list(line.rstrip()))
    infodb = pd.DataFrame(data)
    return infodb


def onoff(x):
    if x == '1':
        x = '0'
    elif x == '0':
        x = '1'
    else:
        pass
    return x


def findcommon(datab):
    freq = datab.mode()
    gamma = freq.agg(''.join, axis=1)
    epsilon = freq.applymap(lambda x: onoff(x)).agg(''.join, axis=1)
    gamma_str = gamma[0]
    epsilon_str = epsilon[0]
    return gamma_str, epsilon_str


def binary2dec(binary):
    return int(binary,2)


if __name__ == "__main__":
    gamma, epsilon = findcommon(ingest("input.txt"))
    g_int = binary2dec(gamma)
    e_int = binary2dec(epsilon)
    power = g_int * e_int
    print(power)