import bpy


class KeymapperOperator(bpy.types.Operator):
    """Searches the keymap for the selected key(s)"""
    bl_idname = "preferences.keymapper"
    bl_label = "Keymapper"
    bl_options = {'REGISTER', 'UNDO'}

    key: bpy.props.StringProperty()

    def execute(self, context):
        space = context.space_data
        space.filter_type = 'KEY'
        space.filter_text = f"{self.key}"
        return {'FINISHED'}
