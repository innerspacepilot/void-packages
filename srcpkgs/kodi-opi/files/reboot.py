#!/usr/bin/python2

import sys,os

if len(sys.argv) != 2:
  print ("exactly one parameter needed: <reboot|poweroff>")

if sys.argv[1] == "reboot":
  os.system('sudo reboot')
elif sys.argv[1] == "poweroff":
  os.system('sudo poweroff')
else:
  print ("wrong argument")

