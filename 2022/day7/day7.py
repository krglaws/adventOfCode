import sys
from typing import IO


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{size} {name}"

    def get_size(self):
        return self.size


class Dir:
    def __init__(self, name: str, parent: "Dir"):
        self.name = name
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f"dir {name}"

    def get_size(self):
        sum_ = 0
        for child in self.children:
            sum_ += child.get_size()
        return sum_


class Shell:
    def __init__(self):
        rootdir = Dir("/", None)
        rootdir.parent = rootdir

        self.cwd = rootdir
        self.path = rootdir.name
        self.ls = False

    def __repr__(self):
        return f"Shell at {path}"

    def cd(self, name):
        if name == "/":
            while self.cwd != self.cwd.parent:
                self.cwd = self.cwd.parent
            self.path = "/"
        elif name == "..":
            self.cwd = self.cwd.parent
            if self.cwd.parent == self.cwd:
                self.path = "/"
            else:
                self.path = self.path[:-self.path[::-1].index("/")-1]
        else:
            try:
                self.cwd = next(filter(lambda child: child.name == name, self.cwd.children))
            except StopIteration:
                raise Exception(f"Failed to find directory {name}")
            self.path = f"{self.path}/{self.cwd.name}"

    def readline(self, line: str):
        if self.ls:
            if line[0] == "$":
                self.ls = False
                self.readline(line)
            elif line[0].isdigit():
                size, name = line.split()
                self.cwd.children.append(File(name, int(size)))
            elif line[:3] == "dir":
                self.cwd.children.append(Dir(line.split()[1], self.cwd))
            else:
                raise Exception(f"Invalid directory listing: '{line}'")
            return

        if line[0] != "$":
            raise Exception(f"Command missing '$': '{line}'")

        cmd = line.split()[1]
        if cmd == "cd":
            self.cd(line.split()[2])
        elif cmd == "ls":
            self.ls = True
        else:
            raise Exception(f"Unrecognized command: '{line}'")

    def start(self, file: IO[str]):
        while line := file.readline():
            self.readline(line[:-1])

    def _get_sum_of_dirs_of_size(self, size: int):
        sum_ = 0
        for child in self.cwd.children:
            if isinstance(child, Dir):
                dir_size = child.get_size()
                if dir_size <= size:
                    sum_ += dir_size
                self.cd(child.name)
                sum_ += self._get_sum_of_dirs_of_size(size)
        self.cd("..")
        return sum_

    def get_sum_of_dirs_of_size(self, size: int):
        self.cd("/")
        return self._get_sum_of_dirs_of_size(size)

    def _find_dir_close_to_size(self, target: int, current: int):
        for child in self.cwd.children:
            if isinstance(child, Dir):
                dir_size = child.get_size()
                if dir_size >= target and dir_size < current:
                    current = dir_size
                self.cd(child.name)
                dir_size = self._find_dir_close_to_size(target, current)
                if dir_size >= target and dir_size < current:
                    current = dir_size 
        self.cd("..")
        return current

    def make_space_for_update(self, total_space: int, update_size: int):
        self.cd("/")
        used_space = self.cwd.get_size()
        available_space = total_space - used_space
        minimum_delete = update_size - available_space
        print(
        f"""
        {total_space=}
        {used_space=}
        {available_space=}
        therefore, the minimum space needed to 
        make room for the update is:
        {update_size} - {available_space} = {minimum_delete}
        """
        )

        return self._find_dir_close_to_size(minimum_delete, self.cwd.get_size())


if __name__ == "__main__":
    shell = Shell()

    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        shell.start(sys.stdin)
    else:
        with open("./input.txt") as infile:
            shell.start(infile)

    print(shell.get_sum_of_dirs_of_size(100000))
    print(shell.make_space_for_update(70000000, 30000000))

