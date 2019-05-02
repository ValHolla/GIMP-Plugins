#!/usr/bin/env python
# vim: expandtab:ts=4:sw=4

'''Draw a G2 Crystal Tux using Vectors'''

from gimpfu import *

def get_coords_by_name(image, layer_name):
    '''Get coordinates by name'''

    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, layer_name))
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    pdb.gimp_selection_none(image)
    return x_1, y_1, x_2, y_2


def draw_body(image):
    '''Draw the Body Layer'''

    body_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B1" fill="none" stroke="black" stroke-width="1" d="M 191.55,45.00 C 197.33,59.30 196.46,75.14 199.89,90.00 204.25,108.93 213.75,119.91 214.00,141.00 214.42,177.06 196.44,209.60 162.00,223.55 147.40,229.46 138.40,230.18 123.00,230.00 92.69,229.64 61.71,207.56 49.87,180.00 43.10,164.23 42.81,154.65 43.00,138.00 43.16,124.27 52.23,103.28 55.58,88.00 55.58,88.00 62.03,49.00 62.03,49.00 69.93,24.13 90.87,8.08 116.00,3.44 148.33,-0.71 178.94,13.79 191.55,45.00 Z" /> </svg>'
    # Body Layer
    body_layer = gimp.Layer(image, "Body", 256, 256,
                            RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(body_layer, -1)
    body_layer.fill(TRANSPARENT_FILL)

    pdb.gimp_vectors_import_from_string(image, body_vector_string, -1, 1, 1)
    body_vector = pdb.gimp_image_get_vectors_by_name(image, "B1")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, body_vector)
    pdb.gimp_context_set_foreground((0, 0, 0))
    pdb.gimp_edit_fill(body_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, body_vector)
    pdb.gimp_selection_none(image)

def draw_tummy(image):
    '''Draw the Tummy layer'''

    # White Patch Layer
    patch_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B2" fill="none" stroke="black" stroke-width="1" d="M 130.00,86.22 C 136.01,86.07 141.31,87.52 147.00,89.34 177.72,99.19 196.95,132.65 197.00,164.00 197.00,164.00 197.00,173.00 197.00,173.00 196.91,180.71 193.72,197.51 189.78,203.99 187.08,208.43 181.30,212.43 177.00,215.33 163.67,224.31 150.72,228.11 135.00,230.56 126.03,231.96 116.72,229.97 108.00,227.87 95.59,224.88 75.12,215.43 67.65,204.99 63.10,198.63 59.04,178.01 59.00,170.00 58.82,130.69 80.26,93.97 121.00,86.22 121.00,86.22 130.00,86.22 130.00,86.22 Z" /> </svg>'
    pdb.gimp_context_set_foreground((208, 208, 208))
    pdb.gimp_context_set_background((171, 171, 171))
    patch_layer = gimp.Layer(image, "White Patch", 256, 256,
                             RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(patch_layer, -1)
    patch_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, patch_vector_string, -1, 1, 1)
    patch_vector = pdb.gimp_image_get_vectors_by_name(image, "B2")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, patch_vector)
    pdb.gimp_image_remove_vectors(image, patch_vector)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    x_pos = (x_2-(x_2-x_1)/2)
    pdb.gimp_edit_blend(patch_layer,
                        FG_BG_RGB_MODE,     # Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_2)         # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)

def draw_left_wing(image):
    '''Draw left wing layer'''

    left_wing_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B3" fill="none" stroke="black" stroke-width="1" d="M 58.00,93.00 C 58.00,93.00 55.61,124.00 55.61,124.00 55.13,126.26 53.54,129.79 52.58,132.00 51.31,134.92 48.90,140.43 46.61,142.49 44.40,144.48 37.32,146.26 34.00,147.60 34.00,147.60 15.00,156.89 15.00,156.89 11.72,157.93 8.05,157.94 6.92,153.94 5.37,148.45 13.61,138.72 17.09,135.00 17.09,135.00 41.96,113.00 41.96,113.00 49.43,105.19 50.52,101.42 56.00,93.00 56.00,93.00 58.00,93.00 58.00,93.00 Z" /> </svg>'

    # Left Wing Layer
    pdb.gimp_context_set_foreground((0, 0, 0))
    left_wing_layer = gimp.Layer(image, "Left Wing", 256, 256,
                                 RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(left_wing_layer, -1)
    left_wing_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, left_wing_vector_string, -1, 1, 1)
    left_wing_vector = pdb.gimp_image_get_vectors_by_name(image, "B3")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, left_wing_vector)
    pdb.gimp_edit_fill(left_wing_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, left_wing_vector)
    pdb.gimp_selection_none(image)

def draw_right_wing(image):
    ''' Draw right wing layer'''

    right_wing_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B4" fill="none" stroke="black" stroke-width="1" d="M 208.52,106.00 C 219.42,119.86 232.48,126.15 241.19,137.00 244.04,140.55 252.01,150.02 248.36,154.69 244.08,160.16 229.85,150.60 225.00,148.26 225.00,148.26 207.97,141.47 207.97,141.47 205.85,139.23 202.69,130.23 201.72,127.00 199.18,118.57 193.18,98.92 193.00,91.00 202.89,91.59 201.18,96.67 208.52,106.00 Z" /> </svg>'

    # Right Wing Layer
    pdb.gimp_context_set_foreground((0, 0, 0))
    right_wing_layer = gimp.Layer(image, "Right Wing", 256, 256,
                                  RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(right_wing_layer, -1)
    right_wing_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, right_wing_vector_string, -1, 1, 1)
    right_wing_vector = pdb.gimp_image_get_vectors_by_name(image, "B4")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, right_wing_vector)
    pdb.gimp_edit_fill(right_wing_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, right_wing_vector)
    pdb.gimp_selection_none(image)

def draw_left_foot(image):
    '''Draw left foot layer'''
    # Left Foot Layer
    left_foot_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B5" fill="none" stroke="black" stroke-width="1" d="M 115.83,210.00 C 121.25,216.68 126.19,230.52 115.83,235.69 113.03,237.18 109.23,236.99 106.00,237.00 106.00,237.00 52.00,237.00 52.00,237.00 48.81,237.00 44.93,237.18 42.18,235.69 32.01,230.51 36.74,216.65 42.18,210.01 51.91,198.65 63.42,197.18 77.00,195.46 90.59,194.77 106.71,199.28 115.83,210.00 Z" /> </svg>'
    pdb.gimp_context_set_foreground((223, 186, 0))
    left_foot_layer = gimp.Layer(image, "Left Foot", 256, 256,
                                 RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(left_foot_layer, -1)
    left_foot_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, left_foot_vector_string, -1, 1, 1)
    left_foot_vector = pdb.gimp_image_get_vectors_by_name(image, "B5")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, left_foot_vector)
    pdb.gimp_edit_fill(left_foot_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, left_foot_vector)
    pdb.gimp_selection_shrink(image, 7)
    left_foot_glow_layer = gimp.Layer(image, "Left Foot Glow", 256, 256,
                                      RGBA_IMAGE, 85, NORMAL_MODE)
    image.add_layer(left_foot_glow_layer, -1)
    pdb.gimp_context_set_foreground((240, 244, 0))
    pdb.gimp_context_set_background((248, 192, 0))
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    y_pos = (y_2-(y_2-y_1)/2)
    pdb.gimp_edit_blend(left_foot_glow_layer,
                        FG_BG_RGB_MODE,     # Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_1+7, y_pos,       # Blend X,Y Startpoint
                        x_2-7, y_pos)       # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, left_foot_glow_layer, 10.0, 10.0, 1)

def draw_right_foot(image):
    '''Draw right foot layer'''

    # Right Foot Layer
    right_foot_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B6" fill="none" stroke="black" stroke-width="1" d="M 215.10,210.09 C 219.88,216.01 224.83,229.49 216.79,234.91 213.46,237.16 208.84,236.99 205.00,237.00 205.00,237.00 150.00,237.00 150.00,237.00 142.93,236.91 136.28,235.24 135.23,227.00 134.75,223.29 136.33,219.31 137.89,216.00 145.22,200.51 160.84,197.50 176.00,195.44 188.99,194.40 206.72,199.71 215.10,210.09 Z" /> </svg>'
    pdb.gimp_context_set_foreground((223, 186, 0))
    right_foot_layer = gimp.Layer(image, "Right Foot", 256, 256,
                                  RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(right_foot_layer, -1)
    right_foot_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, right_foot_vector_string, -1, 1, 1)
    right_foot_vector = pdb.gimp_image_get_vectors_by_name(image, "B6")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, right_foot_vector)
    pdb.gimp_edit_fill(right_foot_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, right_foot_vector)
    pdb.gimp_selection_shrink(image, 7)
    right_foot_glow_layer = gimp.Layer(image, "Right Foot Glow", 256, 256,
                                       RGBA_IMAGE, 85, NORMAL_MODE)
    image.add_layer(right_foot_glow_layer, -1)
    pdb.gimp_context_set_foreground((248, 192, 0))
    pdb.gimp_context_set_background((240, 244, 0))
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    y_pos = (y_2-(y_2-y_1)/2)
    pdb.gimp_edit_blend(right_foot_glow_layer,
                        FG_BG_RGB_MODE,     # Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_1+7, y_pos,       # Blend X,Y Startpoint
                        x_2-7, y_pos)       # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, right_foot_glow_layer, 10.0, 10.0, 1)

def draw_right_eyelid(image):
    '''Draw right eyelid layer'''

    # Right Eyelid Layer
    right_eyelid_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B7" fill="none" stroke="black" stroke-width="1" d="M 177.00,91.00 C 177.00,91.00 131.00,91.00 131.00,91.00 128.60,91.00 124.48,91.24 122.48,89.83 120.13,88.15 120.08,84.61 120.01,82.00 119.83,74.96 120.80,68.38 123.99,62.00 137.77,34.45 175.22,37.68 185.30,66.00 188.96,76.27 187.21,80.30 187.00,90.00 182.16,90.87 181.99,90.98 177.00,91.00 Z" /> </svg>'
    pdb.gimp_context_set_foreground((0, 0, 0))
    right_eyelid_layer = gimp.Layer(image, "Right Eyelid", 256, 256,
                                    RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(right_eyelid_layer, -1)
    right_eyelid_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, right_eyelid_vector_string, -1, 1, 1)
    right_eyelid_vector = pdb.gimp_image_get_vectors_by_name(image, "B7")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, right_eyelid_vector)
    pdb.gimp_edit_fill(right_eyelid_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, right_eyelid_vector)
    pdb.gimp_selection_none(image)

    ## Right Eyelid Reflection
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Right Eyelid"))
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Eyelid")
    right_eyelid_reflection_layer = gimp.Layer(image, "Right Eyelid Reflection", 256, 256,
                                               RGBA_IMAGE, 80, NORMAL_MODE)
    image.add_layer(right_eyelid_reflection_layer, layer_pos)
    right_eyelid_reflection_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image,
                                                                "Right Eyelid"))
    pdb.gimp_selection_shrink(image, 2)
    x_pos = x_2-((x_2-x_1)/2)
    y_pos = y_2-((y_2-y_1)/2)
    pdb.gimp_edit_blend(right_eyelid_reflection_layer,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_pos)       # Blend X,Y Endpoint

    pdb.gimp_selection_translate(image, 0, 3)
    pdb.gimp_edit_cut(right_eyelid_reflection_layer)
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, right_eyelid_reflection_layer, 2.0, 2.0, 1)

def draw_left_eyelid(image):
    ''' Draw left eyelid layer'''
    # Left Eyelid Layer
    left_eyelid_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B8" fill="none" stroke="black" stroke-width="1" d="M 133.98,61.00 C 135.28,67.44 135.50,74.50 133.98,81.00 133.76,83.14 133.13,86.63 131.30,88.01 129.65,89.26 126.03,89.00 124.00,89.00 124.00,89.00 83.00,89.00 83.00,89.00 80.87,89.00 77.27,89.23 75.51,87.98 71.51,85.14 71.95,73.52 72.00,69.00 72.19,53.54 81.19,37.24 97.00,33.47 116.78,30.70 129.34,42.19 133.98,61.00 Z" /> </svg>'
    pdb.gimp_context_set_foreground((0, 0, 0))
    left_eyelid_layer = gimp.Layer(image, "Left Eyelid", 256, 256,
                                   RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(left_eyelid_layer, -1)
    left_eyelid_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, left_eyelid_vector_string, -1, 1, 1)
    left_eyelid_vector = pdb.gimp_image_get_vectors_by_name(image, "B8")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, left_eyelid_vector)
    pdb.gimp_edit_fill(left_eyelid_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, left_eyelid_vector)
    pdb.gimp_selection_none(image)

    ## Left Eyelid Reflection
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Left Eyelid"))
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Eyelid")
    left_eyelid_reflection_layer = gimp.Layer(image, "Left Eyelid Reflection", 256, 256,
                                              RGBA_IMAGE, 80, NORMAL_MODE)
    image.add_layer(left_eyelid_reflection_layer, layer_pos)
    left_eyelid_reflection_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image,
                                                                "Left Eyelid"))
    pdb.gimp_selection_shrink(image, 2)
    x_pos = x_2-((x_2-x_1)/2)
    y_pos = y_2-((y_2-y_1)/2)
    pdb.gimp_edit_blend(left_eyelid_reflection_layer,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_pos)       # Blend X,Y Endpoint

    pdb.gimp_selection_translate(image, 0, 3)
    pdb.gimp_edit_cut(left_eyelid_reflection_layer)
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, left_eyelid_reflection_layer, 2.0, 2.0, 1)

def draw_right_eye(image):
    '''Draw Right Eye'''
    # Right Eye Layer
    right_eye_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B9" fill="none" stroke="black" stroke-width="1" d="M 172.61,61.02 C 183.29,74.38 173.57,91.60 158.00,94.53 150.45,95.96 140.85,93.90 135.10,88.67 125.53,79.96 125.98,65.66 136.04,57.53 139.82,54.48 143.39,53.49 148.00,52.46 157.39,51.17 166.44,53.29 172.61,61.02 Z" /> </svg>'
    pdb.gimp_context_set_foreground((165, 165, 165))
    pdb.gimp_context_set_background((148, 148, 148))
    right_eye_layer = gimp.Layer(image, "Right Eye", 256, 256,
                                 RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(right_eye_layer, -1)
    right_eye_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, right_eye_vector_string, -1, 1, 1)
    right_eye_vector = pdb.gimp_image_get_vectors_by_name(image, "B9")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, right_eye_vector)
    pdb.gimp_image_remove_vectors(image, right_eye_vector)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(right_eye_layer,
                        FG_BG_RGB_MODE,     # Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_2)         # Blend X,Y Endpoint
    pdb.gimp_selection_shrink(image, 7)
    right_eye_glow_layer = gimp.Layer(image, "Right Eye Glow", 256, 256,
                                      RGBA_IMAGE, 85, NORMAL_MODE)
    image.add_layer(right_eye_glow_layer, -1)
    pdb.gimp_context_set_foreground((222, 219, 222))
    pdb.gimp_edit_fill(right_eye_glow_layer, FOREGROUND_FILL)
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, right_eye_glow_layer, 10.0, 10.0, 1)

    # Reflection for Right Eye Top
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Right Eye Glow"))
    right_eye_reflection_layer_top = gimp.Layer(image, "Right Eye Reflection Top", 256, 256,
                                                RGBA_IMAGE, 85, NORMAL_MODE)
    image.add_layer(right_eye_reflection_layer_top, layer_pos)
    right_eye_reflection_layer_top.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Eye")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Right Eye"))
    pdb.gimp_selection_shrink(image, 2)
    x_pos = x_2-((x_2-x_1)/2)
    y_pos = y_2-((y_2-y_1)/2)
    pdb.gimp_edit_blend(right_eye_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_pos)       # Blend X,Y Endpoint

    pdb.gimp_selection_translate(image, -11, 5)
    pdb.gimp_edit_cut(right_eye_reflection_layer_top)
    pdb.gimp_selection_translate(image, 15, -22)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(right_eye_reflection_layer_top)
    pdb.gimp_selection_none(image)

    # Reflection for Right Eye Bottom
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Right Eye Glow"))
    right_eye_reflection_layer_bottom = gimp.Layer(image, "Right Eye Reflection Bottom", 256, 256,
                                                   RGBA_IMAGE, 40, NORMAL_MODE)
    image.add_layer(right_eye_reflection_layer_bottom, layer_pos)
    right_eye_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Eye")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Right Eye"))
    pdb.gimp_selection_shrink(image, 2)
    x_pos = x_2-((x_2-x_1)/2)
    y_pos = y_2-((y_2-y_1)/2)
    pdb.gimp_edit_blend(right_eye_reflection_layer_bottom,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_2,         # Blend X,Y Startpoint
                        x_pos, y_pos)       # Blend X,Y Endpoint
    pdb.gimp_selection_translate(image, 1, -7)
    pdb.gimp_edit_cut(right_eye_reflection_layer_bottom)
    pdb.gimp_selection_none(image)

def draw_left_eye(image):
    '''Draw Left Eye Layer'''

    # Left Eye Layer
    left_eye_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B11" fill="none" stroke="black" stroke-width="1" d="M 109.00,101.61 C 95.35,104.58 85.47,95.43 81.72,83.00 76.84,66.81 82.10,46.45 100.00,41.52 133.70,36.28 137.02,95.51 109.00,101.61 Z" /> </svg>'
    pdb.gimp_context_set_foreground((165, 165, 165))
    pdb.gimp_context_set_background((148, 148, 148))
    left_eye_layer = gimp.Layer(image, "Left Eye", 256, 256,
                                RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(left_eye_layer, -1)
    left_eye_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, left_eye_vector_string, -1, 1, 1)
    left_eye_vector = pdb.gimp_image_get_vectors_by_name(image, "B11")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, left_eye_vector)
    pdb.gimp_image_remove_vectors(image, left_eye_vector)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(left_eye_layer,
                        FG_BG_RGB_MODE,     # Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_2)         # Blend X,Y Endpoint
    pdb.gimp_selection_shrink(image, 7)
    left_eye_glow_layer = gimp.Layer(image, "Left Eye Glow", 256, 256,
                                     RGBA_IMAGE, 85, NORMAL_MODE)
    image.add_layer(left_eye_glow_layer, -1)
    pdb.gimp_context_set_foreground((222, 219, 222))
    pdb.gimp_edit_fill(left_eye_glow_layer, FOREGROUND_FILL)
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, left_eye_glow_layer, 10.0, 10.0, 1)

    # Reflection for Left Eye Top
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Left Eye Glow"))
    left_eye_reflection_layer_top = gimp.Layer(image, "Left Eye Reflection Top", 256, 256,
                                               RGBA_IMAGE, 85, NORMAL_MODE)
    image.add_layer(left_eye_reflection_layer_top, layer_pos)
    left_eye_reflection_layer_top.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Eye")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Eye"))
    pdb.gimp_selection_shrink(image, 2)
    x_pos = x_2-((x_2-x_1)/2)
    y_pos = y_2-((y_2-y_1)/2)
    pdb.gimp_edit_blend(left_eye_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_pos)       # Blend X,Y Endpoint

    pdb.gimp_selection_translate(image, -15, 4)
    pdb.gimp_edit_cut(left_eye_reflection_layer_top)
    pdb.gimp_selection_translate(image, 20, -28)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(left_eye_reflection_layer_top)
    pdb.gimp_selection_none(image)

    # Reflection for Left Eye Bottom
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Left Eye Glow"))
    left_eye_reflection_layer_bottom = gimp.Layer(image, "Left Eye Reflection Bottom", 256, 256,
                                                  RGBA_IMAGE, 40, NORMAL_MODE)
    image.add_layer(left_eye_reflection_layer_bottom, layer_pos)
    left_eye_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Eye")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Eye"))
    pdb.gimp_selection_shrink(image, 2)
    x_pos = x_2-((x_2-x_1)/2)
    y_pos = y_2-((y_2-y_1)/2)
    pdb.gimp_edit_blend(left_eye_reflection_layer_bottom,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_2,         # Blend X,Y Startpoint
                        x_pos, y_pos)       # Blend X,Y Endpoint
    pdb.gimp_selection_translate(image, 8, -8)
    pdb.gimp_edit_cut(left_eye_reflection_layer_bottom)
    pdb.gimp_selection_none(image)

def draw_right_pupil(image):
    '''Draw Right Pupil'''

    # Right Pupil Layer
    right_pupil_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B10" fill="none" stroke="black" stroke-width="1" d="M 137.79,82.81 C 133.85,84.95 130.45,81.70 129.43,78.00 128.10,73.18 129.25,69.10 133.11,66.07 143.33,63.59 144.18,79.33 137.79,82.81 Z" /> </svg>'
    pdb.gimp_context_set_foreground((0, 0, 0))
    right_pupil_layer = gimp.Layer(image, "Right Pupil", 256, 256,
                                   RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(right_pupil_layer, -1)
    right_pupil_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, right_pupil_vector_string, -1, 1, 1)
    right_pupil_vector = pdb.gimp_image_get_vectors_by_name(image, "B10")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, right_pupil_vector)
    pdb.gimp_edit_fill(right_pupil_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, right_pupil_vector)
    pdb.gimp_selection_none(image)

    # Reflection for Right Pupil Top
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Right Pupil"))
    right_pupil_reflection_layer_top = gimp.Layer(image, "Right Pupil Reflection Top", 256, 256,
                                                  RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(right_pupil_reflection_layer_top, layer_pos)
    right_pupil_reflection_layer_top.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Pupil")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image,
                                                                "Right Pupil"))
    pdb.gimp_selection_shrink(image, 1)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(right_pupil_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_2)         # Blend X,Y Endpoint

    pdb.gimp_selection_translate(image, -2, 3)
    pdb.gimp_edit_cut(right_pupil_reflection_layer_top)
    pdb.gimp_selection_translate(image, 4, -14)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(right_pupil_reflection_layer_top)
    pdb.gimp_selection_none(image)

    # Reflection for Right Pupil Bottom
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Right Pupil"))
    right_pupil_reflection_layer_bottom = gimp.Layer(image, "Right Pupil Reflection Bottom",
                                                     256, 256, RGBA_IMAGE, 60, NORMAL_MODE)
    image.add_layer(right_pupil_reflection_layer_bottom, layer_pos)
    right_pupil_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Pupil")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Right Pupil"))
    pdb.gimp_selection_shrink(image, 1)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(right_pupil_reflection_layer_bottom,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_2,         # Blend X,Y Startpoint
                        x_pos, y_1)         # Blend X,Y Endpoint
    pdb.gimp_selection_translate(image, 1, -3)
    pdb.gimp_edit_cut(right_pupil_reflection_layer_bottom)
    pdb.gimp_selection_none(image)

def draw_left_pupil(image):
    '''Draw Left pupil layer'''

    # Left Pupil Layer
    left_pupil_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B12" fill="none" stroke="black" stroke-width="1" d="M 120.02,84.34 C 113.56,82.45 110.99,70.10 119.05,64.04 132.98,60.36 131.00,87.57 120.02,84.34 Z" /> </svg>'
    pdb.gimp_context_set_foreground((0, 0, 0))
    left_pupil_layer = gimp.Layer(image, "Left Pupil", 256, 256,
                                  RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(left_pupil_layer, -1)
    left_pupil_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, left_pupil_vector_string, -1, 1, 1)
    left_pupil_vector = pdb.gimp_image_get_vectors_by_name(image, "B12")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, left_pupil_vector)
    pdb.gimp_edit_fill(left_pupil_layer, FOREGROUND_FILL)
    pdb.gimp_image_remove_vectors(image, left_pupil_vector)
    pdb.gimp_selection_none(image)

    # Reflection for Left Pupil Top
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Left Pupil"))
    left_pupil_reflection_layer_top = gimp.Layer(image, "Left Pupil Reflection Top",
                                                 256, 256, RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(left_pupil_reflection_layer_top, layer_pos)
    left_pupil_reflection_layer_top.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Pupil")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Pupil"))
    pdb.gimp_selection_shrink(image, 1)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(left_pupil_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_2)         # Blend X,Y Endpoint

    pdb.gimp_selection_translate(image, -2, 3)
    pdb.gimp_edit_cut(left_pupil_reflection_layer_top)
    pdb.gimp_selection_translate(image, 4, -14)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(left_pupil_reflection_layer_top)
    pdb.gimp_selection_none(image)

    # Reflection for Left Pupil Bottom
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Left Pupil"))
    left_pupil_reflection_layer_bottom = gimp.Layer(image, "Left Pupil Reflection Bottom",
                                                    256, 256, RGBA_IMAGE, 60, NORMAL_MODE)
    image.add_layer(left_pupil_reflection_layer_bottom, layer_pos)
    left_pupil_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Pupil")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image,
                                                                "Left Pupil"))
    pdb.gimp_selection_shrink(image, 1)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(left_pupil_reflection_layer_bottom,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_2,         # Blend X,Y Startpoint
                        x_pos, y_1)         # Blend X,Y Endpoint
    pdb.gimp_selection_translate(image, 3, -1)
    pdb.gimp_edit_cut(left_pupil_reflection_layer_bottom)
    pdb.gimp_selection_none(image)


def draw_beak(image):
    '''Draw beak layer'''

    # Beak Layer
    beak_vector_string = '<svg xmlns="http://www.w3.org/2000/svg" width="35.5556mm" height="35.5556mm" viewBox="0 0 256 256"> <path id="B13" fill="none" stroke="black" stroke-width="1" d="M 149.50,94.10 C 152.60,100.41 140.50,112.49 136.42,116.96 134.53,119.03 132.85,120.89 130.00,121.55 123.60,123.04 112.18,109.70 108.33,105.00 106.61,102.90 104.35,99.87 104.65,97.00 105.37,90.12 116.52,87.65 122.00,86.46 129.20,85.47 145.85,86.67 149.50,94.10 Z" /> </svg>'
    pdb.gimp_context_set_foreground((220, 160, 14))
    pdb.gimp_context_set_background((220, 184, 12))
    beak_layer = gimp.Layer(image, "Beak", 255, 255,
                            RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(beak_layer, -1)
    beak_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_vectors_import_from_string(image, beak_vector_string, -1, 1, 1)
    beak_vector = pdb.gimp_image_get_vectors_by_name(image, "B13")
    pdb.gimp_image_select_item(image, CHANNEL_OP_ADD, beak_vector)
    pdb.gimp_image_remove_vectors(image, beak_vector)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)

    pdb.gimp_edit_blend(beak_layer,
                        FG_BG_RGB_MODE,     # Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_1, y_1,           # Blend X,Y Startpoint
                        x_2, y_1)           # Blend X,Y Endpoint
    pdb.gimp_selection_shrink(image, 7)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    beak_glow_layer = gimp.Layer(image, "Beak Glow", 256, 256,
                                 RGBA_IMAGE, 85, NORMAL_MODE)
    image.add_layer(beak_glow_layer, -1)
    pdb.gimp_context_set_foreground((240, 244, 0))
    pdb.gimp_context_set_background((248, 192, 0))
    pdb.gimp_edit_blend(beak_glow_layer,
                        FG_BG_RGB_MODE,     # Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_1, y_1+4,         # Blend X,Y Startpoint
                        x_2, y_1+4)         # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, beak_glow_layer, 10.0, 10.0, 1)

    pdb.gimp_selection_none(image)

def add_body_reflections(image):
    '''Draw Body Reflection'''

    # Create new layer and add above the Body layer
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Body"))
    body_reflection_layer_top = gimp.Layer(image, "Body Reflection Top", 256, 256,
                                           RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(body_reflection_layer_top, layer_pos)
    body_reflection_layer_top.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Eye")
    pdb.gimp_ellipse_select(image, x_1-59, y_1-47, 119, 103,
                            CHANNEL_OP_ADD, False, False, 1)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(body_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1+8,       # Blend X,Y Startpoint
                        x_pos, y_2)         # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, body_reflection_layer_top, 2.0, 2.0, 1)

    body_reflection_layer_bottom = gimp.Layer(image, "Body Reflection Bottom",
                                              256, 256, RGBA_IMAGE, 60, NORMAL_MODE)
    image.add_layer(body_reflection_layer_bottom, layer_pos+1)
    body_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    beak_x_1, beak_y_1, beak_x_2, beak_y_2 = get_coords_by_name(image, "Beak")
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Body")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Body"))
    pdb.gimp_selection_shrink(image, 2)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(body_reflection_layer_bottom,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_2,         # Blend X,Y Startpoint
                        x_pos, beak_y_2)    # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "White Patch")
    pdb.gimp_ellipse_select(image, x_1-30, y_1-45, 200, 160,
                            CHANNEL_OP_ADD, False, False, 1)
    pdb.gimp_edit_cut(body_reflection_layer_bottom)
    pdb.gimp_selection_none(image)

    # Beak Reflection Top
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Beak Glow"))
    beak_reflection_layer_top = gimp.Layer(image, "Beak Reflection Top", 256, 256,
                                           RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(beak_reflection_layer_top, layer_pos)
    beak_reflection_layer_top.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Beak")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Beak"))
    pdb.gimp_selection_shrink(image, 2)

    pdb.gimp_edit_blend(beak_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_2, y_1,           # Blend X,Y Startpoint
                        x_1, y_2)           # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Eye")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Right Eye"))
    pdb.gimp_selection_translate(image, -42, 40)
    pdb.gimp_edit_cut(beak_reflection_layer_top)
    pdb.gimp_selection_none(image)

    # Beak Reflection Bottom
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Beak Glow"))
    beak_reflection_layer_bottom = gimp.Layer(image, "Beak Reflection Bottom", 256, 256,
                                              RGBA_IMAGE, 50, NORMAL_MODE)
    image.add_layer(beak_reflection_layer_bottom, layer_pos)
    beak_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Beak")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Beak"))
    pdb.gimp_selection_shrink(image, 2)
    pdb.gimp_edit_blend(beak_reflection_layer_bottom,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_1, y_2,           # Blend X,Y Startpoint
                        x_2, y_1)           # Blend X,Y Endpoint
    pdb.gimp_selection_translate(image, 4, -2)
    pdb.gimp_edit_cut(beak_reflection_layer_bottom)
    pdb.gimp_selection_none(image)

    # White Patch Reflection Top
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "White Patch"))
    white_patch_reflection_layer_top = gimp.Layer(image, "White Patch Reflection Top",
                                                  256, 256, RGBA_IMAGE, 50, NORMAL_MODE)
    image.add_layer(white_patch_reflection_layer_top, layer_pos)
    white_patch_reflection_layer_top.fill(TRANSPARENT_FILL)
    x_1, foot_y_1, x_2, y_2 = get_coords_by_name(image, "Left Foot")
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "White Patch")
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_ellipse_select(image, x_1+5, y_1-19, 127, 165,
                            CHANNEL_OP_ADD, False, False, 1)
    pdb.gimp_edit_blend(white_patch_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, foot_y_1)    # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image,
                                                                "White Patch"))
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(white_patch_reflection_layer_top)
    pdb.gimp_selection_none(image)

    # White Patch Reflection Layer Bottom
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "White Patch"))
    white_patch_reflection_layer_bottom = gimp.Layer(image, "White Patch Reflection Bottom",
                                                     256, 256, RGBA_IMAGE, 40, NORMAL_MODE)
    image.add_layer(white_patch_reflection_layer_bottom, layer_pos)
    white_patch_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    x_1, foot_y_1, x_2, y_2 = get_coords_by_name(image, "Left Foot")
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "White Patch")
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image,
                                                                "White Patch"))
    pdb.gimp_selection_shrink(image, 2)
    pdb.gimp_edit_blend(white_patch_reflection_layer_bottom,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_2,         # Blend X,Y Startpoint
                        x_pos, foot_y_1)    # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)

    # Left Foot Reflection Layer
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Left Foot Glow"))
    left_foot_reflection_layer = gimp.Layer(image, "Left Foot Reflection",
                                            256, 256, RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(left_foot_reflection_layer, layer_pos)
    left_foot_reflection_layer.fill(TRANSPARENT_FILL)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Eye")
    width = y_2-y_1
    height = x_2-x_1
    x_pos = y_2-((y_2-y_1)/2)
    y_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_ellipse_select(image, x_1-41, y_1+152, width, height,
                            CHANNEL_OP_ADD, False, False, 1)
    pdb.gimp_selection_shrink(image, 5)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    x_pos = x_2-((x_2-x_1)/2)
    pdb.gimp_edit_blend(left_foot_reflection_layer,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_pos, y_1,         # Blend X,Y Startpoint
                        x_pos, y_2)         # Blend X,Y Endpoint
    pdb.gimp_selection_none(image)

    # Duplicate the Left Foot Reflection and flip it for the Right
    right_foot_reflection_layer = pdb.gimp_layer_copy(left_foot_reflection_layer, True)
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Right Foot Glow"))
    image.add_layer(right_foot_reflection_layer, layer_pos)
    pdb.gimp_item_set_name(right_foot_reflection_layer, "Right Foot Reflection")
    pdb.gimp_item_transform_flip(right_foot_reflection_layer,
                                 image.width/2, 0, image.width/2, image.height)

    # Left Wing Reflection Top
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Left Wing"))
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Wing")
    left_wing_reflection_layer_top = gimp.Layer(image, "Left Wing Reflection Top",
                                                256, 256, RGBA_IMAGE, 70, NORMAL_MODE)
    image.add_layer(left_wing_reflection_layer_top, layer_pos)
    left_wing_reflection_layer_top.fill(TRANSPARENT_FILL)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image,
                                                                "Left Wing"))
    pdb.gimp_selection_shrink(image, 2)
    pdb.gimp_edit_blend(left_wing_reflection_layer_top,
                        FG_TRANSPARENT_MODE,# Blend-Mode
                        NORMAL_MODE,        # Paint Mode
                        GRADIENT_LINEAR,    # Gradient Type
                        100,                # Opacity
                        0,                  # Offset
                        REPEAT_NONE,        # Repeat
                        False,              # Reverse
                        False,              # Supersampling
                        1,                  # Supersampling Max-Depth
                        0,                  # Supersampling Threshold
                        True,               # Dither
                        x_2-(x_2-x_1)/2,    # Blend X Startpoint
                        y_2-(y_2-y_1)/2,    # Blend Y Startpoint
                        x_2, y_2)           # Blend X,Y Endpoint
    pdb.gimp_selection_translate(image, 3, 3)
    pdb.gimp_edit_cut(left_wing_reflection_layer_top)
    pdb.gimp_selection_none(image)

    # Duplicate the Left Wing Reflection Top and flip it for the Right
    right_wing_reflection_layer_top = pdb.gimp_layer_copy(left_wing_reflection_layer_top, True)
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image,
                                                                                   "Right Wing"))
    image.add_layer(right_wing_reflection_layer_top, layer_pos)
    pdb.gimp_item_set_name(right_wing_reflection_layer_top, "Right Wing Reflection Top")
    pdb.gimp_item_transform_flip(right_wing_reflection_layer_top,
                                 image.width/2, 0, image.width/2, image.height)

    # Left Wing Reflection Bottom
    pdb.gimp_context_set_foreground((255, 255, 255))
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Left Wing"))
    left_wing_reflection_layer_bottom = gimp.Layer(image, "Left Wing Reflection Bottom",
                                                   256, 256, RGBA_IMAGE, 70, NORMAL_MODE)
    image.add_layer(left_wing_reflection_layer_bottom, layer_pos)
    left_wing_reflection_layer_bottom.fill(TRANSPARENT_FILL)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Wing"))
    pdb.gimp_selection_shrink(image, 1)
    pdb.gimp_edit_bucket_fill(left_wing_reflection_layer_bottom,
                              FG_BUCKET_FILL, NORMAL_MODE, 100, 255,
                              False, x_1+2, y_1+2)
    pdb.gimp_selection_shrink(image, 2)
    pdb.gimp_edit_cut(left_wing_reflection_layer_bottom)
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Right Eye")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Right Eye"))
    pdb.gimp_selection_translate(image, x_1-125, y_1+36)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(left_wing_reflection_layer_bottom)
    pdb.gimp_selection_none(image)

    # Duplicate the Left Wing Reflection Top and flip it for the Right
    right_wing_reflection_layer_bottom = pdb.gimp_layer_copy(left_wing_reflection_layer_bottom, True)
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Right Wing"))
    image.add_layer(right_wing_reflection_layer_bottom, layer_pos)
    pdb.gimp_item_set_name(right_wing_reflection_layer_bottom, "Right Wing Reflection Bottom")
    pdb.gimp_item_transform_flip(right_wing_reflection_layer_bottom,
                                 image.width/2, 0, image.width/2, image.height)

def add_shadows(image):
    '''Add Shadows to the image'''

    pdb.gimp_context_set_foreground((0, 0, 0))
    pdb.gimp_context_set_background((255, 255, 255))

    # Left Foot Body Shadow
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Left Foot"))
    x_1, y_1, x_2, y_2 = get_coords_by_name(image, "Left Foot")
    left_foot_body_shadow_layer = gimp.Layer(image, "Left Foot Body Shadow",
                                             256, 256, RGBA_IMAGE, 30, NORMAL_MODE)
    image.add_layer(left_foot_body_shadow_layer, layer_pos+1)
    left_foot_body_shadow_layer.fill(TRANSPARENT_FILL)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Foot"))
    pdb.gimp_selection_translate(image, 10, -1)
    pdb.gimp_edit_bucket_fill(left_foot_body_shadow_layer, FG_BUCKET_FILL, NORMAL_MODE,
                              100, 255, False, x_1+2, y_1+2)
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, left_foot_body_shadow_layer, 15.0, 15.0, 1)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Body"))
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(left_foot_body_shadow_layer)
    pdb.gimp_selection_none(image)

    # Duplicate the Left Foot Shadow for the Right Foot
    right_foot_body_shadow_layer = pdb.gimp_layer_copy(left_foot_body_shadow_layer, True)
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Right Foot"))
    image.add_layer(right_foot_body_shadow_layer, layer_pos+1)
    pdb.gimp_item_set_name(right_foot_body_shadow_layer, "Right Wing Reflection Bottom")
    pdb.gimp_item_transform_flip(right_foot_body_shadow_layer,
                                 image.width/2, 0, image.width/2, image.height)

    # Left On Foot Shadow
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Left Foot Reflection"))
    left_on_foot_shadow_layer = gimp.Layer(image, "On Left Foot Shadow",
                                           256, 256, RGBA_IMAGE, 20, NORMAL_MODE)
    image.add_layer(left_on_foot_shadow_layer, layer_pos)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Foot"))
    pdb.gimp_selection_grow(image, 5)
    fluf, x_1, y_1, x_2, y_2 = pdb.gimp_selection_bounds(image)
    pdb.gimp_edit_bucket_fill(left_on_foot_shadow_layer, FG_BUCKET_FILL, NORMAL_MODE,
                              100, 255, False, x_1+2, y_1+2)
    pdb.gimp_selection_translate(image, -20, 5)
    pdb.gimp_edit_cut(left_on_foot_shadow_layer)
    pdb.gimp_selection_none(image)
    pdb.plug_in_gauss(image, left_on_foot_shadow_layer, 15.0, 15.0, 1)
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Foot"))
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_cut(left_on_foot_shadow_layer)
    pdb.gimp_selection_none(image)

    # Duplicate the Left On Foot Shadow for the Right Foot
    right_on_foot_shadow_layer = pdb.gimp_layer_copy(left_on_foot_shadow_layer, True)
    layer_pos = pdb.gimp_image_get_layer_position(image,
                                                  pdb.gimp_image_get_layer_by_name(image, "Right Foot Reflection"))
    image.add_layer(right_on_foot_shadow_layer, layer_pos)
    pdb.gimp_item_set_name(right_on_foot_shadow_layer, "On Right Foot Shadow")
    pdb.gimp_item_transform_flip(right_on_foot_shadow_layer,
                                 image.width/2, 0, image.width/2, image.height)

    # Beak Drop Shadow
    pdb.script_fu_drop_shadow(image,
                              pdb.gimp_image_get_layer_by_name(image, "Beak"),
                              2, 8, 15, (0, 0, 0), 63, False)
    shadow_layer = pdb.gimp_image_get_layer_by_name(image, "Drop Shadow")
    pdb.gimp_item_set_name(shadow_layer, "Beak Drop Shadow")

    # Left Eye Drop Shadow
    pdb.script_fu_drop_shadow(image,
                              pdb.gimp_image_get_layer_by_name(image, "Left Eye"),
                              4, 4, 15, (0, 0, 0), 63, False)
    shadow_layer = pdb.gimp_image_get_layer_by_name(image, "Drop Shadow")
    pdb.gimp_item_set_name(shadow_layer, "Left Eye Drop Shadow")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Beak"))
    pdb.gimp_edit_cut(shadow_layer)
    pdb.gimp_selection_none(image)

    # Right Eye Drop Shadow
    pdb.script_fu_drop_shadow(image,
                              pdb.gimp_image_get_layer_by_name(image, "Right Eye"),
                              4, 4, 15, (0, 0, 0), 63, False)
    shadow_layer = pdb.gimp_image_get_layer_by_name(image, "Drop Shadow")
    pdb.gimp_item_set_name(shadow_layer, "Right Eye Drop Shadow")
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Beak"))
    pdb.gimp_edit_cut(shadow_layer)
    pdb.gimp_selection_none(image)

    # Tux Drop Shadow
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Body"))
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Left Foot"))
    pdb.gimp_image_select_item(image,
                               CHANNEL_OP_ADD,
                               pdb.gimp_image_get_layer_by_name(image, "Right Foot"))
    pdb.script_fu_drop_shadow(image,
                              pdb.gimp_image_get_layer_by_name(image, "Background"),
                              2, 8, 15, (0, 0, 0), 63, False)
    pdb.gimp_selection_none(image)

def draw_tux():
    '''Draw Tux'''

    # Save User's Settings
    pdb.gimp_context_push()

    # Create the image canvas set PPI to 72
    image = gimp.Image(256, 256, RGB)
    pdb.gimp_image_set_resolution(image, 72.0, 72.0)

    # Disable undo
    pdb.gimp_image_undo_disable(image)

    # Background Layer
    background_layer = gimp.Layer(image, "Background", 256, 256,
                                  RGBA_IMAGE, 100, NORMAL_MODE)
    image.add_layer(background_layer, -1)
    background_layer.fill(TRANSPARENT_FILL)

    # Draw the main body parts
    draw_body(image)
    draw_tummy(image)
    draw_left_wing(image)
    draw_right_wing(image)
    draw_left_foot(image)
    draw_right_foot(image)
    draw_left_eyelid(image)
    draw_right_eyelid(image)
    draw_left_eye(image)
    draw_right_eye(image)
    draw_left_pupil(image)
    draw_right_pupil(image)
    draw_beak(image)
    add_body_reflections(image)
    add_shadows(image)

    # change to the background layer before finishing.
    active_layer = pdb.gimp_image_get_layer_by_name(image, "Background")
    pdb.gimp_image_set_active_layer(image, active_layer)

    # Re-Enable The Undo option
    pdb.gimp_image_undo_enable(image)

    # Restore the User's Settings
    pdb.gimp_context_pop()

    # Display the image
    gimp.Display(image)
    gimp.displays_flush()

register(
        "python_fu_G2_Tux",          # Name
        "Create Crystal Tux G2",     # Blurb
        "Create Crystal Tux G2",     # Help
        "Mike Watters",              # Author
        "Mile Watters",              # Copyright
        "2018",                      # Date
        "Crystal Tux G2",            # Menu Name
        "",                          # Image Types "" for new
        [],                          # User Inputs
        [],                          # Resuts
        draw_tux,                    # Function
        menu="<Image>/File/Create")  # Menu Location

main()
