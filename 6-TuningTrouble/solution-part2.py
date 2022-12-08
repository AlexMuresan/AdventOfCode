def readInput(filename, clean=False):
    with open(filename, 'r') as f:
        lines = f.readlines()

    if clean:
        lines_clean = list(map(lambda x: x.strip('\n'), lines))
        return lines_clean
    else:
        return lines


def findConsecutive(message, msgLength=4):
    for i in range(0, len(message) - msgLength):
        window = message[i:i+msgLength]
        if len(set(window)) == msgLength:
            print(window)
            return i+msgLength
        else:
            continue


if __name__ == "__main__":
    # inputs = readInput('train.txt', clean=True)
    inputs = readInput('test.txt', clean=False)
    
    for message in inputs:
        print(findConsecutive(message, 14))