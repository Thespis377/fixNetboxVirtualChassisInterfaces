#!/usr/bin/python3

import pynetbox
import argparse
import re
import sys


#try:
'''Get the command line arguments.'''
parser = argparse.ArgumentParser(description = 'Fixes the interface names in NetBox for switch stacks')
parser.add_argument('switch', nargs=1, help='The first switch in the stack')
parser.add_argument('-d', '--debug', dest='debug', action='store_true', default=False, help='Add for debug output')
args = parser.parse_args()

URL = "https://netbox.url"         #CHANGE ME
TOKEN = "MyCoolTokenFromNetBox"    #CHANGE ME

debug = args.debug      # Defuault is False
if not args.switch:
  print("A switch name needs to be given")
  sys.exit(0)

def stack(switch, nb):
  '''Changes the interface names to match the true stack names'''
  try:

    switch_ints = {}
    single_ints = nb.devices.filter(q=switch, status=1)  #Get all of the switches with similar names

    if not single_ints:
      print("This switch does not exist in NetBox: {}".format(switch))
      sys.exit(0)

    for i in single_ints:
      if debug:
        print("Switch name: {}".format(i))
      switch_ints[i] = nb.interfaces.filter(device=i)    #Get all of the interfaces for each switch
      m = re.match(r'.*-(\d+)', str(i))                        #Find the switch number, default 1
      num = "1"                                                #Default switch number
      if m:
        num = m.group(1)

      for j in switch_ints[i]:
        name = j.name                                          #Easier to manipulate a separate variable
        test = name.replace("Ethernet1", "Ethernet" + num)
        j.name = test
        if debug:
          print(test)

        j.save()
  except:
    print("There was an error while updating {} in NetBox".format(switch))


def main():
  ''' Call the stack function to update the interfaces in NetBox'''
  try:
    #Connect to NetBox
    api = pynetbox.api(url=URL, token=TOKEN)
    #Just shortens the calls later
    mynb = api.dcim

    if debug:
      print("1st Switch name: {}".format(args.switch[0]))
    stack(args.switch[0], mynb)
  
  except:
    print("There was an error in updating NetBox")

if __name__ == "__main__":
  main()

