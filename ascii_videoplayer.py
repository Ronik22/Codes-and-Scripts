import cv2
from PIL import Image
import os 
from os import path
import sys

filename = input("Enter filename of the video: ")
if not filename:
	print("Video file name is required")
	exit()
if not path.exists(filename):
	print("No such file found")
	exit()

textfname = input("Enter filename of the text file to save the output: ")
if not textfname:
	textfname = 'vascii.txt'

temp = open(textfname,'w')

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]  # characters acc to intensities

def gray_image_resized(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	resized_gray_image = image.resize((new_width,new_height)).convert('L')
	return resized_gray_image

def pix2ascii(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels]) # dividing by 25 to access the list positions
	return characters

def generate_frame(image,new_width=70):
	new_image = pix2ascii(gray_image_resized(image))

	total_pixels = len(new_image)

	ascii_image = "\n".join([new_image[index:(index+new_width)] for index in range(0, total_pixels, new_width)])

	sys.stdout.write(ascii_image)
	temp.write(ascii_image) # prints to a text file
	os.system('cls' if os.name == 'nt' else 'clear')


cap = cv2.VideoCapture(filename)

while True:

	ret,frame = cap.read()
	cv2.imshow("frame",frame)
	generate_frame(Image.fromarray(frame))
	cv2.waitKey(1)

temp.close()