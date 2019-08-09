import zipfile
import hashlib
import configparser
import argparse
import glob
from datetime import datetime as dt
import os.path as op


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
        # Check if the path exist
        if not op.exists(self.path):
            print('Error: Path does not exist!')
            exit(0)
        # Check if only a path, not a file is given as the argument
        elif not op.isdir(self.path):
            print('Error: Path are only allowed as the argument')
            exit(0)

        self.csv_file = config_args['dest']
        self.files = self.generate_files(self.path)

    @staticmethod
    def generate_files(path):
        """A static generator type method for generating the file list"""
        for fc in glob.iglob(f'{path}/**',recursive=True):
            yield fc

    def print_files(self):
        """List files/directories recursively based on the given path"""

        # Print all files using the string join method and list comprehension technique
        print('\n'.join([file for file in self.files]))

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

        today = dt.today()
        zip_datetime = today.strftime('%Y-%m-%d-%H%M%S')
        with zipfile.ZipFile(f'{self.csv_file}_{zip_datetime}.zip', 'w') as zip_file:
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
                        print(f"\n{directory}, {file_name}, {size}, {md5}, {sha1}")

            zip_file.write(self.csv_file)


if __name__ == "__main__":
    # The starting point of the script.
    # The code for the command line arguments and
    # configuration file parsing
    parser = argparse.ArgumentParser()
    config = configparser.ConfigParser()
    config.read(op.join(op.dirname(op.abspath(__file__)), 'config.ini'))

    parser.add_argument('-s', '--source', dest='path', default=config['args']['path'],
                        help="the source file")
    parser.add_argument('-d', '--destination', dest='dest', default=config['args']['dest'],
                        help="the destination csv filename")

    args = parser.parse_args()

    config['args']['path'] = args.path
    config['args']['dest'] = args.dest

    # Initialize the Listdir object together with its arguments
    # path argument: The path of the directory
    # dest argument: The destination file
    listdir = ListDir(path=config['args']['path'], dest=config['args']['dest'])

    # Running the methods of the object
    # listdir.print_files()
    listdir.output_zip()
