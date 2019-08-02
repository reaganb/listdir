# Machine Problem: listdir

#### Develop an application with the following requirements:

1. Take the path of a directory and list the files (recursively)
2. Output the files in a CSV  (comma separated value) file. 
3. Here are the columns of the CSV: parent path, filename, filesize
4. Here's what a row should look like: "D:\Downloads","setup.exe",1048576
5. The output filename should be set by the user using command line arguments
6. Commit your code in GitHub under the project listdir. Post the link to the project here

## The lisdir.py python script

The python script has the functionality to recursively read and list files of a directory path and write the output to another file (csv format). 

### Prerequisites
1. Windows/Linux OS
2. Python 3

### Usage
The script will work as long as there is Python 3 installed on the system.
Check if it is installed by executing the following command on the terminal.
```
$ python --version
```

### Modes

**PRINT** - List recursively the files/directories of the given path.

**WRITE** - Running the script with the -d option and a filename argument, it will write to a csv file with the given filename.

#### Examples:
```
$ python listdir.py .
```
The basic example using the default argument of providing the directory path only.

output:
```
C:\Users\USER\Projects\listdir\
C:\Users\USER\Projects\listdir\listdir.py
C:\Users\USER\Projects\listdir\lvl1
C:\Users\USER\Projects\listdir\lvl1\1.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2
C:\Users\USER\Projects\listdir\lvl1\lvl2\2.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\2b.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\3.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\3b.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\3c.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4\4.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4\4b.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4\4c.txt
C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4\4d.txt
```

```
$ python listdir.py . -d out
```
In this example, the script is executed in the current directory (.) and assign "out" as the output filename using the -d option.

output (out.csv):
```
parent path,filename,filesize
"C:\Users\USER\Projects\listdir", "exercise.py", 557
"C:\Users\USER\Projects\listdir", "listdir.py", 1922
"C:\Users\USER\Projects\listdir\lvl1", "1.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2", "2.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2", "2b.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3", "3.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3", "3b.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3", "3c.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4b.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4c.txt", 0
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4d.txt", 0
"C:\Users\USER\Projects\listdir", "out.csv", 0
"C:\Users\USER\Projects\listdir", "Pipfile", 151
"C:\Users\USER\Projects\listdir", "Pipfile.lock", 1916
"C:\Users\USER\Projects\listdir", "README.md", 1260
```
***Note:*** The script is limited to only two arguments. The first is the directory path and the second is the output filename which is optional. It will raise an error if a file path is placed as the first argument.

