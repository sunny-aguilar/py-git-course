#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """returns True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything ok.")
    sys.exit(0)


# adding this 1st change
# adding this 2nd change
# adding this 3rd change
main()



