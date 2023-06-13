from sys import argv
from process_commands import process_file

def main():
    """
    Executes the main function that processes a file located in the path given as an argument.

    Parameters:
        None.

    Return:
        None.

    Raises:
        Exception: If the path to the file is not provided as the only argument.
    """
    if len(argv) != 2:
        raise Exception('Path not found')

    file_path = argv[1]
    process_file(file_path)

if __name__ == '__main__':
    main()
    