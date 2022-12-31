import bpy

State = [("HIDE","Hide","Hide"),("SHOW","Show","Show")]
# key_mode = [("KEY","Key","Key"),("CLEAR","Clear","Clear")]

class POL_OT_Key_Visibility(bpy.types.Operator):

    bl_idname = "pol.key_visibility"
    bl_label = "Key Visibility"
    bl_description = "Key Visibility"

    # key_mode: bpy.props.EnumProperty(default="KEY")
    index: bpy.props.IntProperty()
    GroupChannel: bpy.props.BoolProperty(default=False)
    State: bpy.props.EnumProperty(items=State)
    GroupName: bpy.props.StringProperty(default="Visibility Group")

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        # layout.prop(self, "key_mode")
        # if self.key_mode == "KEY":
        layout.prop(self, "GroupChannel", text="Group Channel")
        if self.GroupChannel:
            layout.prop(self, "GroupName", text="Group name")
        layout.prop(self, "State", expand=True)


    def execute(self, context):

        scn = context.scene

        Session = scn.POL_Layer_Session[scn.POL_Layer_Session_Index]
        Layers = Session.Layers

        # if self.key_mode == "KEY":

        if self.State == "HIDE":
            mode = True
        if self.State == "SHOW":
            mode = False


        if len(Layers) > 0:
            Active_Layer = Layers[self.index]
            for object in Active_Layer.Objects:

                object.Object.hide_render = mode
                object.Object.hide_viewport = mode

                object.Object.keyframe_insert("hide_render", frame=scn.frame_current)
                object.Object.keyframe_insert("hide_viewport", frame=scn.frame_current)

                if object.Object.animation_data:
                    if object.Object.animation_data.action:

                        if not object.Object.animation_data.action.groups.get(self.GroupName):
                            Action_Group = object.Object.animation_data.action.groups.new(self.GroupName)
                        else:
                            Action_Group = object.Object.animation_data.action.groups.get(self.GroupName)

                        for fc in object.Object.animation_data.action.fcurves:
                            if fc.data_path == "hide_viewport":
                                fc.group = Action_Group
                            if fc.data_path == "hide_render":
                                fc.group = Action_Group


        # if self.key_mode == "CLEAR":
        #     pass



        #
        # update_UI()

        return {'FINISHED'}





classes = [
        POL_OT_Key_Visibility,
        ]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
