#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import necessary packages
import sys
from PIL import Image
import numpy as np
import argparse
import hashlib

parser = argparse.ArgumentParser(
    prog='./MegaDeObfuskator',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""############################################################
##################### MegaDeObfuskator #####################
############################################################
This unmalicious program aims to unmess pixels of an image to turn it intelligible.
You will need the exact software configuration for it to work but also my well kept super secret passphrase...
""")

parser.add_argument('-i','--image', required=True, help="Path to the picture you want to deobfuscate")
parser.add_argument('-p','--passphrase', required=True, help="Super secret passphrase that ensures no one will never revert-hack my image")
args=parser.parse_args()

# I should remember my version configurations to avoid troubles later
print("""Launching MegaDeObfuskator...
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()

  Software critical configuration:
      - Python: """+ ".".join([str(sys.version_info.major), str(sys.version_info.minor), str(sys.version_info.micro)]) + """
      - numpy: """ + np.__version__ )

print("Loading obfuscated picture...")
img = Image.open(args.image)

# Configuring random number generator with the passkey
seed = int(hashlib.md5(args.passphrase.encode('utf-8')).hexdigest(),16) % 2**32
np.random.seed(seed=seed)
# Creating a pseudo-random bit 3D array (width x hight x {R, G, B}) to add noise to the picture
randombitarray = np.random.randint(0,high=255,size=(img.width,img.height,3))

print("Pixel-based deobfuscation ongoing...")
for x in range(img.width):
  for y in range(img.height):
    basepixR,basepixG,basepixB = img.getpixel((x,y))

    newpixR = basepixR - randombitarray[x][y][0]
    newpixG = basepixG - randombitarray[x][y][1]
    newpixB = basepixB - randombitarray[x][y][2]

    if (newpixR <0):
      newpixR = newpixR+255
    if (newpixG <0):
      newpixG = newpixG+255
    if (newpixB <0):
      newpixB = newpixB+255
    img.putpixel((x,y),(newpixR,newpixG,newpixB))

print("Dumping result...")
img.save('restored.bmp')
print("""Mischief reverted...""")
