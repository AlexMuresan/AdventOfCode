import numpy as np

def getRatings(rucksack):
    eg_line = rucksack
    half = int(len(eg_line)/2)

    half_1 = list(eg_line[:half])
    half_2 = list(eg_line[half:])

    common_item = np.intersect1d(half_1, half_2)[0]
    priority = (ord(common_item) - 96 if common_item.islower() else ord(common_item.lower()) - 70)

    return priority


if __name__ == "__main__":
    with open('rucksack-test.txt', "r") as f:
        lines = f.readlines()

    lines_clean = list(map(lambda x: x.strip('\n'), lines))
    priorities = list(map(getRatings, lines_clean))

    print(sum(priorities))


    