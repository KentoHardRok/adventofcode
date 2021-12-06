import fileinput

def ingest(research):
    depth = []
    for line in fileinput.input(files = research):
        depth.append(line.rstrip())
    return depth


if __name__ == "__main__":
    ingest()