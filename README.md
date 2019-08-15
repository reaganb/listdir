# Machine Problem: Logging

#### This machine problem builds on your code from Machine Problem "List Comprehensions and Generators".
1. Modify Machine Problem "List Comprehensions and Generators" to implement logging
    1. You must log both via stdout and on a rolling file
    2. Rolling file max limit should be 5mb with a maximum of 5 files
    3. Use YAML as the logging configuration format of the file

## The listdir module

The python module has the functionality to recursively read and list files of a directory path and write the output to another file (csv format) and archive that file (zip). The zip file has a name format combining csv format file name and the current date and time of creation (outputfile_YYYY-MM-DD-HHmmss.zip). The filename of the zip file conform to the ISO 8601 format standard.

### Prerequisites
1. Windows/Linux OS
2. Python 3

### Usage
The module will work as long as there is Python 3 installed on the system.
Check if it is installed by executing the following command on the terminal.
```
$ python --version
```

### Installation
```
$ git clone -b logging https://github.com/rgbtrend/listdir.git
```
Clone this branch
```
$ pip install .
```
Install this package


### Running the package as a script

#### Example
```
$ python -m listdir

"/home/user/Projects/listdir", "setup.py", 786, edaab1bfb00c687ea31cba9e6c1f037c, 4dc1759166e76cbbfb90690bd63ffbea133df6c0
2019-08-15 23:01:09,720 -- listdir.listdir -- INFO -- 
```
**sample output only**

Running without any arguments will produce the output(csv format) file, zip file, and log file. It will also print on the console the recursive list of files from the given directory path (.) in a logging format that is based on the yml configuration.
```
$ ls
files.txt files.txt_2019-08-XX-XXXXXX.zip rolling.log
``` 
The output filename is based on the config.ini file and the log filename is based on the config.yml file.
