def readInput(filename, clean=False):
    with open(filename, 'r') as f:
        lines = f.readlines()

    if clean:
        lines_clean = list(map(lambda x: x.strip('\n'), lines))
        return lines_clean
    else:
        return lines


def findConsecutive(message):
    for i in range(0, len(message) - 4):
        window = message[i:i+4]
        if len(set(window)) == 4:
            print(window)
            return i+4
        else:
            continue


if __name__ == "__main__":
    # inputs = readInput('train.txt', clean=True)
    inputs = readInput('test.txt', clean=False)
    
    for message in inputs:
        print(findConsecutive(message))