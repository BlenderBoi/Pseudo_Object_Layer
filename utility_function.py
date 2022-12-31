import bpy


def update_UI():

    for screen in bpy.data.screens:
        for area in screen.areas:
            area.tag_redraw()


def draw_subpanel(layout, label, source, property):

    state = getattr(source, property)
    
    if state:
        icon = "TRIA_DOWN"    
    else:
        icon = "TRIA_RIGHT"

    row = layout.row(align=True)
    row.alignment = "LEFT"
    row.prop(source, property, text=label, icon=icon, emboss=False)

    return state 

