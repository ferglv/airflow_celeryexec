import os


def print_tree(directory, file_output=False, padding="|-- ", print_files=True):
    """
        Print tree structure of the directory.
    .
        :param directory: the directory path
        :param file_output: whether to print files or just directories
        :param padding: padding for tree branches
        :param print_files: whether to print file names
    """
    print(directory + "/")
    if os.path.isdir(directory):
        _print_tree(directory, padding, file_output, print_files)


def _print_tree(directory, padding, file_output, print_files, depth=0):
    if not os.path.isdir(directory):
        return

    for item in sorted(os.listdir(directory)):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            print(padding * depth + item + "/")
            _print_tree(path, padding, file_output, print_files, depth + 1)
        elif print_files:
            print(padding * depth + item)


if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    print_files = (
        input("Do you want to print files as well? (yes/no): ").strip().lower() == "yes"
    )
    print_tree(dir_path, print_files=print_files)
