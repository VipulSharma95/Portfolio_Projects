import subprocess

"""
code = subprocess.call("notepad.exe")
if code==0:
    print("success")
else:
    print("error")
"""

args = ["ping","www.yahoo.com"]
process = subprocess.Popen(args,stdout=subprocess.PIPE)

data=process.communicate()
for line in data:
    print(line)

#code = subprocess.call(["ping","www.yahoo.com"])
