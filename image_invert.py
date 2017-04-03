#!/usr/bin/env python
# coding=utf-8
# author:admin[@hackfun.org]
# license:GPL v3
# blog:hackfun.org

import Image

def image_invert():
	img = Image.open('input.png')
	img = img.convert('RGB')
	in_pixels = list(img.getdata())
 	out_pixels = list()
 
	for i in range(len(in_pixels)):
		r = in_pixels[i][0]
		g = in_pixels[i][1]
		b = in_pixels[i][2]
		out_pixels.append((255-r, 255-g, 255-b))
 
	out_img = Image.new(img.mode, img.size)
	out_img.putdata(out_pixels)
	out_img.save("output_inverted.png", "PNG")

def main():
	image_invert()

if __name__ == '__main__':
	main()