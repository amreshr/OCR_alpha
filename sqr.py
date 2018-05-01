>> import os
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Users\\Amresh\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.mkdir("amr.txt")
>>> os.rename("amr.txt","ani.txt")
>>> os.getcwd()
'C:\\Users\\Amresh\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.mkdir("lol")
>>> os.chdir("lol")
>>> os.getcwd()
'C:\\Users\\Amresh\\AppData\\Local\\Programs\\Python\\Python36-32\\lol'
>>> os.rename("lol","rofl")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'lol' -> 'rofl'
>>> os.chdir("..")
>>> os.rename("lol","rofl")
>>> os.getcwd()
'C:\\Users\\Amresh\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.chdir("..")
>>> os.chdir("Python36-32")
>>> os.chdir("rofl")
>>> os.getcwd()
'C:\\Users\\Amresh\\AppData\\Local\\Programs\\Python\\Python36-32\\rofl'