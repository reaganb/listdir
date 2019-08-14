import zipfile
import hashlib
import glob
import logging
import logging.config
from datetime import datetime as dt
import os.path as op
import yaml
import json


class ListDir:
    """
    The ListDir class consist of functions for recursively
    listing of files in a certain path and writing it to another
    file (csv).
    """
    def __init__(self, path, dest, j_son=False):
        """The init function consists of the path and destination file(csv)
        properties

        Keyword arguments:
        path -- the directory path for recursive listing
        dest -- the output file
        """

        self.j_son = json

        self.setup_logging()
        self.logger = logging.getLogger(__name__)

        self.path = op.abspath(path)
        # Check if the path exist
        if not op.exists(self.path):
            self.logger.error('Path does not exist!')
            # print('Error: Path does not exist!')
            exit(0)
        # Check if only a path, not a file is given as the argument
        elif not op.isdir(self.path):
            self.logger.error('Path are only allowed as the argument')
            # print('Error: Path are only allowed as the argument')
            exit(0)

        self.csv_file = dest
        self.files = glob.iglob(f"{self.path}/**", recursive=True)

    @staticmethod
    def hash_file(file, algorithm='md5'):
        """The method for computing the checksum hashing of the file depending on the algorithm provided

        Arguments:
        file -- the directory path for recursive listing
        algorithm -- the algorithm to use (default 'md5')
        """

        block_size = 65536
        hasher = hashlib.md5()
        if algorithm == 'sha1':
            hasher = hashlib.sha1()

        with open(file, 'rb') as hash_file:
            buf = hash_file.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = hash_file.read(block_size)

        return hasher.hexdigest()

    def output_zip(self):
        """Create the csv format file from the recursive listing.
        It will also produce a versioned zip file with a date/time format."""

        today = dt.today()
        zip_datetime = today.strftime('%Y-%m-%d-%H%M%S')
        with zipfile.ZipFile(f'{self.csv_file}_{zip_datetime}.zip', 'w') as zip_file:

            if self.j_son:
                self.csv_file = f"{self.csv_file}.json"

            with open(self.csv_file, 'w+') as file:

                # Iterate through the self.files.
                # Check if the element is a file then pass it to the mdata_list() function
                # and append it to the generator object elements
                # Iterate through the generator object then write each element to the output file
                if not self.j_son:
                    file.write('parent path,filename,filesize,md5,sha1')
                    for line in (self.mdata_to_list(csv) for csv in self.files if op.isfile(csv)):
                        self.logger.info(f"\n{line}")
                        file.write(f"\n{line}")
                else:
                    data = []
                    for line in (self.mdata_to_list(csv) for csv in self.files if op.isfile(csv)):
                        self.logger.info(f"\n{line}")
                        data.append(line)
                    json.dump(data, file, indent=4)

            zip_file.write(self.csv_file)

    def mdata_to_list(self, csv):
        """A separate function to minimize the code in implementing generator comprehension
        on the output_zip method.

        Argument:
        csv -- the csv file path
        """

        directory = f"\"{op.dirname(csv)}\""
        file_name = f"\"{op.basename(csv)}\""
        md5 = self.hash_file(csv, 'md5')
        sha1 = self.hash_file(csv, 'sha1')
        size = op.getsize(csv)
        if not self.j_son:
            return f"{directory}, {file_name}, {size}, {md5}, {sha1}"
        else:
            directory = f"{op.dirname(csv)}"
            file_name = f"{op.basename(csv)}"
            return {
                'directory': directory,
                'file name': file_name,
                'size': size,
                'md5': md5,
                'sha1': sha1,
            }

    def setup_logging(self, default_path='config.yaml', default_level=logging.INFO):

        path = op.join(op.dirname(op.abspath(__file__)), default_path)
        if op.exists(path):
            print('yml exist')
            with open(path,'rt') as f:
                try:
                    config = yaml.safe_load(f.read())
                    logging.config.dictConfig(config)
                except Exception as e:
                    print(e)
                    print('Error in Logging Configuration. Using default configs')
                    logging.basicConfig(level=default_level)
        else:
            logging.basicConfig(level=default_level)
            print('Failed to load configuration file. Using default configs')