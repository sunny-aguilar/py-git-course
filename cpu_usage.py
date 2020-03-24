#!/usr/bin/env python3
import psutil


def check_cpu_usage(percent):
    # patch command was used to fix the file using diff file
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("Everyting ok")
