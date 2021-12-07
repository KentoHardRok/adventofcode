import fileinput

def ingest(research):
    pescadito = []
    for line in fileinput.input(files = research):
        pescado = line.rstrip()
    pescadito = pescado.split(',')
    return pescadito


def decrease(num):
    if num == 0:
        num = 6
        return num
    else:
        num -= 1
        return num


def countfish(fishlist, slot):
    if slot > 0:
        fishlist[slot + 1] -= 1
        fishlist[slot] += 1
    else:  
        fishlist[slot + 1] -= 1
        fishlist[7] += 1
        fishlist[5] += 1
    return fishlist


def growth(fishes, days):
    allfish = [0,0,0,0,0,0,0,0]
    for x in fishes:
        allfish[x] += 1
    print(allfish)
    for i in range(0, days):
        print(i)
        for eachfish in range(sum(allfish)):
            current = fishes[eachfish]
            fishes[eachfish] = decrease(current)
            allfish = countfish(allfish, fishes[eachfish])
            print(allfish)
            print(eachfish) 
    print(allfish)   


if __name__ == "__main__":
 #   fish = ingest("input_short.txt")
 #   fish = list(map(int, fish))
    fish = [6, 3, 4]
    growth(fish, 20)