#!/usr/bin/env python
import suprocess
import os

src = "/data/prod/"
dest = "/data/prod/backup/"

for root, dirs, files in os.walk(src):
    print(files)

subprocess.call(["rsync", "-arq", src, dest])


# dir path: student/data/prod prod_backup
# dir path: student/data/prod prod_backup
# dir path: student/scripts

