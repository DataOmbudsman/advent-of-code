from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = set()

    @abstractmethod
    def size(self):
        raise NotImplementedError


class File(Node):
    def __init__(self, name, parent, size):
        super().__init__(name, parent)
        self._size = size

    def size(self):
        return self._size


class Folder(Node):
    def __init__(self, name, parent):
        super().__init__(name, parent)

    def size(self):
        return sum(child.size() for child in self.children)

    def add_child(self, node):
        self.children.add(node)


def iterate_folders(node):
    if node.children:
        yield node
    for child in node.children:
        yield from iterate_folders(child)


def what_to_delete(root):
    space_total = 70_000_000
    space_needed = 30_000_000
    space_used = root.size()
    space_unused = space_total - space_used
    space_to_free = space_needed - space_unused

    folder_sizes = [folder.size() for folder in iterate_folders(root)]
    for size in sorted(folder_sizes):
        if size > space_to_free:
            return size


def main():
    with open('input') as lines:
        root = Folder(name='/', parent=None)

        for line in lines:
            line = line.rstrip()
            tokens = line.split()

            # changing folders
            if tokens[0] == '$' and tokens[1] == 'cd':
                if tokens[2] == '/':
                    # assumption "cd /" is the first command
                    current_folder = root
                elif tokens[2] == '..':
                    current_folder = current_folder.parent
                else:
                    node = Folder(name=tokens[2], parent=current_folder)
                    current_folder.add_child(node)
                    current_folder = node

            # reading a file
            elif tokens[0].isnumeric():
                file = File(
                    name=tokens[1], parent=current_folder, size=int(tokens[0])
                )
                current_folder.add_child(file)

    print(what_to_delete(root))


if __name__ == "__main__":
    main()
