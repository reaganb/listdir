# Machine Problem: Packaging

#### Requirements: 

1. Use what you've learned about packaging Python projects and apply it to your project from Machine Problem "Date and Time"
2. Commit your code to GitHub and paste the link of the branch here. Name the branch as "packaging"

## The listdir module

The python module has the functionality to recursively read and list files of a directory path and write the output to another file (csv format) and archive that file (zip). The zip file has a name format combining csv format file name and the current date and time of creation (out.txt_YYYY-MM-DD-HHmmss.zip). The filename of the zip file conform to the ISO 8601 format standard.

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
$ pip install listdir-rgb
```


#### Importing the module
```
$ python3 # Run a Python 3 interpreter shell
>>> from listdir import ListDir
```

#### Create a ListDir object
```
>>> path = '.'
>>> dest = 'out.txt'
>>> ld = ListDir(path=path, dest=dest)
```
or
```
>>> ld = ListDir()
```
Either of the two will result the same object. The default path is the current working directory (.) and the default dest file is out.txt

#### Run the methods of the object
```
>>> ld.output_zip()
>>> exit()
$ ls .
lvl1 out.txt out.txt_2019-08-13-151455.zip 
```
The output_zip() will not return anything on the output. Exit the interpreter shell and list the directory/files of the given directory path. The method will produce the file and the versioned zip file.
```
>>> ld.print_files()
C:\Users\USER\Desktop\listdir-test\
C:\Users\USER\Desktop\listdir-test\lvl1
C:\Users\USER\Desktop\listdir-test\lvl1\1.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\2.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\2b.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\3.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\3b.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\3c.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\lvl4
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\lvl4\4.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\lvl4\4b.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\lvl4\4c.txt
C:\Users\USER\Desktop\listdir-test\lvl1\lvl2\lvl3\lvl4\4d.txt
```
The print_files() method returns a listed contents of the given directory path.
