#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import necessary packages
import sys
from PIL import Image
import numpy as np
import argparse
import hashlib

parser = argparse.ArgumentParser(
    prog='./obfuscate.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""############################################################
###################### MegaObfuskator ######################
############################################################
This malicious program aims to mess with pixels of an image to turn it unintelligible.
You will need the exact software configuration for it to work but also my well kept super secret passphrase...
""")

parser.add_argument('-i','--image', required=True, help="Path to the picture you want to obfuscate")
parser.add_argument('-p','--passphrase', required=True, help="Super secret passphrase that ensures no one will never revert-hack my image")
args=parser.parse_args()

# I should remember my version configurations to avoid troubles later
print("""Launching MegaObfuskator...
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠛⠛⠛⠛⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⢀⣀⣤⡴⠶⠶⢦⣤⣀⡀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣧⡀⠛⢻⡏⠀⠀⠀⠀⠀⠀⠉⣿⠛⠂⣼⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⡴⠾⢷⡄⢸⡇⠀⠀⠀⠀⠀⠀⢀⡟⢀⡾⠷⢦⣤⡀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⢁⣀⣀⣀⣻⣆⣻⣦⣤⣀⣀⣠⣴⣟⣡⣟⣁⣀⣀⣀⢻⡄⠀⠀⠀
⠀⠀⢀⡾⠁⣿⠉⠉⠀⠀⠉⠁⠉⠉⠉⠉⠉⠀⠀⠈⠁⠈⠉⠉⣿⠈⢿⡄⠀⠀
⠀⠀⣾⠃⠀⣿⠀⠀⠀⠀⠀⠀⣠⠶⠛⠛⠷⣤⠀⠀⠀⠀⠀⠀⣿⠀⠈⢷⡀⠀
⠀⣼⠃⠀⠀⣿⠀⠀⠀⠀⠀⢸⠏⢤⡀⢀⣤⠘⣧⠀⠀⠀⠀⠀⣿⠀⠀⠈⣷⠀
⢸⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠘⢧⣄⠁⠈⣁⣴⠏⠀⠀⠀⠀⠀⣿⠀⠀⠀⠘⣧
⠈⠳⣦⣀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠻⠶⠶⠟⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⣤⠞⠃
⠀⠀⠀⠙⠷⣿⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣀⣤⣠⣤⡀⠀⣤⣄⣿⡶⠋⠁⠀⠀
⠀⠀⠀⠀⠀⢿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⠀⠀⠀⠀⠀

  Software critical configuration:
      - Python: """+ ".".join([str(sys.version_info.major), str(sys.version_info.minor), str(sys.version_info.micro)]) + """
      - numpy: """ + np.__version__ )

print("Loading pristine picture...")
img = Image.open(args.image)

# Configuring random number generator with the passkey
seed = int(hashlib.md5(args.passphrase.encode('utf-8')).hexdigest(),16) % 2**32
np.random.seed(seed=seed)
# Creating a pseudo-random bit 3D array (width x hight x {R, G, B}) to add noise to the picture
randombitarray = np.random.randint(0,high=255,size=(img.width,img.height,3))

print("Pixel-based obfuscation ongoing...")
for x in range(img.width):
  for y in range(img.height):
    # Retrieving base pixel, one value per color
    basepixR,basepixG,basepixB = img.getpixel((x,y))

    # Modifying each color independantly
    newpixR = basepixR + randombitarray[x][y][0]
    newpixG = basepixG + randombitarray[x][y][1]
    newpixB = basepixB + randombitarray[x][y][2]

    # Pixel color value is between 0 and 255
    if (newpixR >255):
      newpixR = newpixR-255
    if (newpixG >255):
      newpixG = newpixG-255
    if (newpixB >255):
      newpixB = newpixB-255

    # Replacing pixel
    img.putpixel((x,y),(newpixR,newpixG,newpixB))

# Saving the result
print("Dumping result...")
img.save('obfuscated.bmp')
print("""Mischief managed...""")
