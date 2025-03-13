import os
#print(os.name)

#print(os.environ)

print(os.environ["TMP"])
print(os.getenv("TMP2"))

#print(os.getcwd())
#os.chdir(r"D:\Python Jupyter\Projects\Python 101")

#print(os.getcwd())
#os.mkdir("test")
#path = r'D:\Pytest\2025\03\12'
#os.makedirs(path)

print(os.getcwd())
#os.remove("mySnake.log")

#os.startfile(r"D:\GATech\HDDA\Code\Homework 1\Q1.pdf")

#print(os.path.basename(r"D:\GATech\HDDA\Code\Homework 1\Q1.pdf"))

print(os.path.dirname(r'C:\Python27\Tools\pynche\ChipViewer.py'))

print(os.path.exists(r'C:\Python27\Tools\pynche\ChipViewer.py'))
print(os.path.exists(r'C:\Python27\Tools\pynche\fake.py'))

print(os.path.join(r'C:\Python27\Tools\pynche','ChipViewer.py'))

dirname,fname = os.path.split(r'C:\Python27\Tools\pynche\fake.py')
print(dirname)
print(fname)

