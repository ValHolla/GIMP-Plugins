#!/usr/bin/env python
# vim: expandtab:ts=4:sw=4

''' billiard_ball.py
    Mike Watters
    2018(c) Mike Watters
    <valholla75_at_gmail_dot_com>

    This script requests the number of a billiard ball, size (px)
    and Font for the number.  Then Generates a billiard ball
    with basic lightting, shadows and reflections.
    '''

from gimpfu import *

def generate_ball(size, ball, font):
    '''Generate the Ball'''
    # Double the size for the width
    size_x = size*2

    # Initialize the Progress Bar
    if ball < 1:
        initstr = "Generating Cue Ball..."
    else:
        initstr = "Generating Ball "+str(ball)+"..."
    gimp.progress_init(initstr)

    # Save User's Settings
    pdb.gimp_context_push()

    # Create new image, set resolution to 72ppi
    ballimg = gimp.Image(size_x, size, RGB)
    pdb.gimp_image_set_resolution(ballimg, 72.0, 72.0)

    # Disable undo
    pdb.gimp_image_undo_disable(ballimg)

    # Generate Solid or Stripe Layer
    layer0 = gimp.Layer(ballimg, "Billard Ball", size_x, size,
                        RGBA_IMAGE, 100, NORMAL_MODE)

    # List of colors for the balls
    color_list = [
        (255, 255, 255), (255, 255, 0), (0, 0, 255),
        (255, 0, 0), (160, 40, 170), (243, 153, 10),
        (40, 150, 30), (150, 50, 50), (0, 0, 0),
        (255, 255, 0), (0, 0, 255), (255, 0, 0),
        (160, 40, 170), (243, 153, 10), (40, 150, 30),
        (150, 50, 50)
    ]

    # Set the foreground color to the color of the ball in the color_list
    pdb.gimp_context_set_foreground(color_list[ball])

    # Set the background to White
    pdb.gimp_context_set_background((255, 255, 255))

    # Fill layer with White
    layer0.fill(WHITE_FILL)

    # Add the layer to the image
    ballimg.add_layer(layer0, -1)

    # Check to see if the ball selected is a solid or stripe,
    # and fill the Layer correctly.
    if ball < 9:
        # Solid Layer
        pdb.gimp_edit_fill(layer0, FOREGROUND_FILL)
    else:
        # Using Rect Select, Stripe will be the center 1/3 of the layer
        pdb.gimp_rect_select(ballimg,
                             0,                  # upper left x coordinate
                             (round(size/3)),    # upper left y coordinate
                             size_x,             # width
                             (round(size/3)),    # height
                             CHANNEL_OP_ADD,     # Mode
                             False,              # feather
                             0)                  # feather radius
        # Fill the Selection
        pdb.gimp_edit_fill(layer0, FOREGROUND_FILL)
        # Unselect the Stripe
        pdb.gimp_selection_none(ballimg)

    # If Cue Ball do not need Number Circle or Number
    if ball > 0:
        # Number Circle Layer
        layer1 = gimp.Layer(ballimg, "Circle Layer", size_x, size,
                            RGBA_IMAGE, 100, NORMAL_MODE)

        # Add the layer to the image
        ballimg.add_layer(layer1, -1)

        # Add an alpha Channel
        pdb.gimp_layer_add_alpha(layer1)

        # Fill with Transparency
        pdb.gimp_drawable_fill(layer1, TRANSPARENT_FILL)

        # create the white circle for the Number,
        # the size will be 1/5th the requested size of the ball
        # The exact position will be centered later
        pdb.gimp_ellipse_select(ballimg,
                                round(size_x/2),  # upper left x coordinate
                                round(size/2),    # upper left y coordinate
                                size/5,           # width of ellipse
                                size/5,           # height of ellipse
                                CHANNEL_OP_ADD,   # Mode
                                True,             # antialias
                                False,            # feather
                                0)                # festher radius

        # Fill the elipse Selection with White
        pdb.gimp_edit_fill(layer1, WHITE_FILL)

        # Crop and Center the layer
        pdb.plug_in_autocrop_layer(ballimg, layer1)
        layer1.set_offsets(int(size_x/2-layer1.width/2),
                           int(size/2-layer1.height/2))

        # Ball Number
        # Set Foreground to Black for Ball Number
        pdb.gimp_palette_set_foreground((0, 0, 0))

        # Create Number Text layer
        # Exact Position will be centered later
        number_layer = pdb.gimp_text_fontname(ballimg, None,
                                              round(size_x/2),  # upper left x corrdinate
                                              round(size/2),    # upper left y coordinate
                                              ball,             # text
                                              0,                # border
                                              True,             # antialias
                                              size/8,           # text size
                                              PIXELS,           # size units
                                              font)             # font name

        # Center the Number layer
        number_layer.set_offsets(int(size_x/2-number_layer.width/2),
                                 int(size/2-number_layer.height/2))

    # Merge all visible layers
    layer3 = pdb.gimp_image_merge_visible_layers(ballimg, EXPAND_AS_NECESSARY)

    # Map to Sphere
    pdb.plug_in_map_object(ballimg, layer3,
                           1,                   # mapping 1=sphere
                           0.5, 0.5, 2.0,       # viewpoint x,y,z
                           0.5, 0.5, 0.9,       # object pos x,y,z
                           1.0, 0.0, 0.0,       # first axis x,y,z
                           0.0, 1.0, 0.0,       # second axis x,y,z
                           0.0, -10.0, -5.0,    # axis rotation x,y,z
                           0,                   # light type 0=point
                           (255, 255, 255),     # light color (r,g,b)
                           -0.5, -0.5, 2.0,     # light position x,y,z
                           1.0, 1.0, 1.0,       # light direction x,y,z
                           0.4,                 # ambient-intensity
                           0.6,                 # diffuse-intenstity
                           0.5,                 # diffuse-reflectivity
                           0.5,                 # specular-reflectifity
                           27.0,                # highlight
                           True,                # antialias
                           False,               # tiled
                           False,               # new image
                           True,                # transparent background
                           0.250,               # radius
                           1.0,                 # x-scale
                           1.0,                 # y-scale
                           1.0,                 # z-scale
                           0,                   # unused for sphere
                           layer3,              # unused for sphere
                           layer3,              # unused for sphere
                           layer3,              # unused for sphere
                           layer3,              # unused for sphere
                           layer3,              # unused for sphere
                           layer3,              # unused for sphere
                           layer3,              # unused for sphere
                           layer3)              # unused for sphere

    # Scale the sphere to selected Size
    pdb.gimp_image_scale(ballimg, size, size)

    # Re-Enable The Undo option
    pdb.gimp_image_undo_enable(ballimg)

    # Restore the User's Settings
    pdb.gimp_context_pop()

    # Display the image
    gimp.Display(ballimg)
    gimp.displays_flush()

register(
        "python_fu_billiard_ball",   # Name
        "Create Billiard Ball",      # Blurb
        "Create Billiard Ball",      # Help
        "Mike Watters",              # Author
        "Mile Watters",              # Copyright
        "2018",                      # Date
        "Create Billiard Ball...",   # Menu Name
        "",                          # Image Types "" for new
        [
            (PF_INT, "size", "Size(px)", 256),
            (PF_OPTION, "ball", "Ball Number", 0,
             ("cue", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)),
            (PF_FONT, "font", "Number Font", "Comic Sans MS")
        ],                           # User Inputs
        [],                          # Resuts
        generate_ball,               # Function
        menu="<Image>/File/Create")  # Menu Location

main()
