import argparse
import configparser
import os.path as op
import listdir

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
    parser.add_argument('-j', '--json', dest='j_son', action="store_true", default=False,
                        help="enable JSON output")
    args = parser.parse_args()

    config['args']['path'] = args.path
    config['args']['dest'] = args.dest

    # Initialize the Listdir object together with its arguments
    # path argument: The path of the directory
    # dest argument: The destination file
    # yml_config argument: The yml config for logging
    # j_son argument: Set the flag for json format output
    listdir = listdir.ListDir(path=config['args']['path'], dest=config['args']['dest'],
                              yml_config=config['args']['yml_config'], j_son=args.j_son)

    # Running the method of the object
    listdir.output_zip()

