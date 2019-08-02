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

#### Example:
```
$ python listdir.py . out.csv
```
In this example, the script is executed in the current directory (.) and assign out.csv as the output file.

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
***Note:*** The script is limited to only two arguments. The first is the directory path and the second is the output file (.csv). It will raise an error if a file path is placed as the first argument.

