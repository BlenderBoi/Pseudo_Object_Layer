import bpy

class POL_MT_Layers_Extra_Menu(bpy.types.Menu):
    bl_label = "Pseudo Object Layer Extras Menu"
    bl_idname = "POL_MT_object_layers_extra"

    def draw(self, context):

        layout = self.layout
        scn = context.scene

        row = layout.row()
        row.operator("pol.key_visibility",text="Key Visibility", icon="KEYTYPE_MOVING_HOLD_VEC").index = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index
        layout.operator("pol.export_layers_to_fbx", icon ="EXPORT")


class POL_MT_Icon_Expose_Menu(bpy.types.Menu):
    bl_label = "Pseudo Object Layer Icon Expose Menu"
    bl_idname = "POL_MT_object_layers_icon_expose"

    def draw(self, context):


        scn = context.scene
        obj = context.object
        layout = self.layout


        options = [
            ("Solo", "Solo", "RADIOBUT_ON"),
            ("layer_to_collection", "Collection From Layer", "COLLECTION_NEW"),
            ("Select", "Select", "RESTRICT_SELECT_OFF"),
            ("Search", "Search", "VIEWZOOM"),
            ("Modifier", "Modifier", "MODIFIER"),
            ("Display_As", "Display As", "MOD_WIREFRAME"),
            ("Visibility", "Hide Viewport", "HIDE_OFF"),
            ("Render", "Hide Render", "RESTRICT_RENDER_OFF"),
            ("key_Visibility", "Key Visibility", "KEYTYPE_MOVING_HOLD_VEC"),
            ("Export", "Export", "EXPORT"),
            ("Lock", "Lock Selection", "LOCKED"),
            ("Particle", "Particle", "PARTICLE_DATA"),
            ("Trash", "Remove", "TRASH"),
        ]







        for option in options:
            
            if option[2]:

                row = layout.row(align=True)
                row.label(text="", icon=option[2])
                row.prop(scn.POL_List_Icon, option[0], text=option[1], icon=option[2])
                row.separator()
            else:
                row = layout.row(align=True)
                row.label(text="", icon="DOT")
                row.prop(preferences, option[0], text=option[1])
                row.separator()









classes = [POL_MT_Layers_Extra_Menu, POL_MT_Icon_Expose_Menu]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
