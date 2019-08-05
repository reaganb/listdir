# Machine Problem: listdir with hashes

#### Add more features to the application you made in the previous Machine Problem. Here are the additional requirements:

1. Add 2 new columns to the output: md5 and sha1
2. The data under these columns should include the respective hashes of the file
3. The output file should be zipped
4. If the user set the output filename to be out.txt, it should now output out.txt.zip
5. Commit your code under the branch: listdir-with-hashes
6. Submit the link to the project here

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
$ python listdir.py . -d out.txt
```
In this example, the script is executed in the current directory (.) and assign out.txt as the output file.

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

```
$ ls
```
One function of the script is that it will archive the output file into a zip format.

output:
```
listdir.py  out.txt out.txt.zip
```
