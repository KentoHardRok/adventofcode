import numpy as np


def ingest(number):
    right = np.loadtxt(number, usecols=(range(11,15)), dtype=str)
    left = np.loadtxt(number, usecols=(range(0,10)), dtype=str)
    return left, right


def find_num(nums):
    length_check = np.vectorize(len)
    lnm = length_check(nums)
    if lnm == 2 or lnm == 3 or lnm == 4 or lnm == 7:
        return 1
    else:
        return 0
    

if __name__ == "__main__":
    left, right = ingest("input.txt")
    total = 0
    for x in np.nditer(right):
        total += find_num(x)
    print(total)

