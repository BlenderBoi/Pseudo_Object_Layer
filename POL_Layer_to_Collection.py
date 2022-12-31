import bpy
from . utility_function import*

ENUM_Mode = [("MOVE", "Move", "Move"), ("ADD", "Add", "Add")]

class POL_OT_Layer_To_Collection(bpy.types.Operator):

    bl_idname = "pol.layer_to_collection"
    bl_label = "Move Layer to Collection"
    bl_description = "Convert Layer to Collection"
    bl_options = {"REGISTER", "UNDO"}

    index: bpy.props.IntProperty()
    Mode: bpy.props.EnumProperty(items=ENUM_Mode)
    Collection_Name: bpy.props.StringProperty()

    def invoke(self, context, event):

        scn = context.scene
        Session = scn.POL_Layer_Session[scn.POL_Layer_Session_Index]
        Layers = Session.Layers
        Layer = Layers[self.index]

        self.Collection_Name = Layer.Name

        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "Collection_Name", text="Name")
        layout.prop(self, "Mode", text="Mode")

    def execute(self, context):


        scn = context.scene
        Session = scn.POL_Layer_Session[scn.POL_Layer_Session_Index]
        Layers = Session.Layers
        Layer = Layers[self.index]

        collection = bpy.data.collections.new(self.Collection_Name)
        context.scene.collection.children.link(collection)



        for object in Layer.Objects:

            if self.Mode == "MOVE":
                for coll in object.Object.users_collection:
                    coll.objects.unlink(object.Object)

            if not collection.children.data.objects.get(object.Object.name):
                collection.children.data.objects.link(object.Object)

        # newItem = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers.add()
        # newItem.Name = self.Name
        # scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index = len(scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers)-1

        update_UI()

        return {'FINISHED'}


classes = [
        POL_OT_Layer_To_Collection,
        ]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
