import argparse
import os.path as op
import glob


class ListDir:
    """
    The ListDir class consist of functions for recursively
    listing of files in a certain path and writing it to another
    file (csv).
    """
    def __init__(self, path, dest):
        """The init function consists of the path and destination file(csv)
        properties"""

        self.path = op.abspath(path)
        # Check if the path exist
        if not op.exists(self.path):
            print('Error: Path does not exist!')
            exit(0)
        # Check if only a path, not a file is given as the argument
        elif not op.isdir(self.path):
            print('Error: Path are only allowed as the argument')
            exit(0)

        self.csv_file = dest
        self.files = glob.glob(f'{self.path}/**', recursive=True)

    def print_files(self):
        """List files/directories recursively based on the given path"""

        for file in self.files:
            print(file)

    def output_csv(self):
        """Create the csv file from the recursive listing"""

        with open(f'{self.csv_file}.csv', 'w+') as file:
            file.write('parent path,filename,filesize')
            for csv in self.files:
                if op.isfile(csv):
                    dir = f"\"{op.dirname(csv)}\""
                    fname = f"\"{op.basename(csv)}\""
                    size = op.getsize(csv)
                    file.write(f"\n{dir}, {fname}, {size}")


if __name__ == "__main__":
    # The starting point of the script and
    # the code for the command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help="the source file")
    parser.add_argument('-d', '--destination', dest='filename',
                        help="the destination csv filename")

    args = parser.parse_args()

    # Initialize the Listdir object together with its arguments
    # First argument: The path of the directory
    # Second argument: The destination file (.csv), default is None
    listdir = ListDir(args.path, args.filename)

    # Running the functions of the Class ListDir
    if args.filename is not None:
        listdir.output_csv()
    else:
        listdir.print_files()
