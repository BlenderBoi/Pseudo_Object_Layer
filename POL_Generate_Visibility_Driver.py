import bpy
from . import utility_function




ENUM_Driver_Source = [("SCENE","Scene","Scene"),("OBJECT","Object","Object")]

class POL_OT_Generate_Visibility_Driver(bpy.types.Operator):

    bl_idname = "pol.generate_visibility_driver"
    bl_label = "Generate Visibility Driver"
    bl_description = "Generate Visibility Driver"
    bl_options = {"REGISTER", "UNDO"}

    index: bpy.props.IntProperty()

    Driver_Source: bpy.props.EnumProperty(items=ENUM_Driver_Source,default="SCENE")
    Driver_Object: bpy.props.StringProperty()
    Driver_Name: bpy.props.StringProperty()


    def invoke(self, context, event):

        scn = context.scene
        Session = scn.POL_Layer_Session[scn.POL_Layer_Session_Index]
        Layers = Session.Layers

        if len(Layers) > 0:
            Active_Layer = Layers[self.index]
            self.Driver_Name = Active_Layer.Name + "_Visibility"

        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        # layout.prop(self, "Driver_Source", text="Driver Type")
        layout.prop(self, "Driver_Name", text="Driver Name")

        if self.Driver_Source == "OBJECT":
            layout.prop_search(self, "Driver_Object", context.view_layer, "objects", text="Driver")

    def execute(self, context):

        scn = context.scene

        Session = scn.POL_Layer_Session[scn.POL_Layer_Session_Index]
        Layers = Session.Layers

        if self.Driver_Source == "SCENE":

            rna_ui = scn.get('_RNA_UI')
            if rna_ui is None:
                scn['_RNA_UI'] = {}
                rna_ui = scn['_RNA_UI']

            scn[self.Driver_Name] = True
            rna_ui[self.Driver_Name] = {"min": 0, "max": 1, "soft_min": 0, "soft_max":1}


        if self.Driver_Source == "OBJECT":
            if context.view_layer.objects.get(self.Driver_Object):
                obj = context.view_layer.objects.get(self.Driver_Object)

                rna_ui = obj.get('_RNA_UI')
                if rna_ui is None:
                    obj['_RNA_UI'] = {}
                    rna_ui = obj['_RNA_UI']

                obj[self.Driver_Name] = True
                rna_ui[self.Driver_Name] = {"min": 0, "max": 1, "soft_min": 0, "soft_max":1}


            else:
                return {'FINISHED'}



        if len(Layers) > 0:
            Active_Layer = Layers[self.index]
            for object in Active_Layer.Objects:

                d = object.Object.driver_add("hide_viewport").driver
                v = d.variables.new()

                if self.Driver_Source == "SCENE":

                    path = '["' + self.Driver_Name + '"]'

                    v.name = "Visibility_Driver"
                    v.targets[0].id_type = "SCENE"
                    v.targets[0].id = scn
                    v.targets[0].data_path = path
                    d.expression = v.name


                if self.Driver_Source == "OBJECT":

                    path = '["' + self.Driver_Name + '"]'
                    d.type = "SCRIPTED"
                    v.name = "Visibility_Driver"
                    v.targets[0].id = obj
                    v.targets[0].data_path = path
                    d.expression = v.name



            # utility_function.update_UI()


        return {'FINISHED'}





classes = [
        POL_OT_Generate_Visibility_Driver,
        ]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
