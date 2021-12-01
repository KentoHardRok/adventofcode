import fileinput

def ingest(research):
    depth = []
    for line in fileinput.input(files = research):
        depth.append(line.rstrip())
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
            print(num, "(increased)", increase)
        elif num < last:
            decrease += 1
            print(num, "(decreased)", decrease)
        last = num
    print("increased: ", increase)
    print("decreased: ", decrease)


if __name__ == "__main__":
    upordown(ingest("input_short.txt"))