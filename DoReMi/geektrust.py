import sys

from process_commands import process_file


def main():
    if len(sys.argv) != 2:
        raise Exception("File path not entered")

    file_path = sys.argv[1]
    process_file(file_path)


if __name__ == "__main__":
    main()
