import os
from screeninfo import get_monitors
import shutil
import hashlib
from git import Repo

def get_info():
    login =os.getlogin()
    user_name = os.uname()[1]
    path = str(os.getcwd())
    keyboard_type = os.popen("setxkbmap -query").read()
    for m in get_monitors():
         height = str(m.height)
    drives = ""
    for el in os.popen("diskutil list").readlines():
        drives += str(el)
    disk_size = str(shutil.disk_usage("/")[0] // (2 ** 30))

    sysinfo_hash = hashlib.md5((login + user_name + path + keyboard_type + height + drives + disk_size).encode('utf-8')).hexdigest()
    return sysinfo_hash

path = input("Set the path of installation: ")
Repo.clone_from(git_url, path)
print("Done.")

sysinfo = get_info()
f = open('/home/' + os.getlogin() + '/lab2.txt', 'w')
f.write(sysinfo)
f.close()