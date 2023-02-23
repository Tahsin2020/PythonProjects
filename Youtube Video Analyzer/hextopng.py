import numpy as np
from PIL import Image

def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)

# Open a file: file
file = open('button.txt',mode='r')
 
# read all lines at once
all_of_it = file.read()
 
# close the file
file.close()

hex_array = all_of_it.split()
# print(hex_array)

rgb_array = []

for hex in hex_array:
   hex_number = hex.replace('#', '')
   rgb = hex_to_rgb(hex_number)
   rgb_array.append(rgb)

print(rgb_array)

width = 36
height = 36
im_array = np.zeros([height,width , 3], dtype=np.uint8)
count=0

for y in range(width):
    for x in range(height):
    # colour = 255 * i/width
    # im_array[:,i] = [colour, 255-colour , 255-colour]
        im_array[y,x]=rgb_array[count]
        count+=1


img = Image.fromarray(im_array)
img.save('grad.png')