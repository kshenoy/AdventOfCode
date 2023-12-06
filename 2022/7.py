import pprint
import re

pp = pprint.PrettyPrinter(indent=2, width=120)


class File:
    def __init__(self, name, size=0):
        self.Name = name
        self.Size = size
        self.Children = {}  # name : str => File

    def add_child(self, child):
        if child.Name not in self.Children:
            self.Children[child.Name] = child

    def get_child(self, name):
        return self.Children[name]

    def get_children(self):
        return self.Children.values()


class Shell:
    def __init__(self):
        self.Filetree = File("/")
        self.Path = []

    def cd(self, loc: str):
        match loc:
            case "/":
                self.Path = []
            case "..":
                self.Path.pop()
            case _:
                self.Path.append(loc)

    def add_file(self, file: File):
        parent = self.get_file_at(self.Path)
        parent.add_child(file)
        if not self.is_dir(file):
            self.update_sizes(file.Size)

    def get_file_at(self, path):
        curr_file = self.Filetree
        for file in path:
            curr_file = curr_file.get_child(file)
        return curr_file

    def update_sizes(self, size: int):
        file = self.Filetree
        file.Size += size
        for ancestor in self.Path:
            file = file.get_child(ancestor)
            file.Size += size

    def is_dir(self, f: File) -> bool:
        return len(f.get_children()) != 0

    def print(self, file: File, prefix: str = ""):
        if self.is_dir(file):
            print(prefix, file.Name + "/", " =", file.Size, sep="")
        else:
            print(prefix, file.Name, " =", file.Size, sep="")

        prefix = "  " + prefix
        for child in file.get_children():
            self.print(child, prefix)

    def tree(self):
        self.print(self.Filetree, "- ")


shell = Shell()


def parse_cmd(input_str: str):
    global shell
    tokens = input_str.split(" ")
    if tokens[1] == "cd":
        shell.cd(tokens[2])


def parse_ls_out(input_str: str):
    global shell
    token, name = input_str.split(" ")
    size = 0 if token == "dir" else int(token)
    shell.add_file(File(name, size))


with open("7_in.txt") as file:
    for line in file:
        line = line.rstrip()
        if line[0] == "$":
            parse_cmd(line)
        else:
            parse_ls_out(line)

# shell.tree()


def findSub100KDirs(file: File) -> int:
    global shell
    size_sum = file.Size if file.Size <= 100000 else 0

    for child in file.get_children():
        if shell.is_dir(child):
            size_sum += findSub100KDirs(child)
    return size_sum


totalSub100KSizes = findSub100KDirs(shell.Filetree)

print("The total size of all dirs sub-100K is", totalSub100KSizes)


space_required = 30000000 - (70000000 - shell.Filetree.Size)


def get_smallest_size(file: File, smallest_size: int) -> int:
    global shell, space_required

    if not shell.is_dir(file) or file.Size < space_required:
        return smallest_size

    smallest_size = min(file.Size, smallest_size)
    # print("Smallest file:", file.Name, "with Size", file.Size)
    for child in file.get_children():
        smallest_size = get_smallest_size(child, smallest_size)
    return smallest_size


smallest_size = get_smallest_size(shell.Filetree, shell.Filetree.Size)

print(
    "Space required is",
    space_required,
    "so the smallest size to delete is",
    smallest_size,
)
