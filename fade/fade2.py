from sys import *
from math import *

def commandline(argv):
   if len(argv) < 4:
      print "Missing Input Line Argument!!!"
      exit()
   else:
      try:
         f = open(argv[1], 'r')
      except:
         print "File not found!"
         exit()

      try:
         col = int(argv[2])
         row = int(argv[3])
         radius = int(argv[4])
      except:
         print "row, col, and radius must be an integer"
         exit()

      return f, col, row, radius

def pixel_color(color, scale):
   pixel_color = float(color)*scale
   return int(pixel_color)

def main():

   command = commandline(argv)
   f = command[0]
   col = command[1]
   row = command[2]
   radius = command[3]

   lines = f.readlines()
   image = open('faded_light_10.ppm', 'w')
   image.write(lines[0])
   image.write(lines[1])
   image.write(lines[2])
   image_widthall = lines[1].split() 
   image_width = image_widthall[0]

   x = 0
   y = 0

   for p in range(3, len(lines), 3):
      diff_distance = float(sqrt((row - x)**2 + (col - y)**2))
      scale_p = (radius - diff_distance)/float((radius))

      if scale_p < 0.2:
         scale_p = 0.2

      image.write(str(pixel_color(lines[p], scale_p)) + '\n')
      image.write(str(pixel_color(lines[p + 1], scale_p)) + '\n')
      image.write(str(pixel_color(lines[p + 2], scale_p)) + '\n')

      x = x + 1
      if x > (int(image_width) - 1):
         y = y + 1
         x = 0

   image.close()

if __name__ == '__main__':
   main()

