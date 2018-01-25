import subprocess

cmd = r"aapt dump badging C:/Users/songjl/Documents/GitHub/appiumnAuto/img/y.apk | findstr launchable-activity:"#>>C:\Users\songjl\Desktop\python30\1.txt 2>&1"
result = ""
p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE, shell=True)
print(p.communicate())
