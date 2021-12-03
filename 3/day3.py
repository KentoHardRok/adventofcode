import fileinput
import pandas as pd
import numpy as np

def ingest(info):
    data = []
    for line in fileinput.input(files = info):
        data.append(list(line.rstrip()))
    infodb = pd.DataFrame((data), 
    columns=list('abcdefghijkl'))
    return infodb

def gen(db, commondt):
    col = 'abcdefghijkl'
    print(commondt)
    count = 0
    newdb = db
    for i in commondt:
        chk = col[count]
        if i == 'a':
            newdb = db.loc[db["{}".format(chk)] == i]
        else:
            veri = newdb.loc[db["{}".format(chk)] == i]
            if veri.empty:
                return newdb
            else:
                newdb = newdb.loc[db["{}".format(chk)] == i]
        count += 1
    return newdb    

def diffpd(data):
    df = data.mode()



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
    raw = ingest("input.txt")
    gamma, epsilon = findcommon(raw)
    g_int = binary2dec(gamma)
    e_int = binary2dec(epsilon)
    print(gen(raw, gamma))
    print(gen(raw, epsilon))
    power = g_int * e_int
    print(power)