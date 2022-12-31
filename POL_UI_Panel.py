import bpy
from . import POL_Operator
from bpy.app.handlers import persistent
from . import utility_function


def Show_Session_List(self, context, layout):


    scn = context.scene

    layout = layout.box()

    if utility_function.draw_subpanel(layout, "Category", scn, "POL_Session_Show"):
    

        row = layout.row()
        row.template_list("POL_UL_Layer_Session_List", "", scn, "POL_Layer_Session", scn, "POL_Layer_Session_Index")

        col = row.column(align=True)


        col.operator("pol.add_layer_session", text="", icon="ADD")
        col.operator("pol.remove_layer_session", text="", icon="REMOVE").index = scn.POL_Layer_Session_Index
        col.separator()
        col.operator("pol.reorder_layer_session", text="", icon="TRIA_UP").mode="UP"
        col.operator("pol.reorder_layer_session", text="", icon="TRIA_DOWN").mode="DOWN"






class POL_UI_Panel(bpy.types.Panel):
    """Pseudo Object Layer"""
    bl_label = "Pseudo Object Layer"
    bl_idname = "POL_PT_Main_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Pseudo Object Layer"


    def draw(self, context):

        layout = self.layout
        scn = context.scene

        row = layout.row()

        col = row.column(align=True)

        if len(scn.POL_Layer_Session)==0:
            col.operator("pol.add_layer_session", text="New Session", icon="ADD")


        if len(scn.POL_Layer_Session) > 0:

            col = row.column(align=True)

            col.prop(scn, "POL_Session_Dropdown", text="")

            col.template_list("POL_UL_Layer_List", "", scn.POL_Layer_Session[scn.POL_Layer_Session_Index], "Layers", scn.POL_Layer_Session[scn.POL_Layer_Session_Index], "Layers_Index")

            col = row.column(align=True)
            col.operator("pol.layer_from_selected", text="", icon="ADD")
            col.operator("pol.remove_pseudo_layer", text="", icon="REMOVE")
            col.separator()
            col.menu("POL_MT_object_layers_icon_expose", text="", icon="VIS_SEL_11")
            col.menu("POL_MT_object_layers_extra", text="", icon="DOWNARROW_HLT")

            col.separator()


            col.operator("pol.reorder_layer", text="", icon="TRIA_UP").mode= "UP"
            col.operator("pol.reorder_layer", text="", icon="TRIA_DOWN").mode="DOWN"

            row = layout.row()

            row.operator("pol.layer_from_selected", text="New From Selected", icon="PLUS")



            row = layout.row(align=True)

            if len(scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers) > 0:





                row.operator("pol.add_selected_to_layer", text="Assign", icon="ADD").index = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index
                row.operator("pol.remove_selected_layer_object", text="Unassign", icon="REMOVE")
                layout.separator()
                layout.operator("pol.batch_layers_to_collections", text="Batch Layers to Collection", icon="COLLECTION_NEW")

                layout.separator()


                # row.operator("pol.generate_visibility_driver",text="Generate Visibility Driver", icon="DRIVER").index = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index

                row = layout.row()
                # row.operator("pol.parent_parentless_to_empty", text="Parent Layer Orphan Objects to Empty", icon="CON_CHILDOF")

                Layers = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers
                Layer_Index = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index




                ActiveLayer = Layers[Layer_Index]

                if len(ActiveLayer.Objects) > 0:

                    box = layout.box()

                    if utility_function.draw_subpanel(box, "Layer Object List", scn, "POL_Show_Object_List"):

                        box.template_list("POL_UL_Object_List", "", ActiveLayer, "Objects", ActiveLayer, "Object_Index")
                        box.operator("pol.purge_missing_objects", text="Purge Missing Objects")


        Show_Session_List(self, context, layout)

@ persistent
def load_Setting(scene):
    if len(bpy.context.scene.POL_Layer_Session) == 0:
        bpy.ops.pol.add_layer_session()



classes = [
        POL_UI_Panel,
        ]


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.app.handlers.load_post.append(load_Setting)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.app.handlers.load_post.remove(load_Setting)

if __name__ == "__main__":
    register()
