import numpy as np

file = 'test.txt'
with open(file, 'r') as f:
    lines = f.readlines()

lines = [x.strip('\n') for x in lines]
lines = np.array(lines)

box_size = 4
nr_towers = int((len(lines[0]) + 1) / box_size)

nr_levels = 0
for line in lines:
    if ('[' in line) or (']' in line):
        nr_levels += 1

stack = []
for level_idx in range(nr_levels):
    line = lines[level_idx]
    chunks = [line[i:i+box_size] for i in range(0, len(line), box_size)]
    chunks = list(map(lambda x: x.strip(' []'), chunks))
    stack.append(chunks)

stack = np.array(stack)
box_list = []
for row in stack.T:
    box_list.append([x for x in row if x != ''])


instructions = []
for line in lines[nr_levels+2:]:
    tmp_line = line.replace('move', '').replace('from', '').replace('to', '').split(' ')
    line_clean = [x for x in tmp_line if x != '']
    instructions.append(line_clean)

for line in lines[:nr_levels+1]:
    print(line)

box_list = []
for row in stack.T:
    box_list.append([x for x in row if x != ''])

for move in instructions:
    nr_boxes = int(move[0])
    source = int(move[1]) - 1
    dest = int(move[2]) - 1

    for box in range(nr_boxes):
        box_list[dest].insert(0, box_list[source][0])
        del box_list[source][0]

top_stack = []
for col in box_list:
    top_stack.append(col[0])

top_stack = ''.join(top_stack)

print(top_stack)


