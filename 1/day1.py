import fileinput

def ingest(research):
    depth = []
    for line in fileinput.input(files = research):
        depth.append(line.rstrip())
    return depth

def upordown(data):
    last = 0
    increase = 0
    decrease = 0
    for num in range(len(data)):
        if last == 0:
            print(data[num], "(N/A - no previous measurement)")
        elif data[num] > last:
            increase += 1
            print(data[num], "(increased)")
        elif data[num] < last:
            decrease += 1
            print(data[num], "(decreased)")
        last = data[num]
    print("increased:", increase)
    print("decreased: ", decrease)


if __name__ == "__main__":
    upordown(ingest("input_short.txt"))