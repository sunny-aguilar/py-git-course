#!/usr/bin/env python
import suprocess
import os

src = "/data/prod/"
dest = "/data/prod/backup/"

for root, dirs, files in os.walk(src):

