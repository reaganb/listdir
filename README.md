# Machine Problem: List Comprehensions and Generators

#### This machine problem builds on your work from on the previous one. 

1. Modify the previous Machine Problem to implement comprehensions and generators whenever if it's applicable
2. Commit your code to a branch named "list-comprehension-generators"

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

#### Run the methods of the object

```
>>> ld.output_zip()
>>> exit()
$ ls .
lvl1 out.txt out.txt_2019-08-13-151455.zip 
```
The output_zip() will not return anything on the output. Exit the interpreter shell and list the directory/files of the given directory path. The method produced the file and the versioned zip file.

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


#### Implementing List comprehension and Generators
```
def output_zip(self):
    """Create the csv format file from the recursive listing"""

    today = dt.today()
    zip_datetime = today.strftime('%Y-%m-%d-%H%M%S')
    with zipfile.ZipFile(f'{self.csv_file}_{zip_datetime}.zip', 'w') as zip_file:

        with open(self.csv_file, 'w+') as file:
            file.write('parent path,filename,filesize,md5,sha1')

            # Iterate through the self.files.
            # Check if the element is a file then pass it to the mdata_list() function
            # and append it to the generator object elements
            # Iterate through the generator object then write each element to the output file
            for line in (self.mdata_to_list(csv) for csv in self.files if op.isfile(csv)):
                file.write(f"\n{line}")
```
Instead of implementing list comprehension and generator in the module's code, I have decided to use a different technique. Combining the two would result to the usage of  a ***generator compression***. The syntax is the same with using list comprehension but it is more efficient in terms of memory usage. The code shown is a snippet of a method implementing generator comprehension from the listdir main module.



