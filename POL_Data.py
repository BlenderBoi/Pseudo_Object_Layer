import bpy
from . import utility_function


Display_As_Enum = [("BOUNDS", "Bounds","Bounds"),("WIRE", "Wire", "Wire"), ("SOLID","Solid", "Solid"), ("TEXTURED","Textured", "Textured")]

def update_visibility(self, context):
    for obj in self.Objects:
        if context.view_layer.objects.get(obj.Object.name):
            obj.Object.hide_viewport = not(self.Visibility_State)
            # obj.Object.hide_render = not(self.Visibility_State)
            obj.Object.hide_set(not(self.Visibility_State))

def update_render(self, context):
    for obj in self.Objects:
        if context.view_layer.objects.get(obj.Object.name):
            obj.Object.hide_render = not(self.Render_State)


def update_selectable(self, context):
    for obj in self.Objects:
        if context.view_layer.objects.get(obj.Object.name):
            obj.Object.hide_select = self.Selectable_State

def update_display_as_state(self, context):

    for obj in self.Objects:
        if context.view_layer.objects.get(obj.Object.name):
            obj.Object.display_type = self.Display_As_State

def update_modifier_state(self, context):

    for obj in self.Objects:
        if context.view_layer.objects.get(obj.Object.name):
            if len(obj.Object.modifiers) > 0:
                for modifier in obj.Object.modifiers:
                    if modifier.type != 'PARTICLE_SYSTEM':
                        modifier.show_viewport = self.Modifier_State
                        modifier.show_render = self.Modifier_State

def update_particle_emitter(self, context):

    for obj in self.Objects:
        if context.view_layer.objects.get(obj.Object.name):
            if len(obj.Object.modifiers) > 0:
                for modifier in obj.Object.modifiers:
                    if modifier.type == 'PARTICLE_SYSTEM':
                        modifier.show_viewport = self.Particle_System_State
                        modifier.show_render = self.Particle_System_State

def update_solo_state(self, context):

    scn = context.scene
    Layers = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers


    Layer_Check = [not(Layer.Solo_State) for Layer in Layers]

    if all(Layer_Check):
        for Layer in Layers:
            Layer.Visibility_State = True

    else:
        for Layer in Layers:
            Layer.Visibility_State = Layer.Solo_State


    utility_function.update_UI()

    # return {'FINISHED'}









class POL_Object_PropertyGroup(bpy.types.PropertyGroup):

    Object : bpy.props.PointerProperty(type=bpy.types.Object)


class POL_Layer_PropertyGroup(bpy.types.PropertyGroup):

    Name : bpy.props.StringProperty()

    Show_Object : bpy.props.BoolProperty(default=False)


    Visibility_State : bpy.props.BoolProperty(update = update_visibility, default=True)
    Selectable_State : bpy.props.BoolProperty(update = update_selectable, default=False)
    Render_State: bpy.props.BoolProperty(update = update_render, default = True)

    Display_As_State : bpy.props.EnumProperty(update = update_display_as_state, default="TEXTURED", items=Display_As_Enum)

    Modifier_State : bpy.props.BoolProperty(update = update_modifier_state, default=True)
    Particle_System_State : bpy.props.BoolProperty(update = update_particle_emitter, default=True)

    Solo_State : bpy.props.BoolProperty(update = update_solo_state, default=False)

    Objects : bpy.props.CollectionProperty(type=POL_Object_PropertyGroup)
    Object_Index : bpy.props.IntProperty()


class POL_Layer_Session_PropertyGroup(bpy.types.PropertyGroup):

    Name : bpy.props.StringProperty()
    Layers : bpy.props.CollectionProperty(type=POL_Layer_PropertyGroup)
    Layers_Index : bpy.props.IntProperty()



class POL_UL_Object_List(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        scn = context.scene
        ob = data
        row = layout.row(align=True)



        Frame_Object = row.operator("pol.frame_layer_object", text="", icon="VIEWZOOM")
        Frame_Object.object_index = index
        Frame_Object.layer_index = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index


        # row.prop(item, "Object", text="", emboss=False)
        row.label(text=item.Object.name)


        Remove = row.operator("pol.remove_layer_object", text="", icon="TRASH")
        Remove.object_index = index
        Remove.layer_index = scn.POL_Layer_Session[scn.POL_Layer_Session_Index].Layers_Index




class POL_UL_Layer_Session_List(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        scn = context.scene
        ob = data
        row = layout.row()



        row.prop(item, "Name", emboss=False, text="")
        row.operator("pol.remove_layer_session", text="", icon="TRASH").index = index


class POL_UL_Layer_List(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        scn = context.scene
        ob = data
        row = layout.row(align=True)

        # visibility = row.operator("pol.toogle_visibility_layer_object", text="", icon="HIDE_OFF")
        # visibility.index = index
        # visibility.state = True



        if scn.POL_List_Icon.Solo:
            if item.Solo_State:
                Solo = row.operator("pol.solo_layer", text="", icon="RADIOBUT_ON")
                Solo.index = index
            else:
                Solo = row.operator("pol.solo_layer", text="", icon="RADIOBUT_OFF")
                Solo.index = index
            # row.prop(item, "Solo_State", text="", icon="RADIOBUT_ON")
        if scn.POL_List_Icon.layer_to_collection:
            LTC = row.operator("pol.layer_to_collection", text="", icon="COLLECTION_NEW")
            LTC.index = index

        if scn.POL_List_Icon.Select:
            Select = row.operator("pol.select_layer_object", text="", icon="RESTRICT_SELECT_OFF")
            Select.index = index

        if scn.POL_List_Icon.Search:
            Search = row.operator("pol.frame_layer_objects", text="", icon="VIEWZOOM")
            Search.layer_index = index

        if scn.POL_List_Icon.Modifier:
            row.prop(item, "Modifier_State", text="", icon="MODIFIER")

        if scn.POL_List_Icon.Display_As:
            row.prop(item, "Display_As_State", text="", icon="MOD_WIREFRAME")

        if scn.POL_List_Icon.Visibility:
            row.prop(item, "Visibility_State", text="", icon="HIDE_OFF")

        if scn.POL_List_Icon.Render:
            row.prop(item, "Render_State", text="", icon="RESTRICT_RENDER_OFF")



        if scn.POL_List_Icon.key_Visibility:
            row.operator("pol.key_visibility",text="", icon="KEYTYPE_MOVING_HOLD_VEC").index = index

        # if scn.POL_List_Icon.drive_Visibility:
        #     row.operator("pol.drive_visibility",text="", icon="DRIVER").index = index
        #
        if scn.POL_List_Icon.Export:
            row.operator("pol.export_layer_to_fbx", text="", icon ="EXPORT").index = index

        if scn.POL_List_Icon.Lock:
            row.prop(item, "Selectable_State", text="", icon="LOCKED")

        if scn.POL_List_Icon.Particle:
            row.prop(item, "Particle_System_State", text="", icon="PARTICLE_DATA")
        row.prop(item, "Name", text="", emboss=False)

        if scn.POL_List_Icon.Trash:
            row.operator("pol.remove_pseudo_layer", text="", icon="TRASH").index = index

        col = row.column()



class POL_List_Icon_PropertyGroup(bpy.types.PropertyGroup):

    Show_Icon_Expose : bpy.props.BoolProperty(default=False)

    Export : bpy.props.BoolProperty(default=False)
    Select : bpy.props.BoolProperty(default=True)
    Modifier : bpy.props.BoolProperty(default=False)
    Display_As : bpy.props.BoolProperty(default=False)
    Visibility : bpy.props.BoolProperty(default=True)
    Render : bpy.props.BoolProperty(default=True)
    Lock : bpy.props.BoolProperty(default=True)
    Solo : bpy.props.BoolProperty(default=False)
    Particle : bpy.props.BoolProperty(default=False)
    Trash : bpy.props.BoolProperty(default=True)
    Search : bpy.props.BoolProperty(default=False)
    key_Visibility : bpy.props.BoolProperty(default=False)
    layer_to_collection: bpy.props.BoolProperty(default=False)

    # drive_Visibility: bpy.props.BoolProperty(default=False)
#Search
#Solo

def POL_DynamicEnum_Session_Update(self, context):

    scn = context.scene

    if scn.POL_Session_Dropdown == "NEW":

        bpy.ops.pol.add_layer_session("INVOKE_DEFAULT")
        scn.POL_Session_Dropdown = str(len(scn.POL_Session_Dropdown) - 3)


    else:
        if not scn.POL_Layer_Session_Index == int(scn.POL_Session_Dropdown):
            scn.POL_Layer_Session_Index = int(scn.POL_Session_Dropdown)


def POL_Update_SessionEnum(self, context):

    scn = context.scene


    if not str(scn.POL_Session_Dropdown) == scn.POL_Layer_Session_Index:
        scn.POL_Session_Dropdown = str(scn.POL_Layer_Session_Index)


def POL_DynamicDropdown(self, context):

    scn = bpy.context.scene

    Enum = []

    for index, Session in enumerate(scn.POL_Layer_Session):
        item = (str(index), Session.Name, Session.Name)
        Enum.append(item)

    additem = ("NEW","*New Category*","New Category")

    Enum.append(additem)

    return Enum



classes = (
    POL_Object_PropertyGroup,
    POL_Layer_PropertyGroup,
    POL_UL_Object_List,
    POL_UL_Layer_List,
    POL_List_Icon_PropertyGroup,
    POL_Layer_Session_PropertyGroup,
    POL_UL_Layer_Session_List
        )


def register():

    for cls in classes:
        bpy.utils.register_class(cls)


    bpy.types.Scene.POL_Session_Dropdown = bpy.props.EnumProperty(items=POL_DynamicDropdown, update=POL_DynamicEnum_Session_Update)
    bpy.types.Scene.POL_Operators = bpy.props.BoolProperty(default=False)

    bpy.types.Scene.POL_List_Icon = bpy.props.PointerProperty(type=POL_List_Icon_PropertyGroup)

    bpy.types.Scene.POL_Session_Show = bpy.props.BoolProperty(default=False)

    # bpy.types.Scene.POL_Layers = bpy.props.CollectionProperty(type=POL_Layer_PropertyGroup)
    # bpy.types.Scene.POL_Layers_Index = bpy.props.IntProperty()

    bpy.types.Scene.POL_Layer_Session = bpy.props.CollectionProperty(type=POL_Layer_Session_PropertyGroup)
    bpy.types.Scene.POL_Layer_Session_Index = bpy.props.IntProperty(update=POL_Update_SessionEnum)

    bpy.types.Scene.POL_Show_Object_List = bpy.props.BoolProperty(default=False)

    # bpy.types.Scene.POL_Layer_To_Collection = bpy.props.BoolProperty(default=False)





def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.POL_Session_Dropdown
    del bpy.types.Scene.POL_Operators
    del bpy.types.Scene.POL_Session_Show

    # del bpy.types.Scene.POL_Layers
    # del bpy.types.Scene.POL_Layers_Index

    del bpy.types.Scene.POL_Layer_Session
    del bpy.types.Scene.POL_Layer_Session_Index


    del bpy.types.Scene.POL_Show_Object_List
    # del bpy.types.Scene.POL_Layer_To_Collection


if __name__ == "__main__":
    register()
