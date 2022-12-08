import collections
import numpy as np

def getBadgePriorities(group):
    split_group = list(map(list, group))

    intersect_1 = np.intersect1d(split_group[0], split_group[1])
    badge = np.intersect1d(intersect_1, split_group[2])[0]

    priority = (ord(badge) - 96 if badge.islower() else ord(badge.lower()) - 70)

    return priority

if __name__ == "__main__":
    with open('rucksack-test.txt', "r") as f:
        lines = f.readlines()

    lines_clean = list(map(lambda x: x.strip('\n'), lines))

    group_size = 3
    groups = np.array_split(lines_clean, len(lines_clean) / group_size)
    
    priorities = list(map(getBadgePriorities, groups))
    print(sum(priorities))

    