# Manifest of a serial-obfuscator

I designed this overly complicated softfware, the MegaObfuskator, to mess with the content of an image but in a reversible manner.
I however am not sure how for now...

The MegaObfuskator takes two arguments:
 - the picture to obfuscate
 - the passphrase to ensure having the same result and the reversibility of the process

It outputs the obfuscated picture in the file "obfuscated.bmp" and prevent anyone to understand what was the initial content.
The only thing I am sure about is that without my passphrase even the greatest mind cannot revert the process (muhahaha, how michievous of me !!!)!

For safety, I already develloped the MegaDeObfukator. As for the other one, it takes two arguments:
 - the picture to deobfuscate
 - the passphrase to unmess the pixels

 It outputs the retrieved picture to "restored.bmp"

Usage example:
./MegaDeObfuskator --image pic.bmp --passphrase MySuperPassphrase

Reminder, to install python:
https://www.python.org/downloads/release/python-368/

# Obfuscation algorithm

The obfuscation algorithm is well described in the following paragraphs although its sound chinese to me, it looks more like latin:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae nibh ac metus gravida mollis at vitae justo. Proin vitae bibendum odio. Nunc fermentum tincidunt augue sit amet suscipit. Praesent a ante massa. Maecenas neque arcu, scelerisque ut sapien sed, interdum consequat ante. In feugiat erat sit amet elit aliquet convallis. Quisque fermentum eu nisl at aliquam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vel arcu ligula. Aenean molestie nisi leo, ac consequat elit ornare vel. Fusce id sapien non risus malesuada tincidunt.

Pellentesque ipsum sem, volutpat venenatis odio quis, vestibulum porta orci. Nullam vel felis arcu. Morbi sollicitudin tincidunt mollis. Proin vulputate tellus metus, eu pharetra mi molestie eget. Aliquam erat volutpat. Phasellus pharetra justo eget erat consequat condimentum. Vestibulum rhoncus, mauris in sollicitudin congue, leo lacus dignissim dolor, vitae malesuada magna augue et ex. Duis ut nisl eros. Nulla sollicitudin urna lorem, a iaculis nisi faucibus et. Suspendisse ultrices mollis est non porttitor. Fusce mollis imperdiet luctus. Aliquam sed risus in quam semper elementum. Aenean eget eros ac urna elementum aliquet. Etiam sed imperdiet erat, at vehicula felis.

Curabitur magna dolor, semper quis metus sed, posuere consectetur lectus. Morbi semper sollicitudin consequat. Curabitur consequat ante dolor, sit amet imperdiet risus rutrum vel. Nulla facilisi. Praesent sit amet est posuere purus suscipit tincidunt at ut enim. Quisque varius augue eget aliquet sagittis. Aenean commodo feugiat purus. Curabitur tristique sed nisi a pretium. Nullam quam sem, molestie eu felis nec, tincidunt euismod purus. Ut lobortis ultrices euismod. Maecenas posuere euismod purus, at pharetra augue euismod egestas. Vivamus luctus cursus lacus non ullamcorper. Phasellus hendrerit sem eu nibh aliquam ullamcorper. Quisque consectetur suscipit consequat. Aliquam non volutpat nisl. Nullam consequat blandit libero vel volutpat.

Aliquam eleifend vitae arcu ut elementum. Morbi vel pulvinar tortor, vel faucibus erat. Integer nec dolor viverra, luctus arcu ac, elementum augue. In hac habitasse platea dictumst. Maecenas iaculis dolor est, in imperdiet enim ultricies sed. Pellentesque odio arcu, pellentesque sit amet ex id, tincidunt tincidunt metus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed pellentesque fringilla libero, non ultricies lectus condimentum at.

Aenean ultricies eros ac eros pulvinar dapibus. Sed odio nisi, varius id arcu et, ornare pretium sapien. Pellentesque cursus metus ex, sed imperdiet metus elementum quis. Proin feugiat justo eu neque suscipit faucibus. Duis sit amet ligula eu felis suscipit elementum id a metus. Donec sed nisi felis. Nunc et imperdiet nibh. Proin ullamcorper eget metus vitae ultrices. Donec bibendum quam sed tellus mollis, at lobortis elit mattis.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin nec faucibus nisi, ut ultricies tortor. Fusce eleifend ligula eu sapien elementum blandit. Morbi blandit orci magna, ac aliquet velit vestibulum in. Sed consectetur nisl facilisis nisl placerat mollis. Aenean id accumsan justo, eu volutpat orci. Nullam feugiat condimentum neque auctor imperdiet. Nam pellentesque posuere semper. Aenean auctor viverra ex id sodales. Sed at arcu blandit purus varius blandit in sed orci.

Vivamus aliquam ante pellentesque risus blandit hendrerit. Nulla id sodales dolor, in accumsan tellus. Praesent a neque a dolor facilisis fermentum. Etiam varius tellus nec molestie auctor. Maecenas bibendum bibendum orci, vitae vehicula ipsum mattis vitae. Etiam tincidunt vel velit non fringilla. Duis pretium leo vel leo laoreet egestas. Cras interdum libero quis neque molestie finibus.

Suspendisse potenti. Donec tristique vel velit id convallis. Suspendisse potenti. Vivamus vehicula a enim eu bibendum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non dui vel eros lacinia congue sed vel risus. Quisque rhoncus tortor vel eros molestie, in dapibus turpis elementum. Nam sit amet erat nisl. Donec ac lacus augue. Duis eu faucibus urna. Morbi tristique orci a risus auctor, faucibus aliquet libero varius. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Vestibulum at odio gravida, porttitor ante quis, blandit mauris. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse vitae tempor purus. Aenean a faucibus nisi, at tincidunt nulla. Nulla venenatis odio augue, id vehicula justo bibendum vitae. Fusce laoreet, lorem nec varius eleifend, dolor mi ultrices justo, eget maximus mauris nunc vitae nisi. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean dignissim nisi vitae risus posuere, vitae rutrum magna laoreet. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse lectus augue, lacinia vel semper quis, congue ut eros. Suspendisse id venenatis ex, vitae vestibulum velit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus vulputate sollicitudin imperdiet. Aliquam a nunc lectus. Mauris fermentum id ligula sit amet molestie. Cras quis sodales erat.

Vivamus at tempor nisl. Nulla quis mollis turpis. Aenean et tortor sem. Sed sem odio, porta quis aliquet sit amet, mattis vitae sem. Ut aliquet cursus dignissim. Donec tristique lectus efficitur metus feugiat pharetra vel sed augue. Praesent gravida nisl at nulla pulvinar scelerisque.




### Do not read under any circumstances if you are not me

Note to my 8 cats that are driving me crazy by behaving like a well known roman emperor and making me mess with my alphabet and numbers:
UgabmzgXizbvmz0802
