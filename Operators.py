import bpy
from . Keyboard_Layouts import key_names


class KeymapperOperator(bpy.types.Operator):
    """Searches the keymap for the selected key(s)"""
    bl_idname = "preferences.keymapper"
    bl_label = "Keymapper"
    bl_options = {'REGISTER', 'UNDO'}

    key: bpy.props.StringProperty()

    def execute(self, context):
        props = context.scene.keymapper_props  # noqa: F841
        space = context.space_data
        space.filter_type = 'KEY'
        space.filter_text = f"{self.key}"
        for key in key_names:
            if key_names[key] == self.key.replace('Numpad ', ''):
                prop = key
        exec(f"props.k_{prop} = not props.k_{prop}")
        return {'FINISHED'}
