import bpy


class KeymapperProperties(bpy.types.PropertyGroup):

    def search(self, context):
        shift = ''
        ctrl = ''
        alt = ''
        oskey = ''
        wm = context.window_manager
        keyconfig = wm.keyconfigs['Blender']
        keymap = keyconfig.keymaps[self.keymap]
        for keymap_item in keymap.keymap_items:
            if keymap_item.name == self.keymap_item:
                item = keymap.keymap_items[keymap_item.idname]
                if item.shift:
                    shift = 'Shift '
                if item.ctrl:
                    ctrl = 'Ctrl '
                if item.alt:
                    alt = 'Alt '
                if item.oskey:
                    oskey = 'OS '
                self.keybind = f"{shift}{ctrl}{alt}{oskey}{item.type}"
        context.space_data.filter_type = 'NAME'
        context.space_data.filter_text = f'{self.keymap_item}'

    def get_keymap(self, context):
        keymaps = []
        wm = context.window_manager
        keyconfig = wm.keyconfigs['Blender']
        for keymap in keyconfig.keymaps:
            keymaps.append((keymap.name, keymap.name, ''))
            context.scene.keymaps.append(keymaps)
        return keymaps

    def get_keymap_item(self, context):
        keymap_items = []
        wm = context.window_manager
        keyconfig = wm.keyconfigs['Blender']
        keymap = keyconfig.keymaps[self.keymap]
        for item in keymap.keymap_items:
            keymap_items.append((item.name, item.name, ''))
            context.scene.keymap_items.append(keymap_items)
        return keymap_items

    keymap: bpy.props.EnumProperty(
        name='Keymap',  # noqa: F821
        description='List of Keymaps',
        items=get_keymap,
    )

    keymap_item: bpy.props.EnumProperty(
        name='Item',  # noqa: F821
        description='List of Keymap Items',
        items=get_keymap_item,
        update=search,
    )

    keybind: bpy.props.StringProperty(
        name='Keybind',  # noqa: F821
        description='Keyboard Shortcut for the current item',
        default='Ctrl N'
    )

    idname: bpy.props.StringProperty()
