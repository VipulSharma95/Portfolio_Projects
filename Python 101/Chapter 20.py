import sys

print(sys.argv)

print(sys.executable)

#sys.exit(0)

#print(sys.path)
print(sys.platform)

os=sys.platform
if os=="win32":
    import winreg
    print(winreg)
elif os.startswith('linux'):
    import subprocess
    subprocess.Popen(["ls,-l"])


