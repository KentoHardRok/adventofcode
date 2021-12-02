import fileinput

def ingest(research):
    depth = []
    for line in fileinput.input(files = research):
        depth.append(line.rstrip())
    return depth

def shmove(data):
    forward = 0
    depth = 0
    for m in range(len(data)):
        now = data[m].split()
        if now[0] == "forward":
            forward += int(now[1])
        if now[0] == "up":
            depth -= int(now[1])
        if now[0] == "down":
            depth += int(now[1])
    return(forward * depth)
    
def amy(data):
    forward = 0
    aim = 0
    depth = 0
    for m in range(len(data)):
        now = data[m].split()
        move = now[0]
        num = int(now[1])
        if move == "forward":
            forward += num
            if aim == 0:
                pass
            else:
                depth += aim * num 
        elif move == "up":
            aim -= num 
        elif move == "down":
            aim += num 
        print(aim, depth, forward)
    return(forward * depth)
    

if __name__ == "__main__":
    print(amy(ingest("2/input.txt")))