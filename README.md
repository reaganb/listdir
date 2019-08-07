# Machine Problem: Date and Time

#### Requirements: 

1. Modify Machine Problem "Config files" to include the date and time in the filename of the output.
2. Use your best judgement on where to put it and how should it be formatted.
3. Commit your code to a branch named "with-date-filename" in the same project repository

## The listdir.py python script

The python script has the functionality to recursively read and list files of a directory path and write the output to another file (csv format) and archive that file (zip). The zip file has a name format combining csv format file name and the current date and time of creation (out.txt_YYYY-MM-DD-HHmmss.zip). The filename of the zip file conform to the ISO 8601 format standard.

### Prerequisites
1. Windows/Linux OS
2. Python 3

### Usage
The script will work as long as there is Python 3 installed on the system.
Check if it is installed by executing the following command on the terminal.
```
$ python --version
```

#### Examples:
```
$ python listdir.py
```
In this example, the script is executed as it is. It will still run despite that because the code has a config parser that provides a configuration file.

output (out.txt):
```
parent path,filename,filesize,md5,sha1
"C:\Users\USER\Projects\listdir", "listdir.py", 3837, b7800f7cb6c6b78cffcaf561e40169a8, 1c7fef433173171946f914294782195f4e873f99
"C:\Users\USER\Projects\listdir\lvl1", "1.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2", "2.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2", "2b.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3", "3.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3", "3b.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3", "3c.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4b.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4c.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
"C:\Users\USER\Projects\listdir\lvl1\lvl2\lvl3\lvl4", "4d.txt", 0, d41d8cd98f00b204e9800998ecf8427e, da39a3ee5e6b4b0d3255bfef95601890afd80709
```
Contents of config.ini
```
[args]
path = .
dest = out.txt
```
The ***args*** is the section and ***path*** and ***dest*** are its variables. Based on this configuration file, the path is the current working directory and the output file would be out.txt.

```
$ ls
```
One function of the script is that it will archive the output file into a zip type.

output:
```
listdir.py  out.txt out.txt_2019-08-07-133924.zip
```