import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    file_path = os.path.join(directory, filename)

    with open(file_path, "a+") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in content_input():
            file.write(line + "\n")


def content_input() -> None:
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        yield line + "\n"


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory = os.path.join(*sys.argv[dir_index:file_index - 1])
        os.makedirs(directory, exist_ok=True)
        filename = sys.argv[file_index]
        create_file(directory, filename)
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        os.makedirs(directory, exist_ok=True)
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]
        create_file(".", filename)
    else:
        print("Invalid arguments. Use either -d or -f flag.")
        return


if __name__ == "__main__":
    main()
