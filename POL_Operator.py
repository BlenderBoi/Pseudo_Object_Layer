import bpy
import numpy
from . import utility_function


class POL_OT_Add_Pseudo_Layer(bpy.types.Operator):

    bl_idname = "pol.add_pseudo_layer"
    bl_label = "Add Pseudo Layer"
    bl_description = "Add Pseudo Layer"
    bl_options = {"REGISTER", "UNDO"}

    Name: bpy.props.StringProperty(default="Layer")

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)


    def execute(self, context):

        scn = context.scene

        newItem = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers.add()
        newItem.Name = self.Name
        scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index = len(scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers)-1

        utility_function.update_UI()

        return {'FINISHED'}



class POL_OT_Add_Layer_Object(bpy.types.Operator):

    bl_idname = "pol.add_layer_object"
    bl_label = "Add Layer Object"
    bl_description = "Add Layer Object"
    bl_options = {"REGISTER", "UNDO"}

    index: bpy.props.IntProperty()


    def execute(self, context):

        scn = context.scene

        layers = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers
        data = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers[self.index]

        newItem = data.Objects.add()
        data.Object_Index = len(data.Objects)-1

        utility_function.update_UI()

        return {'FINISHED'}



class POL_OT_Add_Selected_to_Layer(bpy.types.Operator):

    bl_idname = "pol.add_selected_to_layer"
    bl_label = "Add Selected Object"
    bl_description = "Add Selected Object to Layer"

    bl_options = {"REGISTER", "UNDO"}

    index: bpy.props.IntProperty()


    def execute(self, context):

        scn = context.scene
        layers = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers
        data = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers[self.index]



        object_check = [object.Object for object in data.Objects]

        for object in context.selected_objects:

            if not object in object_check:
                newItem = data.Objects.add()
                newItem.Object = object

                object.hide_viewport = not(data.Visibility_State)
                object.hide_select = data.Selectable_State
                object.display_type=  data.Display_As_State


                # if object == context.object:
                #     data.Object_Index = newItem.index


                # data.Object_Index = len(data.Objects)-1

                utility_function.update_UI()



        return {'FINISHED'}



class POL_OT_New_Layer_From_Selected(bpy.types.Operator):

    bl_idname = "pol.layer_from_selected"
    bl_label = "New Layer From Selected"
    bl_description = "New Layer from selected objects"
    bl_options = {"REGISTER", "UNDO"}

    Name: bpy.props.StringProperty(default="Layer")

    def invoke(self, context, event):

        scn = context.scene
        self.Name = "Layer" + str(len(scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers))

        return context.window_manager.invoke_props_dialog(self)



    def execute(self, context):


        scn = context.scene

        newItem = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers.add()
        newItem.Name = self.Name
        scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index = len(scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers)-1

        utility_function.update_UI()

        layers = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers
        data = newItem


        if context.active_object:
            if context.active_object.select_get():
                ActiveObject = data.Objects.add()
                ActiveObject.Object = context.active_object
                data.Object_Index = len(data.Objects)-1




        object_check = [object.Object for object in data.Objects]

        for object in context.selected_objects:


            if not object in object_check:
                newObject = data.Objects.add()
                newObject.Object = object

                # object.hide_viewport = not(data.Visibility_State)
                # object.hide_select = data.Selectable_State
                # object.display_type=  data.Display_As_State


                # data.Object_Index = len(data.Objects)-1
                # if object == context.object:
                #     data.Object_Index = newItem.index
        if context.active_object:
            if not context.active_object.select_get():
                data.Object_Index = len(data.Objects)-1


        utility_function.update_UI()

        return {'FINISHED'}







class POL_OT_Remove_Pseudo_Layer(bpy.types.Operator):

    bl_idname = "pol.remove_pseudo_layer"
    bl_label = "Remove Pseudo Layer"
    bl_description = "Remove Layer"
    bl_options = {"REGISTER", "UNDO"}

    index : bpy.props.IntProperty()

    def invoke(self, context, event):

        scn = context.scene

        scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers.remove(self.index)

        if len(scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers) > 0:
            if scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index == 0:
                scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index = 0
            if scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index > 0:
                scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index -= 1

        utility_function.update_UI()


        return {'FINISHED'}



class POL_OT_Remove_Layer_Object(bpy.types.Operator):

    bl_idname = "pol.remove_layer_object"
    bl_label = "Remove Layer Object"
    bl_description = "Remove Layer Object"
    bl_options = {"REGISTER", "UNDO"}

    object_index : bpy.props.IntProperty()
    layer_index : bpy.props.IntProperty()


    def invoke(self, context, event):

        scn = context.scene

        Layer = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers[self.layer_index]
        Layer.Objects.remove(self.object_index)

        if len(Layer.Objects) > 0:
            if Layer.Object_Index == 0:
                Layer.Object_Index = 0
            if Layer.Object_Index > 0:
                Layer.Object_Index -= 1

        utility_function.update_UI()


        return {'FINISHED'}



class POL_OT_Select_Layer_Object(bpy.types.Operator):

    bl_idname = "pol.select_layer_object"
    bl_label = "Select Layer Object"
    bl_description = "Select Layer Object (Hold Shift to Deselect All Before Selecting)"
    bl_options = {"REGISTER", "UNDO"}

    index : bpy.props.IntProperty()



            

    def invoke(self, context, event):


        if event.shift:
            for object in context.selected_objects:
                object.select_set(False)

        scn = context.scene

        Layer = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers[self.index]

        Objects = [object.Object for object in Layer.Objects if context.view_layer.objects.get(object.Object.name)]

        State_Check = [object.select_get() for object in Objects if object]
        Toogle_Check = not(any(State_Check))


        if len(Objects)>0:
            for object in Objects:
                object.select_set(Toogle_Check)

            ActiveObject = Layer.Objects[Layer.Object_Index].Object

            if context.view_layer.objects.get(ActiveObject.name):

                context.view_layer.objects.active = ActiveObject

        utility_function.update_UI()


        return {'FINISHED'}



def View_Object(context, Object):
    SaveSelected = context.selected_objects
    SaveActive = context.active_object

    bpy.ops.object.select_all(action='DESELECT')


    state = Object.hide_select


    Object.hide_select = False
    Object.select_set(True)
    context.view_layer.objects.active = Object

    bpy.ops.view3d.view_selected(use_all_regions=False)

    bpy.ops.object.select_all(action='DESELECT')

    for selected in SaveSelected:
        selected.select_set(True)

    Object.hide_select = state


    context.view_layer.objects.active = SaveActive


def View_Objects(context, Objects):
    SaveSelected = context.selected_objects


    SaveActive = context.active_object

    state_hide_select = []


    bpy.ops.object.select_all(action='DESELECT')

    for Object in Objects:
        if Object.hide_select:
            state_hide_select.append(Object)
            Object.hide_select = False

        Object.select_set(True)

    if len(Objects) > 0:
        context.view_layer.objects.active = Objects[0]


    bpy.ops.view3d.view_selected(use_all_regions=False)

    for Object in state_hide_select:
        Object.hide_select = True

    bpy.ops.object.select_all(action='DESELECT')

    for selected in SaveSelected:
        selected.select_set(True)



    context.view_layer.objects.active = SaveActive










class POL_OT_Frame_Layer_Object(bpy.types.Operator):

    bl_idname = "pol.frame_layer_object"
    bl_label = "Frame Layer Object"
    bl_description = "Frame Layer Object"
    bl_options = {"REGISTER", "UNDO"}

    layer_index : bpy.props.IntProperty()
    object_index : bpy.props.IntProperty()

    def invoke(self, context, event):

        scn = context.scene

        Layer = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers[self.layer_index]
        Object = Layer.Objects[self.object_index].Object
        View_Object(context, Object)


        utility_function.update_UI()


        return {'FINISHED'}



class POL_OT_Frame_Layer_Objects(bpy.types.Operator):

    bl_idname = "pol.frame_layer_objects"
    bl_label = "Frame Layer Objects"
    bl_description = "Frame Layer Objects"
    bl_options = {"REGISTER", "UNDO"}

    layer_index : bpy.props.IntProperty()

    def invoke(self, context, event):

        scn = context.scene

        Layer = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers[self.layer_index]

        Objects = []

        if len(Layer.Objects)>0:
            for Object in Layer.Objects:
                Objects.append(Object.Object)


            View_Objects(context, Objects)


        utility_function.update_UI()


        return {'FINISHED'}




class POL_OT_Purge_Missing_Objects(bpy.types.Operator):

    bl_idname = "pol.purge_missing_objects"
    bl_label = "Purge Missing Objects"
    bl_description = "Purge Missing Objects"
    bl_options = {"REGISTER", "UNDO"}


    def invoke(self, context, event):

        scn = context.scene

        Layers = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers

        for Layer in Layers:
            for index, object in enumerate(Layer.Objects):
                if object.Object:
                    Object_Check = context.view_layer.objects.get(object.Object.name)

                    if not Object_Check:
                        Layer.Objects.remove(index)
                else:
                    Layer.Objects.remove(index)



        utility_function.update_UI()


        return {'FINISHED'}














class POL_OT_Remove_Selected_Layer_Object(bpy.types.Operator):

    bl_idname = "pol.remove_selected_layer_object"
    bl_label = "Remove Layer Object"
    bl_description = "Remove Layer Object"
    bl_options = {"REGISTER", "UNDO"}

    def invoke(self, context, event):

        scn = context.scene
        Layer = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers[scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index]

        selected = context.selected_objects

        for selected_object in selected:

            count = -1

            while(True):
                if len(Layer.Objects) > 0:
                    for object in Layer.Objects:

                        count += 1
                        print(object.Object)
                        print(selected_object)

                        if object.Object == selected_object:
                            Layer.Objects.remove(count)
                            break
                break



        utility_function.update_UI()


        return {'FINISHED'}






class POL_OT_Solo_Layer(bpy.types.Operator):

    bl_idname = "pol.solo_layer"
    bl_label = "Solo Layer"
    bl_description = "Solo Layer"
    bl_options = {"REGISTER", "UNDO"}
    index : bpy.props.IntProperty()

    def invoke(self, context, event):

        scn = context.scene

        Layers = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers

        Active_Layer = Layers[self.index]


        for Layer in Layers:


            if event.shift:
                if Layer == Layers[self.index]:
                    if Layer.Solo_State:
                        Layer.Solo_State = False
                    else:
                        Layer.Solo_State = True

            else:
                if Layer == Layers[self.index]:
                    if Layer.Solo_State:
                        Layer.Solo_State = False
                    else:
                        Layer.Solo_State = True
                else:
                    Layer.Solo_State = False



        utility_function.update_UI()


        return {'FINISHED'}





class POL_OT_Add_Layer_Session(bpy.types.Operator):

    bl_idname = "pol.add_layer_session"
    bl_label = "Add Layer Category"
    bl_description = "Add Layer Category"
    bl_options = {"REGISTER", "UNDO"}
    Name: bpy.props.StringProperty(default="Category")

    def invoke(self, context, event):
        scn = context.scene
        self.Name = "Category" + str(len(scn.POL_Layer_Session))

        return context.window_manager.invoke_props_dialog(self)
        # return self.execute(context)

    def execute(self, context):

        scn = context.scene

        newItem = scn.POL_Layer_Session.add()
        newItem.Name = self.Name
        scn.POL_Layer_Session_Index = len(scn.POL_Layer_Session)-1

        utility_function.update_UI()

        return {'FINISHED'}


#Drop Down
#Extra operator
#Utility in Object Layer (Hide Unhide)
#Utility in Catagory Layer (Hide Unhide)
#Catagory Drop Down - Optional
#New Icon Expose Style


class POL_OT_Remove_Layer_Session(bpy.types.Operator):

    bl_idname = "pol.remove_layer_session"
    bl_label = "Remove Layer Session"
    bl_description = "Remove Layer Session"
    bl_options = {"REGISTER", "UNDO"}
    index: bpy.props.IntProperty()

    def execute(self, context):


        scn = context.scene

        Session = scn.POL_Layer_Session
        Session_Index = scn.POL_Layer_Session_Index
        Session.remove(self.index)

        if len(Session) > 0:
            if scn.POL_Layer_Session_Index == 0:
                scn.POL_Layer_Session_Index = 0
            if scn.POL_Layer_Session_Index > 0:
                scn.POL_Layer_Session_Index -= 1

        if len(Session) == 0:
            New = Session.add()
            New.Name = "Category"

        utility_function.update_UI()

        return {'FINISHED'}



def Utils_Create_Empty(name, location):

    Object = bpy.data.objects.new(name, None)
    bpy.context.collection.objects.link(Object)
    Object.location = location

    return Object

def Utils_Midpoint(points):

    sum_point = numpy.sum(points, 0)
    mid_point = [p / len(points) for p in sum_point]


    return mid_point




class POL_OT_Reorder_Layer_Session(bpy.types.Operator):

    bl_idname = "pol.reorder_layer_session"
    bl_label = "Reorder Layer Session"
    bl_description = "Reorder Layer Session"
    bl_options = {"REGISTER", "UNDO"}
    mode: bpy.props.StringProperty()

    def invoke(self, context, event):

        scn = context.scene
        sessions = scn.POL_Layer_Session
        session = sessions[scn.POL_Layer_Session_Index]

        if self.mode == "DOWN" and scn.POL_Layer_Session_Index < len(sessions) -1:


          sessions.move(scn.POL_Layer_Session_Index, scn.POL_Layer_Session_Index+1)
          scn.POL_Layer_Session_Index = scn.POL_Layer_Session_Index + 1


        if self.mode == "UP" and scn.POL_Layer_Session_Index >= 1:


            sessions.move(scn.POL_Layer_Session_Index, scn.POL_Layer_Session_Index-1)
            scn.POL_Layer_Session_Index = scn.POL_Layer_Session_Index - 1

        utility_function.update_UI()
        return {'FINISHED'}

class POL_OT_Reorder_Layer(bpy.types.Operator):

    bl_idname = "pol.reorder_layer"
    bl_label = "Reorder Layer"
    bl_description = "Reorder Layer"
    bl_options = {"REGISTER", "UNDO"}
    mode: bpy.props.StringProperty()

    def invoke(self, context, event):

        scn = context.scene


        session = scn.POL_Layer_Session[scn.POL_Layer_Session_Index]
        layers = session.Layers

        if len(layers) > 0:
            layer = layers[session.Layers_Index]

            if self.mode == "DOWN" and session.Layers_Index < len(layers) -1:

                print("run down")
                layers.move(session.Layers_Index, session.Layers_Index+1)
                session.Layers_Index = session.Layers_Index + 1


            if self.mode == "UP" and session.Layers_Index >= 1:

                print("run up")
                layers.move(session.Layers_Index, session.Layers_Index-1)
                session.Layers_Index = session.Layers_Index - 1

        utility_function.update_UI()
        return {'FINISHED'}























        return {'FINISHED'}







classes = [
        POL_OT_Add_Pseudo_Layer,
        POL_OT_Add_Layer_Object,
        POL_OT_Add_Selected_to_Layer,
        POL_OT_New_Layer_From_Selected,
        POL_OT_Remove_Pseudo_Layer,
        POL_OT_Remove_Layer_Object,
        POL_OT_Select_Layer_Object,
        POL_OT_Frame_Layer_Object,
        POL_OT_Remove_Selected_Layer_Object,
        POL_OT_Frame_Layer_Objects,
        POL_OT_Solo_Layer,
        POL_OT_Add_Layer_Session,
        POL_OT_Remove_Layer_Session,
        POL_OT_Reorder_Layer_Session,
        POL_OT_Reorder_Layer,
        POL_OT_Purge_Missing_Objects,
        ]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
