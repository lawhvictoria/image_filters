from sys import*
from math import*

def groups_of_three(list):
   return_list = []
   group = []
   for i in range(len(list)):
      group.append(list[i])
      if (i + 1) % 3 == 0:
         return_list.append(group)
         group = []
   if group != []:
      return_list.append(group)
   return return_list

def commandline(argv):
   try:
      file = open(argv[1], 'r')
      return file
   except:
      print "File not found."
      exit()

def blur_arg(arg):
   try:
      neighbor_reach = int(arg[2])
      return neighbor_reach
   except:
      print "Neighbor argument not given. Now using default neighbor value 4."
      neighbor_reach = 4
      return neighbor_reach

def colordata_list(read_color, width):
   pixel_color = [c.split() for c in read_color]
   groups = groups_of_three(pixel_color)
   color_list = []
   line = []
   beginning = 0
   for pixel in groups:
      line.append([int(pixel[0][0]), int(pixel[1][0]), int(pixel[2][0])])
      beginning += 1
      if beginning == width:
         color_list.append(line)
         line = []
         beginning = 0
   return color_list

def blurred_image(width, height, updated):
   file = open('blurred_lights_10.ppm', 'w')
   file.write('P3\n')
   file.write(str(width)+' ')
   file.write(str(height)+'\n')
   file.write('255\n')
   for value in updated:
      file.write(value)

def blurring(colordata, width, height, neighbor_reach):
   blur_list = []
   for row in range(height):
      for col in range(width):
         avg_red = 0
         avg_green = 0
         avg_blue = 0
         avg_total = 0
         for x in range(max((col - neighbor_reach), 0),
                        min((col + neighbor_reach + 1), width)):
            for y in range(max((row - neighbor_reach), 0),
                           min((row + neighbor_reach + 1), height)):
               pixel = colordata[y][x]
               avg_red = avg_red + int(pixel[0])
               avg_green = avg_green + int(pixel[1])
               avg_blue = avg_blue + int(pixel[2])
               avg_total += 1
         total_red = int(avg_red / avg_total)
         total_green = int(avg_green / avg_total)
         total_blue = int(avg_blue / avg_total)
         blur_list.append(str(total_red) + ' ' + str(total_green) + ' ' + str(total_blue) + ' ')
   return blur_list

def main():
   openfile = commandline(argv)
   neighbor_reach = blur_arg(argv)
   openfile.readline()
   width_height = openfile.readline().split()
   width = int(width_height[0])
   height = int(width_height[1])
   openfile.readline()
   read_color = openfile.readlines()
   color_datalist = colordata_list(read_color, width)
   updated = blurring(color_datalist, width, height, neighbor_reach)
   blurred_image(width, height, updated)

if __name__ == '__main__':
   main()
