import bpy
import pathlib
import os
import bpy_extras

def export_layers_to_fbx(context,
filepath,
use_active_collection,
global_scale,
apply_unit_scale,
apply_scale_options,
use_space_transform,
bake_space_transform,
object_types,
use_mesh_modifiers,
use_mesh_modifiers_render,
mesh_smooth_type,
use_subsurf,
use_mesh_edges,
use_tspace,
use_custom_props,
add_leaf_bones,
primary_bone_axis,
secondary_bone_axis,
use_armature_deform_only,
armature_nodetype,
bake_anim,
bake_anim_use_all_bones,
bake_anim_use_nla_strips,
bake_anim_use_all_actions,
bake_anim_force_startend_keying,
bake_anim_step,
bake_anim_simplify_factor,
path_mode,
embed_textures,
batch_mode,
use_batch_own_dir,
use_metadata):

    POL_Session = bpy.context.scene.POL_Layer_Session[bpy.context.scene.POL_Layer_Session_Index]
    Layers = POL_Session.Layers

    for Layer in Layers:
        Layer.Visibility_State = True
        Objects = Layer.Objects
        bpy.ops.object.select_all(action='DESELECT')

        for object in Objects:

            object.Object.select_set(True)

        path = os.path.dirname(filepath)
        basename = pathlib.Path(filepath).stem

        filename = basename + "_" + Layer.Name + ".fbx"
        path = os.path.join(path, filename)
        print(path)
        bpy.ops.export_scene.fbx(
        use_selection = True,
        filepath=path,
        use_active_collection = use_active_collection,
        global_scale = global_scale,
        apply_unit_scale = apply_unit_scale,
        apply_scale_options = apply_scale_options,
        use_space_transform = use_space_transform,
        bake_space_transform = bake_space_transform,
        object_types = object_types,
        use_mesh_modifiers = use_mesh_modifiers,
        use_mesh_modifiers_render = use_mesh_modifiers_render,
        mesh_smooth_type = mesh_smooth_type,
        use_subsurf = use_subsurf,
        use_mesh_edges = use_mesh_edges,
        use_tspace = use_tspace,
        use_custom_props = use_custom_props,
        add_leaf_bones = add_leaf_bones,
        primary_bone_axis = primary_bone_axis,
        secondary_bone_axis = secondary_bone_axis,
        use_armature_deform_only = use_armature_deform_only,
        armature_nodetype = armature_nodetype,
        bake_anim = bake_anim,
        bake_anim_use_all_bones = bake_anim_use_all_bones,
        bake_anim_use_nla_strips = bake_anim_use_nla_strips,
        bake_anim_use_all_actions = bake_anim_use_all_actions,
        bake_anim_force_startend_keying = bake_anim_force_startend_keying,
        bake_anim_step = bake_anim_step,
        bake_anim_simplify_factor = bake_anim_simplify_factor,
        path_mode = path_mode,
        embed_textures = embed_textures,
        batch_mode = batch_mode,
        use_batch_own_dir = use_batch_own_dir,
        use_metadata = use_metadata



        )

    bpy.ops.object.select_all(action='DESELECT')
    return {'FINISHED'}



def export_layer_to_fbx(context,
index,
filepath,
use_active_collection,
global_scale,
apply_unit_scale,
apply_scale_options,
use_space_transform,
bake_space_transform,
object_types,
use_mesh_modifiers,
use_mesh_modifiers_render,
mesh_smooth_type,
use_subsurf,
use_mesh_edges,
use_tspace,
use_custom_props,
add_leaf_bones,
primary_bone_axis,
secondary_bone_axis,
use_armature_deform_only,
armature_nodetype,
bake_anim,
bake_anim_use_all_bones,
bake_anim_use_nla_strips,
bake_anim_use_all_actions,
bake_anim_force_startend_keying,
bake_anim_step,
bake_anim_simplify_factor,
path_mode,
embed_textures,
batch_mode,
use_batch_own_dir,
use_metadata):

    POL_Session = bpy.context.scene.POL_Layer_Session[bpy.context.scene.POL_Layer_Session_Index]
    Layers = POL_Session.Layers
    Layer = Layers[index]

    Layer.Visibility_State = True
    Objects = Layer.Objects
    bpy.ops.object.select_all(action='DESELECT')

    for object in Objects:

        object.Object.select_set(True)

    path = os.path.dirname(filepath)
    basename = pathlib.Path(filepath).stem

    filename = basename + "_" + Layer.Name + ".fbx"
    path = os.path.join(path, filename)
    print(path)
    bpy.ops.export_scene.fbx(
    use_selection = True,
    filepath=path,
    use_active_collection = use_active_collection,
    global_scale = global_scale,
    apply_unit_scale = apply_unit_scale,
    apply_scale_options = apply_scale_options,
    use_space_transform = use_space_transform,
    bake_space_transform = bake_space_transform,
    object_types = object_types,
    use_mesh_modifiers = use_mesh_modifiers,
    use_mesh_modifiers_render = use_mesh_modifiers_render,
    mesh_smooth_type = mesh_smooth_type,
    use_subsurf = use_subsurf,
    use_mesh_edges = use_mesh_edges,
    use_tspace = use_tspace,
    use_custom_props = use_custom_props,
    add_leaf_bones = add_leaf_bones,
    primary_bone_axis = primary_bone_axis,
    secondary_bone_axis = secondary_bone_axis,
    use_armature_deform_only = use_armature_deform_only,
    armature_nodetype = armature_nodetype,
    bake_anim = bake_anim,
    bake_anim_use_all_bones = bake_anim_use_all_bones,
    bake_anim_use_nla_strips = bake_anim_use_nla_strips,
    bake_anim_use_all_actions = bake_anim_use_all_actions,
    bake_anim_force_startend_keying = bake_anim_force_startend_keying,
    bake_anim_step = bake_anim_step,
    bake_anim_simplify_factor = bake_anim_simplify_factor,
    path_mode = path_mode,
    embed_textures = embed_textures,
    batch_mode = batch_mode,
    use_batch_own_dir = use_batch_own_dir,
    use_metadata = use_metadata



    )

    bpy.ops.object.select_all(action='DESELECT')
    return {'FINISHED'}


@bpy_extras.io_utils.orientation_helper(axis_forward='-Z', axis_up='Y')
class POL_Export_Layers_To_FBX(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):

    bl_idname = "pol.export_layers_to_fbx"
    bl_label = "Export Layers to FBX"


    filename_ext = ".fbx"
    filter_glob: bpy.props.StringProperty(default="*.fbx", options={'HIDDEN'})
    directory: bpy.props.StringProperty()

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.

    # use_selection: bpy.props.BoolProperty(
    #         name="Selected Objects",
    #         description="Export selected and visible objects only",
    #         default=False,
    #         )
    use_active_collection: bpy.props.BoolProperty(
            name="Active Collection",
            description="Export only objects from the active collection (and its children)",
            default=False,
            )
    global_scale: bpy.props.FloatProperty(
            name="Scale",
            description="Scale all data (Some importers do not support scaled armatures!)",
            min=0.001, max=1000.0,
            soft_min=0.01, soft_max=1000.0,
            default=1.0,
            )
    apply_unit_scale: bpy.props.BoolProperty(
            name="Apply Unit",
            description="Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)",
            default=True,
            )
    apply_scale_options: bpy.props.EnumProperty(
            items=(('FBX_SCALE_NONE', "All Local",
                    "Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0"),
                   ('FBX_SCALE_UNITS', "FBX Units Scale",
                    "Apply custom scaling to each object transformation, and units scaling to FBX scale"),
                   ('FBX_SCALE_CUSTOM', "FBX Custom Scale",
                    "Apply custom scaling to FBX scale, and units scaling to each object transformation"),
                   ('FBX_SCALE_ALL', "FBX All",
                    "Apply custom scaling and units scaling to FBX scale"),
                   ),
            name="Apply Scalings",
            description="How to apply custom and units scalings in generated FBX file "
                        "(Blender uses FBX scale to detect units on import, "
                        "but many other applications do not handle the same way)",
            )

    use_space_transform: bpy.props.BoolProperty(
            name="Use Space Transform",
            description="Apply global space transform to the object rotations. When disabled "
                        "only the axis space is written to the file and all object transforms are left as-is",
            default=True,
            )
    bake_space_transform: bpy.props.BoolProperty(
            name="Apply Transform",
            description="Bake space transform into object data, avoids getting unwanted rotations to objects when "
                        "target space is not aligned with Blender's space "
                        "(WARNING! experimental option, use at own risks, known broken with armatures/animations)",
            default=False,
            )

    object_types: bpy.props.EnumProperty(
            name="Object Types",
            options={'ENUM_FLAG'},
            items=(('EMPTY', "Empty", ""),
                   ('CAMERA', "Camera", ""),
                   ('LIGHT', "Lamp", ""),
                   ('ARMATURE', "Armature", "WARNING: not supported in dupli/group instances"),
                   ('MESH', "Mesh", ""),
                   ('OTHER', "Other", "Other geometry types, like curve, metaball, etc. (converted to meshes)"),
                   ),
            description="Which kind of object to export",
            default={'EMPTY', 'CAMERA', 'LIGHT', 'ARMATURE', 'MESH', 'OTHER'},
            )

    use_mesh_modifiers: bpy.props.BoolProperty(
            name="Apply Modifiers",
            description="Apply modifiers to mesh objects (except Armature ones) - "
                        "WARNING: prevents exporting shape keys",
            default=True,
            )
    use_mesh_modifiers_render: bpy.props.BoolProperty(
            name="Use Modifiers Render Setting",
            description="Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)",
            default=True,
            )
    mesh_smooth_type: bpy.props.EnumProperty(
            name="Smoothing",
            items=(('OFF', "Normals Only", "Export only normals instead of writing edge or face smoothing data"),
                   ('FACE', "Face", "Write face smoothing"),
                   ('EDGE', "Edge", "Write edge smoothing"),
                   ),
            description="Export smoothing information "
                        "(prefer 'Normals Only' option if your target importer understand split normals)",
            default='OFF',
            )
    use_subsurf: bpy.props.BoolProperty(
            name="Export Subdivision Surface",
            description="Export the last Catmull-Rom subdivision modifier as FBX subdivision "
                        "(does not apply the modifier even if 'Apply Modifiers' is enabled)",
            default=False,
            )
    use_mesh_edges: bpy.props.BoolProperty(
            name="Loose Edges",
            description="Export loose edges (as two-vertices polygons)",
            default=False,
            )
    use_tspace: bpy.props.BoolProperty(
            name="Tangent Space",
            description="Add binormal and tangent vectors, together with normal they form the tangent space "
                        "(will only work correctly with tris/quads only meshes!)",
            default=False,
            )
    use_custom_props: bpy.props.BoolProperty(
            name="Custom Properties",
            description="Export custom properties",
            default=False,
            )
    add_leaf_bones: bpy.props.BoolProperty(
            name="Add Leaf Bones",
            description="Append a final bone to the end of each chain to specify last bone length "
                        "(use this when you intend to edit the armature from exported data)",
            default=True # False for commit!
            )
    primary_bone_axis: bpy.props.EnumProperty(
            name="Primary Bone Axis",
            items=(('X', "X Axis", ""),
                   ('Y', "Y Axis", ""),
                   ('Z', "Z Axis", ""),
                   ('-X', "-X Axis", ""),
                   ('-Y', "-Y Axis", ""),
                   ('-Z', "-Z Axis", ""),
                   ),
            default='Y',
            )
    secondary_bone_axis: bpy.props.EnumProperty(
            name="Secondary Bone Axis",
            items=(('X', "X Axis", ""),
                   ('Y', "Y Axis", ""),
                   ('Z', "Z Axis", ""),
                   ('-X', "-X Axis", ""),
                   ('-Y', "-Y Axis", ""),
                   ('-Z', "-Z Axis", ""),
                   ),
            default='X',
            )
    use_armature_deform_only: bpy.props.BoolProperty(
            name="Only Deform Bones",
            description="Only write deforming bones (and non-deforming ones when they have deforming children)",
            default=False,
            )
    armature_nodetype: bpy.props.EnumProperty(
            name="Armature FBXNode Type",
            items=(('NULL', "Null", "'Null' FBX node, similar to Blender's Empty (default)"),
                   ('ROOT', "Root", "'Root' FBX node, supposed to be the root of chains of bones..."),
                   ('LIMBNODE', "LimbNode", "'LimbNode' FBX node, a regular joint between two bones..."),
                  ),
            description="FBX type of node (object) used to represent Blender's armatures "
                        "(use Null one unless you experience issues with other app, other choices may no import back "
                        "perfectly in Blender...)",
            default='NULL',
            )
    bake_anim: bpy.props.BoolProperty(
            name="Baked Animation",
            description="Export baked keyframe animation",
            default=True,
            )
    bake_anim_use_all_bones: bpy.props.BoolProperty(
            name="Key All Bones",
            description="Force exporting at least one key of animation for all bones "
                        "(needed with some target applications, like UE4)",
            default=True,
            )
    bake_anim_use_nla_strips: bpy.props.BoolProperty(
            name="NLA Strips",
            description="Export each non-muted NLA strip as a separated FBX's AnimStack, if any, "
                        "instead of global scene animation",
            default=True,
            )
    bake_anim_use_all_actions: bpy.props.BoolProperty(
            name="All Actions",
            description="Export each action as a separated FBX's AnimStack, instead of global scene animation "
                        "(note that animated objects will get all actions compatible with them, "
                        "others will get no animation at all)",
            default=True,
            )
    bake_anim_force_startend_keying: bpy.props.BoolProperty(
            name="Force Start/End Keying",
            description="Always add a keyframe at start and end of actions for animated channels",
            default=True,
            )
    bake_anim_step: bpy.props.FloatProperty(
            name="Sampling Rate",
            description="How often to evaluate animated values (in frames)",
            min=0.01, max=100.0,
            soft_min=0.1, soft_max=10.0,
            default=1.0,
            )
    bake_anim_simplify_factor: bpy.props.FloatProperty(
            name="Simplify",
            description="How much to simplify baked values (0.0 to disable, the higher the more simplified)",
            min=0.0, max=100.0,  # No simplification to up to 10% of current magnitude tolerance.
            soft_min=0.0, soft_max=10.0,
            default=1.0,  # default: min slope: 0.005, max frame step: 10.
            )
    path_mode: bpy_extras.io_utils.path_reference_mode
    embed_textures: bpy.props.BoolProperty(
            name="Embed Textures",
            description="Embed textures in FBX binary file (only for \"Copy\" path mode!)",
            default=False,
            )
    batch_mode: bpy.props.EnumProperty(
            name="Batch Mode",
            items=(('OFF', "Off", "Active scene to file"),
                   ('SCENE', "Scene", "Each scene as a file"),
                   ('COLLECTION', "Collection",
                    "Each collection (data-block ones) as a file, does not include content of children collections"),
                   ('SCENE_COLLECTION', "Scene Collections",
                    "Each collection (including master, non-data-block ones) of each scene as a file, "
                    "including content from children collections"),
                   ('ACTIVE_SCENE_COLLECTION', "Active Scene Collections",
                    "Each collection (including master, non-data-block one) of the active scene as a file, "
                    "including content from children collections"),
                   ),
            )
    use_batch_own_dir: bpy.props.BoolProperty(
            name="Batch Own Dir",
            description="Create a dir for each exported file",
            default=True,
            )
    use_metadata: bpy.props.BoolProperty(
            name="Use Metadata",
            default=True,
            options={'HIDDEN'},
            )





    # def draw(self, context):
    #     pass



    def execute(self, context):

        return export_layers_to_fbx(
        context,
        self.filepath,
        self.use_active_collection,
        self.global_scale,
        self.apply_unit_scale,
        self.apply_scale_options,
        self.use_space_transform,
        self.bake_space_transform,
        self.object_types,
        self.use_mesh_modifiers,
        self.use_mesh_modifiers_render,
        self.mesh_smooth_type,
        self.use_subsurf,
        self.use_mesh_edges,
        self.use_tspace,
        self.use_custom_props,
        self.add_leaf_bones,
        self.primary_bone_axis,
        self.secondary_bone_axis,
        self.use_armature_deform_only,
        self.armature_nodetype,
        self.bake_anim,
        self.bake_anim_use_all_bones,
        self.bake_anim_use_nla_strips,
        self.bake_anim_use_all_actions,
        self.bake_anim_force_startend_keying,
        self.bake_anim_step,
        self.bake_anim_simplify_factor,
        self.path_mode,
        self.embed_textures,
        self.batch_mode,
        self.use_batch_own_dir,
        self.use_metadata
        )











@bpy_extras.io_utils.orientation_helper(axis_forward='-Z', axis_up='Y')
class POL_Export_Layer_To_FBX(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    """Export Layer to FBX"""
    bl_idname = "pol.export_layer_to_fbx"
    bl_label = "Export Layer to FBX"

    index: bpy.props.IntProperty()
    filename_ext = ".fbx"
    filter_glob: bpy.props.StringProperty(default="*.fbx", options={'HIDDEN'})
    directory: bpy.props.StringProperty()

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.

    # use_selection: bpy.props.BoolProperty(
    #         name="Selected Objects",
    #         description="Export selected and visible objects only",
    #         default=False,
    #         )
    use_active_collection: bpy.props.BoolProperty(
            name="Active Collection",
            description="Export only objects from the active collection (and its children)",
            default=False,
            )
    global_scale: bpy.props.FloatProperty(
            name="Scale",
            description="Scale all data (Some importers do not support scaled armatures!)",
            min=0.001, max=1000.0,
            soft_min=0.01, soft_max=1000.0,
            default=1.0,
            )
    apply_unit_scale: bpy.props.BoolProperty(
            name="Apply Unit",
            description="Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)",
            default=True,
            )
    apply_scale_options: bpy.props.EnumProperty(
            items=(('FBX_SCALE_NONE', "All Local",
                    "Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0"),
                   ('FBX_SCALE_UNITS', "FBX Units Scale",
                    "Apply custom scaling to each object transformation, and units scaling to FBX scale"),
                   ('FBX_SCALE_CUSTOM', "FBX Custom Scale",
                    "Apply custom scaling to FBX scale, and units scaling to each object transformation"),
                   ('FBX_SCALE_ALL', "FBX All",
                    "Apply custom scaling and units scaling to FBX scale"),
                   ),
            name="Apply Scalings",
            description="How to apply custom and units scalings in generated FBX file "
                        "(Blender uses FBX scale to detect units on import, "
                        "but many other applications do not handle the same way)",
            )

    use_space_transform: bpy.props.BoolProperty(
            name="Use Space Transform",
            description="Apply global space transform to the object rotations. When disabled "
                        "only the axis space is written to the file and all object transforms are left as-is",
            default=True,
            )
    bake_space_transform: bpy.props.BoolProperty(
            name="Apply Transform",
            description="Bake space transform into object data, avoids getting unwanted rotations to objects when "
                        "target space is not aligned with Blender's space "
                        "(WARNING! experimental option, use at own risks, known broken with armatures/animations)",
            default=False,
            )

    object_types: bpy.props.EnumProperty(
            name="Object Types",
            options={'ENUM_FLAG'},
            items=(('EMPTY', "Empty", ""),
                   ('CAMERA', "Camera", ""),
                   ('LIGHT', "Lamp", ""),
                   ('ARMATURE', "Armature", "WARNING: not supported in dupli/group instances"),
                   ('MESH', "Mesh", ""),
                   ('OTHER', "Other", "Other geometry types, like curve, metaball, etc. (converted to meshes)"),
                   ),
            description="Which kind of object to export",
            default={'EMPTY', 'CAMERA', 'LIGHT', 'ARMATURE', 'MESH', 'OTHER'},
            )

    use_mesh_modifiers: bpy.props.BoolProperty(
            name="Apply Modifiers",
            description="Apply modifiers to mesh objects (except Armature ones) - "
                        "WARNING: prevents exporting shape keys",
            default=True,
            )
    use_mesh_modifiers_render: bpy.props.BoolProperty(
            name="Use Modifiers Render Setting",
            description="Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)",
            default=True,
            )
    mesh_smooth_type: bpy.props.EnumProperty(
            name="Smoothing",
            items=(('OFF', "Normals Only", "Export only normals instead of writing edge or face smoothing data"),
                   ('FACE', "Face", "Write face smoothing"),
                   ('EDGE', "Edge", "Write edge smoothing"),
                   ),
            description="Export smoothing information "
                        "(prefer 'Normals Only' option if your target importer understand split normals)",
            default='OFF',
            )
    use_subsurf: bpy.props.BoolProperty(
            name="Export Subdivision Surface",
            description="Export the last Catmull-Rom subdivision modifier as FBX subdivision "
                        "(does not apply the modifier even if 'Apply Modifiers' is enabled)",
            default=False,
            )
    use_mesh_edges: bpy.props.BoolProperty(
            name="Loose Edges",
            description="Export loose edges (as two-vertices polygons)",
            default=False,
            )
    use_tspace: bpy.props.BoolProperty(
            name="Tangent Space",
            description="Add binormal and tangent vectors, together with normal they form the tangent space "
                        "(will only work correctly with tris/quads only meshes!)",
            default=False,
            )
    use_custom_props: bpy.props.BoolProperty(
            name="Custom Properties",
            description="Export custom properties",
            default=False,
            )
    add_leaf_bones: bpy.props.BoolProperty(
            name="Add Leaf Bones",
            description="Append a final bone to the end of each chain to specify last bone length "
                        "(use this when you intend to edit the armature from exported data)",
            default=True # False for commit!
            )
    primary_bone_axis: bpy.props.EnumProperty(
            name="Primary Bone Axis",
            items=(('X', "X Axis", ""),
                   ('Y', "Y Axis", ""),
                   ('Z', "Z Axis", ""),
                   ('-X', "-X Axis", ""),
                   ('-Y', "-Y Axis", ""),
                   ('-Z', "-Z Axis", ""),
                   ),
            default='Y',
            )
    secondary_bone_axis: bpy.props.EnumProperty(
            name="Secondary Bone Axis",
            items=(('X', "X Axis", ""),
                   ('Y', "Y Axis", ""),
                   ('Z', "Z Axis", ""),
                   ('-X', "-X Axis", ""),
                   ('-Y', "-Y Axis", ""),
                   ('-Z', "-Z Axis", ""),
                   ),
            default='X',
            )
    use_armature_deform_only: bpy.props.BoolProperty(
            name="Only Deform Bones",
            description="Only write deforming bones (and non-deforming ones when they have deforming children)",
            default=False,
            )
    armature_nodetype: bpy.props.EnumProperty(
            name="Armature FBXNode Type",
            items=(('NULL', "Null", "'Null' FBX node, similar to Blender's Empty (default)"),
                   ('ROOT', "Root", "'Root' FBX node, supposed to be the root of chains of bones..."),
                   ('LIMBNODE', "LimbNode", "'LimbNode' FBX node, a regular joint between two bones..."),
                  ),
            description="FBX type of node (object) used to represent Blender's armatures "
                        "(use Null one unless you experience issues with other app, other choices may no import back "
                        "perfectly in Blender...)",
            default='NULL',
            )
    bake_anim: bpy.props.BoolProperty(
            name="Baked Animation",
            description="Export baked keyframe animation",
            default=True,
            )
    bake_anim_use_all_bones: bpy.props.BoolProperty(
            name="Key All Bones",
            description="Force exporting at least one key of animation for all bones "
                        "(needed with some target applications, like UE4)",
            default=True,
            )
    bake_anim_use_nla_strips: bpy.props.BoolProperty(
            name="NLA Strips",
            description="Export each non-muted NLA strip as a separated FBX's AnimStack, if any, "
                        "instead of global scene animation",
            default=True,
            )
    bake_anim_use_all_actions: bpy.props.BoolProperty(
            name="All Actions",
            description="Export each action as a separated FBX's AnimStack, instead of global scene animation "
                        "(note that animated objects will get all actions compatible with them, "
                        "others will get no animation at all)",
            default=True,
            )
    bake_anim_force_startend_keying: bpy.props.BoolProperty(
            name="Force Start/End Keying",
            description="Always add a keyframe at start and end of actions for animated channels",
            default=True,
            )
    bake_anim_step: bpy.props.FloatProperty(
            name="Sampling Rate",
            description="How often to evaluate animated values (in frames)",
            min=0.01, max=100.0,
            soft_min=0.1, soft_max=10.0,
            default=1.0,
            )
    bake_anim_simplify_factor: bpy.props.FloatProperty(
            name="Simplify",
            description="How much to simplify baked values (0.0 to disable, the higher the more simplified)",
            min=0.0, max=100.0,  # No simplification to up to 10% of current magnitude tolerance.
            soft_min=0.0, soft_max=10.0,
            default=1.0,  # default: min slope: 0.005, max frame step: 10.
            )
    path_mode: bpy_extras.io_utils.path_reference_mode
    embed_textures: bpy.props.BoolProperty(
            name="Embed Textures",
            description="Embed textures in FBX binary file (only for \"Copy\" path mode!)",
            default=False,
            )
    batch_mode: bpy.props.EnumProperty(
            name="Batch Mode",
            items=(('OFF', "Off", "Active scene to file"),
                   ('SCENE', "Scene", "Each scene as a file"),
                   ('COLLECTION', "Collection",
                    "Each collection (data-block ones) as a file, does not include content of children collections"),
                   ('SCENE_COLLECTION', "Scene Collections",
                    "Each collection (including master, non-data-block ones) of each scene as a file, "
                    "including content from children collections"),
                   ('ACTIVE_SCENE_COLLECTION', "Active Scene Collections",
                    "Each collection (including master, non-data-block one) of the active scene as a file, "
                    "including content from children collections"),
                   ),
            )
    use_batch_own_dir: bpy.props.BoolProperty(
            name="Batch Own Dir",
            description="Create a dir for each exported file",
            default=True,
            )
    use_metadata: bpy.props.BoolProperty(
            name="Use Metadata",
            default=True,
            options={'HIDDEN'},
            )





    # def draw(self, context):
    #     pass



    def execute(self, context):

        return export_layer_to_fbx(
        context,
        self.index,
        self.filepath,
        self.use_active_collection,
        self.global_scale,
        self.apply_unit_scale,
        self.apply_scale_options,
        self.use_space_transform,
        self.bake_space_transform,
        self.object_types,
        self.use_mesh_modifiers,
        self.use_mesh_modifiers_render,
        self.mesh_smooth_type,
        self.use_subsurf,
        self.use_mesh_edges,
        self.use_tspace,
        self.use_custom_props,
        self.add_leaf_bones,
        self.primary_bone_axis,
        self.secondary_bone_axis,
        self.use_armature_deform_only,
        self.armature_nodetype,
        self.bake_anim,
        self.bake_anim_use_all_bones,
        self.bake_anim_use_nla_strips,
        self.bake_anim_use_all_actions,
        self.bake_anim_force_startend_keying,
        self.bake_anim_step,
        self.bake_anim_simplify_factor,
        self.path_mode,
        self.embed_textures,
        self.batch_mode,
        self.use_batch_own_dir,
        self.use_metadata
        )





classes = [
        POL_Export_Layers_To_FBX,
        POL_Export_Layer_To_FBX
        ]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
