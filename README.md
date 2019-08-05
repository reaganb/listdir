# Machine Problem: Config files

#### This machine problem builds on your work from on the previous one.
#### Requirements: 

1. Modify your work on Machine Problem "listdir with hashes" and create a config file for it
2. The config file should contain the input directory and the output file
3. Your application should still support the command line arguments for the value of the input directory and output file
4. If the command line argument is present, use its value instead of the value in the config file. If its not present, use the value of the config file
5. Commit your work in GitHub to a new branch named "config". Paste the link of the branch here.

## The listdir.py python script

The python script has the functionality to recursively read and list files of a directory path and write the output to another file (csv format) and archive that file (zip). 

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
One function of the script is that it will archive the output file into a zip format.

output:
```
listdir.py  out.txt out.txt.zip
```