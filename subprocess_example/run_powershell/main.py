#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# PowerShell example: https://stackoverflow.com/documentation/powershell/822/getting-started-with-powershell/3444/allow-scripts-stored-on-your-machine-to-run-un-signed#t=20170819174703981402

FILE_NAME_POWERSHELL = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'

file_name_ps1 = 'hello_world.ps1'
command = FILE_NAME_POWERSHELL + ' -ExecutionPolicy Bypass -File ' + file_name_ps1

print('OS:')
import os
os.system(command)

print()
import subprocess

print('subprocess.call:')
retcode = subprocess.call(command, stderr=subprocess.STDOUT)
print(retcode)

print()
print('subprocess.check_output:')
output = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
print(output)

print()
print('subprocess.run:')
rs = subprocess.run(command)
print(rs.returncode)

print()
print('subprocess.Popen:')
from subprocess import Popen, PIPE, STDOUT
rs = Popen(command, universal_newlines=True, stdout=PIPE, stderr=STDOUT)
for line in rs.stdout:
    line = line.rstrip()
    print(line)
