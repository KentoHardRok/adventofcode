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
        return True, num
    else:
        num -= 1
        return False, num


def countfish(fishlist, slot):
    if fishlist[slot] > 0:
        fishlist[slot + 1] -= 1
        fishlist[slot] += 1
    else:  
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
        current = range(sum(allfish))
        for eachfish in current:
            babyfish, fishes[eachfish] = decrease(fishes[eachfish])
            allfish = countfish(allfish, fishes[eachfish])
            print(allfish)
            if babyfish:
                allfish[7] += 1    
            print(current) 
    print(allfish)   


if __name__ == "__main__":
 #   fish = ingest("input_short.txt")
 #   fish = list(map(int, fish))
    fish = [6, 3]
    growth(fish, 20)