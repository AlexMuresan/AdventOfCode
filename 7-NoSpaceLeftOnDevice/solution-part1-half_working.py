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
        if line.startswith("$"):
            if "cd" in line:
                current_dir = line.split(' ')[2]
                if root_node:
                    current_node = root_node
                    if current_node.folders:
                        current_node = searchTree(root_node, target=current_dir)
                    else:
                        current_node = Node(current_dir)
                else:
                    root_node = Node(current_dir)
                    current_node = root_node

        else:
            first, second = line.split(' ')
            if first == "dir":
                current_node.folders.append(Node(second, parent=current_node))
            else:
                current_node.files.append({
                    "name": second,
                    "size": int(first)
                })

    return root_node


if __name__ == "__main__":
    command_list = readLines("test.txt", cleanup=True)
    root_node = processInput(command_list)

    print(root_node)
    print('\t', root_node.folders)
    for folder in root_node.folders:
        print('\t', folder)
        print('\t\t', folder.folders)
        if folder.folders:
            for next_level_folder in folder.folders:
                print('\t\t', next_level_folder)
                print('\t\t\t', next_level_folder.folders)
                print('\t\t\t', next_level_folder.files)
        print('\t\t', folder.files)
    print('\t', root_node.files)
