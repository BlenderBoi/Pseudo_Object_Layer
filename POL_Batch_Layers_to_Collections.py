import bpy
from . utility_function import*

ENUM_Mode = [("MOVE", "Move", "Move"), ("ADD", "Add", "Add")]

class POL_OT_Batch_Layers_To_Collections(bpy.types.Operator):

    bl_idname = "pol.batch_layers_to_collections"
    bl_label = "Batch Move Layers to Collections"
    bl_description = "Batch Move Layers to Collections"
    bl_options = {"REGISTER", "UNDO"}


    Mode: bpy.props.EnumProperty(items=ENUM_Mode)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "Mode", text="Mode")

    def execute(self, context):

        scn = context.scene
        Session = scn.POL_Layer_Session[scn.POL_Layer_Session_Index]
        Layers = Session.Layers
        # Layer = Layers[self.index]

        for Layer in Layers:

            collection = bpy.data.collections.new(Layer.Name)
            context.scene.collection.children.link(collection)

            for object in Layer.Objects:

                if self.Mode == "MOVE":
                    for coll in object.Object.users_collection:
                        coll.objects.unlink(object.Object)

                if not collection.children.data.objects.get(object.Object.name):
                    collection.children.data.objects.link(object.Object)


        update_UI()

        return {'FINISHED'}


classes = [
        POL_OT_Batch_Layers_To_Collections,
        ]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
