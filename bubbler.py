#!/usr/bin/env python

from gimpfu import *

def bubbler(image, drawable, thickness):
	
	return
	
	
register(
	"Bubbler",
	"Create Speech Bubbles",
	"Create Speech Bubbles",
	"Bartholmew Black",
	"Bartholmew Black",
	"2022",
	"<Image>/Filters/Decor/Add Bubble...",
	"*",
	[
		(PF_INT, "thickness", "Thickness", 3)
	],
	[],
	bubbler)
	
main()
