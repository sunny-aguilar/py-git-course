#!/usr/bin/env python3
import os

def check_reboot():
    """returns True if the computer has a pending reboot"""
    return os.path.exist("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")

main()



