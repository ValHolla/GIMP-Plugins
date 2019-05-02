#!/usr/bin/env python
# vim: expandtab:ts=4:sw=4

''' Plugin to Generate an image with a Grid
    User defined size of image, and user defined size of Grid
'''

from gimpfu import *

def generate_graph_paper(width, height, grid_size):
    ''' Generate a new Image containing the Graph Paper
        with the user supplied parameters, and display the new image

    Parameters:
        width:     The width of the canvas in px
        height:    The height of the canvas in px
        grid_size: Spacing for the grid lines in px
    '''
    ## Init the progress bar:
    gimp.progress_init("Generating Grid Lines")

    ## Save the User's Settings, so we can restore them when we are done
    pdb.gimp_context_push()

    ## Create the Image, Set the Resolution to 72ppi
    img = gimp.Image(width, height, RGB)
    pdb.gimp_image_set_resolution(img, 72.0, 72.0)

    ## We are creating a new image: Disable UNDO
    pdb.gimp_image_undo_disable(img)

    ## Create the Drawable Layer and Add to the Image
    background = gimp.Layer(img, "Grid", width, height,
                            RGB_IMAGE, 100, NORMAL_MODE)
    background.fill(WHITE_FILL)
    img.add_layer(background, -1)

    ## Configure the Brush for Grid Lines, Brush Name, Size and Color
    pdb.gimp_context_set_brush("1. Pixel")
    pdb.gimp_context_set_brush_size(1.0)
    pdb.gimp_context_set_foreground((0, 0, 0))

    ## Number of Horizontal and Vertical lines
    vlines = round(width/grid_size)
    hlines = round(height/grid_size)

    ## Init Progress
    progress = 1

    ## Add Virtical Lines
    i = 0
    ## We want the Grids to be centered on the Canvas
    vpoint = round((width-(grid_size*vlines))/2)

    while i <= vlines:
        ## Do not draw line if along the edge of Canvas
        if (vpoint > 0) & (vpoint < width):
            pdb.gimp_pencil(background, 4, [vpoint, 0, vpoint, height])
            gimp.progress_update(progress/(vlines+hlines))
        i += 1
        progress += 1
        vpoint += grid_size

    ## Add Horizontal Lines
    i = 0
    ## We want the Grids to be centered on the Canvas
    hpoint = round((height-(grid_size*hlines))/2)
    while i <= hlines:
        ## Do not draw line if along the edge of Canvas
        if (hpoint > 0) & (hpoint < height):
            pdb.gimp_pencil(background, 4, [0, hpoint, width, hpoint])
            gimp.progress_update(progress/(vlines+hlines))
        i += 1
        progress += 1
        hpoint += grid_size

    ## ReEnable UNDO
    pdb.gimp_image_undo_enable(img)

    ## Restore the User's Settings
    pdb.gimp_context_pop()

    ## Show New Image
    gimp.Display(img)
    gimp.displays_flush()

register(
        "python_fu_generate_graph_paper",
        "Graph Paper Generator",
        "Generate Graph Paper",
        "Mike Watters",
        "Mike Watters",
        "2018",
        "Graph Paper...",
        " ",
        [
            (PF_INT, "number", "Width (px)", 612), ## default 8.5"
            (PF_INT, "number", "Height (px)", 792), ## default 11"
            (PF_INT, "number", "Size of Grid (px)", 72) ## default 1" square
        ],
        [],
        generate_graph_paper, menu="<Image>/File/Create")

main()
