

bl_info = {
    "name": "Pseudo Object Layer",
    "author": "BlenderBoi",
    "version": (1, 5, 1),
    "blender": (3, 1, 0),
    "description": "Help in grouping objects",
    "warning": "",
    "wiki_url": "",
    "category": "Utility",
}


#Global Solo (Checkbox)
#Grouped Utility Operator

import bpy
from . import POL_UI_Panel
from . import POL_Data
from . import POL_Operator
from . import POL_Key_Visibility
from . import POL_Export_FBX_Layers
# from . import POL_Generate_Visibility_Driver
from . import POL_Layer_to_Collection
from . import POL_Batch_Layers_to_Collections
from . import Extras_Menu

files = [Extras_Menu, POL_Batch_Layers_to_Collections, POL_UI_Panel, POL_Data, POL_Operator, POL_Key_Visibility, POL_Export_FBX_Layers, POL_Layer_to_Collection]


#Save Objeects Location, Rotation, Scale



def register():

    for file in files:
        file.register()



def unregister():

    for file in files:
        file.unregister()

if __name__ == "__main__":
    register()
