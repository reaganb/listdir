import zipfile
import hashlib
import argparse
import os.path as op
import glob


class ListDir:
    """
    The ListDir class consist of functions for recursively
    listing of files in a certain path and writing it to another
    file (csv).
    """
    def __init__(self, **config_args):
        """The init function consists of the path and destination file(csv)
        properties

        Keyword arguments:
        config_args['path'] -- the directory path for recursive listing
        config_args['dest'] -- the output file
        """

        self.path = op.abspath(config_args['path'])
        self.dest = op.abspath(config_args['dest'])
        # Check if the path exist
        if not op.exists(self.path):
            print('Error: Path does not exist!')
            exit(0)
        # Check if only a path, not a file is given as the argument
        elif not op.isdir(self.path):
            print('Error: Path are only allowed as the argument')
            exit(0)

        self.csv_file = config_args['dest']
        self.files = glob.glob(f'{self.path}/**', recursive=True)

    def print_files(self):
        """List files/directories recursively based on the given path"""

        for file in self.files:
            print(file)

    @staticmethod
    def hash_file(file, algorithm):
        """The method for computing the checksum hashing of the file depending on the algorithm provided

        Keyword arguments:
        file -- the directory path for recursive listing
        algorithm -- the algorithm to use (default 'md5')
        """

        block_size = 65536
        if algorithm == 'sha1':
            hasher = hashlib.sha1()
        else:
            hasher = hashlib.md5()

        with open(file, 'rb') as hash_file:
            buf = hash_file.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = hash_file.read(block_size)

        return hasher.hexdigest()

    def output_zip(self):
        """Create the csv format file from the recursive listing"""

        with zipfile.ZipFile(f'{self.csv_file}.zip', 'w') as zip_file:
            with open(self.csv_file, 'w+') as file:
                file.write('parent path,filename,filesize,md5,sha1')

                for csv in self.files:
                    if op.isfile(csv):
                        directory = f"\"{op.dirname(csv)}\""
                        file_name = f"\"{op.basename(csv)}\""
                        md5 = self.hash_file(csv, 'md5')
                        sha1 = self.hash_file(csv, 'sha1')
                        size = op.getsize(csv)
                        file.write(f"\n{directory}, {file_name}, {size}, {md5}, {sha1}")

            zip_file.write(self.csv_file)


if __name__ == "__main__":
    # The starting point of the script and
    # the code for the command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('path', help="the source file")
    parser.add_argument('dest', help="the destination csv filename")

    args = parser.parse_args()

    # Initialize the Listdir object together with its arguments
    # path argument: The path of the directory
    # dest argument: The destination file (.csv)
    listdir = ListDir(path=args.path, dest=args.dest)

    # Running the function of the object
    listdir.print_files()
    listdir.output_zip()
