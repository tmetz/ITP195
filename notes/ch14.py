"""

my_file = open("infile.txt", "r", encoding="utf_8" newline = "\n")

my_file.read() # reads the entire contents of the file as a string and returns it.

my_file.readline() # Delivers the next line as a string

my_file.readlines() # returns a single list of all the lines from the file

for line_str in my_file:
    print line_str


my_file.write(s) # writes the string s to the file

my_file.writelines(lst) # write a list of strings one at a time to the file

my_file.tell() # tells you your current cursor position

my_file.seek(100) # tells you what character to go to; in this case 100

my_file.seek(0, 100) # from the beginning to 100

my_file.seek(100, 1) # from the current position to 100 later - only for binary

my_file.seek(-100, 2) # go backwards from end


with open("filename.txt", "r") as my_file:
    do stuff
# automatically closes the file at the end so you don't have to remember




For csv files:

import csv

my_file = open('workbook1.csv', 'r')
workbook_reader = csv.reader(my_file)

for row in workbook_reader:
    print(row)



import os    # interface to operating system - we will use for file paths
c:\\windows\\users\\tmetz    # need a double back slash to escape the \

os.getcwd()   # returns path of current working directory
os.chdir(path_str)
os.listdir(path_str)   # directory listing

os.rename(source_path, dest_path)

os.mkdir(path_str)

os.remove(path_str)

os.rmdir(path_str)

os.walk(path_str) # starts at the dir in path_str and yields 3 values: dir_name, dir_list, and files

os.path.isfile(path_str)
os.path.isdir(path_str)
os.path.exists(path_str)

p = '/users/bill/python/myfile.py'
os.path.basename(p) # 'myfile.py'
os.path.dirname(p)  #  '/users/bill/python/
os.path.split(p) # [ '/users/bill/python/', 'myfile.py']
os.path.join(base_dir, file) # returns whole path

"""


"""
import os

def check(search_str, count, files_found_list, dirs_found_list):
    for dirname, dir_list, file_list in os.walk("."):
        for f in file_list:
            pass

"""

"""
a "finally" suite at the end of try-except block still runs some code whether
or not an error was caught and handled.

You can use an "else" at the end of a try-except block to run stuff that you only
want to run if you did not find any errors in the try block


# you don't have to wait for Python to throw an exception....

class MyException(Exception):
    pass   # Fill stuff in

if my_int < 0:
    raise MyException
"""



