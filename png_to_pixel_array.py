# this script exists solely cause i am bad with js
# i cannot figure out for the life of me how to just do it correctly and just import the image as pixels with js
# too bad!

from PIL import Image
import pyperclip

str = "var pixels = ["

with Image.open("original.png") as image:
	
	image = image.convert('RGB')

	for y in range(image.size[1]):
		for x in range(image.size[0]):
      
			pixel = image.getpixel((x, y))
   
			if pixel[0] + pixel[1] + pixel[2] > 0:
				str = str + f"new Pixel({x}, {y}, {pixel[0]}, {pixel[1]}, {pixel[2]}), "


str = str + "]"

pyperclip.copy(str)
print("done! dusted! incredible!")