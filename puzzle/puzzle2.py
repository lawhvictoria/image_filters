from sys import *

def commandline(argv):
   if len(argv) == 1:
      print "File not given!"
      exit()
   else:
      try:
         f = open(argv[1], 'r')
      except:
         print "File not found!"
         exit()

      return f

def print_color(color):
   red = int(color)*10
   if red < 255:
      return str(int(red))
   else:
      return "255"

def main():
   command = commandline(argv)

   lines = command.readlines()

   image = open('hidden10.ppm', 'w')
   image.write(lines[0])
   image.write(lines[1])
   image.write(lines[2])

   color_list = []
   for i in range(3, len(lines), 3):
      red = int(lines[i])*10
#      print lines[i]
#      print lines[i+1]
#      print lines[i+2]
      image.write(print_color(lines[i]) + ' ')
      image.write(print_color(lines[i]) + ' ')
      image.write(print_color(lines[i]) + ' ')

   image.close()

   return color_list



if __name__ == '__main__':
   main()

