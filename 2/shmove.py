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
    
         

if __name__ == "__main__":
    print(shmove(ingest("2/input.txt")))