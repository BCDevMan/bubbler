#!/usr/bin/env python

from gimpfu import *

def bubbler(image, drawable, thickness):
	new_layer = create_layer(image)
	draw_bubble(image, new_layer, thickness)
	pdb.gimp_selection_none(image)
	pdb.script_fu_drop_shadow(image, new_layer, 8, 8, 10, (0, 0, 0), 50, 1)
	pdb.gimp_image_merge_down(image, new_layer, 1)
#	new_layer = pdb.gimp_image_get_active_layer(image)
	new_layer = pdb.gimp_image_get_layer_by_name(image, 'Drop Shadow')
	pdb.gimp_item_set_name(new_layer, 'Speech Bubble')
	return

def draw_bubble(image, bubble_layer, thickness):
	pdb.gimp_image_set_active_layer(image, bubble_layer)
	
	foreground_color = pdb.gimp_context_get_foreground()
	
	pdb.gimp_context_set_foreground((0, 0, 0))
	pdb.gimp_edit_fill(bubble_layer, 0)
	
	pdb.gimp_selection_shrink(image, thickness)
	pdb.gimp_context_set_foreground((255, 255, 255))

	pdb.gimp_edit_fill(bubble_layer, 0)
	
	pdb.gimp_context_set_foreground(foreground_color)

	return
	
def create_layer(image):
	image_width = pdb.gimp_image_width(image)
	image_height = pdb.gimp_image_height(image)
	active_layer = pdb.gimp_image_get_active_layer(image)
	bubble_layer = pdb.gimp_layer_new(image, image_width, image_height, 0, 'Speech Bubble', 100, 0)
	pdb.gimp_layer_add_alpha(bubble_layer)
	pdb.gimp_drawable_fill(bubble_layer, 3)
	pdb.gimp_image_insert_layer(image, bubble_layer, None, 0)
	pdb.gimp_image_lower_item(image, bubble_layer)
	return bubble_layer
	
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
		(PF_INT, "thickness", "Thickness", 3),
	],
	[],
	bubbler)
	
main()
