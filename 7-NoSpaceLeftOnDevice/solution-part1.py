import numpy as np


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.folders = []
        self.files = []
    def __str__(self) -> str:
        return f"Node: {self.name}"
    def __repr__(self) -> str:
        return f"{self.name}"


def searchTree(node, target, answer=None):
    if node.name == target:
        answer=node

    for folder in node.folders:
        answer=searchTree(folder, target, answer=answer)

    return answer
        


def readLines(input_path, cleanup=False):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    if cleanup:
        clean_lines = list(map(lambda x: x.strip('\n'), lines))
        return clean_lines
    else:
        return lines


def processInput(command_list) -> Node:
    root_node = None

    for line in command_list:
        if line.startswith('$'):
            if "ls" in line:
                ls_output = []
            if "cd" in line:
                folder = line.split(' ')[-1]
                if folder != "..":
                    if current_node:
                        new_node = Node(folder, parent=current_node)
                        current_node = new_node
                    else:
                        current_node = Node(folder)
        else:
            first, second = line.split(' ')
            if first == "dir":
                current_node.folders
            


if __name__ == "__main__":
    command_list = readLines("train.txt", cleanup=True)
    # root_node = processInput(command_list)

    root_node = Node("/")
    dir_a = Node("a", parent=root_node)
    dir_d = Node("d", parent=root_node)
    dir_e = Node("e", parent=dir_a)
    dir_f = Node("f", parent=dir_e)
    
    root_node.folders = [dir_a, dir_d]
    dir_a.folders = [dir_e]
    dir_e.folders = [dir_f]

    target = '/'
    found_node = searchTree(node=root_node, target=target)
    print(found_node)


