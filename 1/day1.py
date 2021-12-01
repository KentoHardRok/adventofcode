import fileinput

def ingest(research):
    depth = []
    for line in fileinput.input(files = research):
        depth.append(int(line.rstrip()))
    return depth

def upordown(data):
    last = ""
    increase = 0
    decrease = 0
    for num in data:
        if last == "":
            print(num, "(N/A - no previous measurement)")
        elif num > last:
            increase += 1
            print(num, "(increased)")
        elif num < last:
            decrease += 1
            print(num, "(decreased)")
        last = num
    print("increased: ", increase)
    print("decreased: ", decrease)

def windows(data):
    last = ""
    increase = 0
    decrease = 0
    for num in range(len(data)):
        current = sum(data[num:num+3]) 
        if last == "":
            print(data[num], "(N/A - no previous measurement)")
        elif current > last:
            increase += 1
            print(data[num], "(increased)")
        elif current < last:
            decrease += 1
            print(data[num], "(decreased)")
        last = current
    print("increased: ", increase)

if __name__ == "__main__":
    windows(ingest("1/input.txt"))