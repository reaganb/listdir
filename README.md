# Machine Problem: JSON output

#### This machine problem builds on your code from Machine Problem "Logging". 

1. Modify Machine Problem 4 and add a functionality to output JSON instead of CSV
    1. This functionality is enabled when an argument is used
2. Commit your code to a branch named "json-output"
3. Paste the link to the branch here

## The listdir module

The python module has the functionality to recursively read and list files of a directory path and write the output to another file (csv or json format) and archive that file (zip). The zip file has a name format combining csv or json format file name and the current date and time of creation (outputfile_YYYY-MM-DD-HHmmss.zip). The filename of the zip file conform to the ISO 8601 format standard.

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
$ git clone -b json-output https://github.com/rgbtrend/listdir.git
```
Clone this branch
```
$ pip install .
```
Install this package


### Running the package as a script

#### Examples
```
$ python -m listdir
```
Running without any arguments will produce the output(csv format) file, zip file, and log file. It will also print on the console the recursive list of files from the given directory path in a logging format that is based on the yml configuration.
```
$ ls
files.txt files.txt_2019-08-XX-XXXXXX.zip rolling.log
``` 
The output filename is based on the config.ini file and the log filename is based on the config.yml file.

```
$ python -m listdir -j
$ ls
files.txt.json files.txt.json_2019-08-XX-XXXXXX.zip rolling.log
``` 
Providing the -j flag will produced a json format output file.
