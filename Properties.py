import bpy
from . Keyboard_Layouts import key_names


class KeymapperProperties(bpy.types.PropertyGroup):

    def search(self, context):
        props = context.scene.keymapper_props
        wm = context.window_manager
        active_keyconfig = context.preferences.keymap.active_keyconfig
        keyconfig = wm.keyconfigs[active_keyconfig]
        keymap = keyconfig.keymaps[self.keymap]
        for keymap_item in keymap.keymap_items:
            if keymap_item.name == self.keymap_item:
                item = keymap.keymap_items[keymap_item.idname]
                props.shift = item.shift
                props.ctrl = item.ctrl
                props.alt = item.alt
                props.cmd = item.oskey
                self.keybind = f"{item.type}"
        context.space_data.filter_type = 'NAME'
        context.space_data.filter_text = f'{self.keymap_item}'

    def get_keymap(self, context):
        keymaps = []
        wm = context.window_manager
        active_keyconfig = context.preferences.keymap.active_keyconfig
        keyconfig = wm.keyconfigs[active_keyconfig]
        for keymap in keyconfig.keymaps:
            keymaps.append((keymap.name, keymap.name, ''))
            context.scene.keymaps.append(keymaps)
        return keymaps

    def get_keymap_item(self, context):
        keymap_items = []
        wm = context.window_manager
        active_keyconfig = context.preferences.keymap.active_keyconfig
        keyconfig = wm.keyconfigs[active_keyconfig]
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
        default='N'  # noqa: F821
    )

    for key in key_names:
        exec(f"k_{key}: bpy.props.BoolProperty()")

    show_keyboard: bpy.props.BoolProperty(
        name='Keyboard',  # noqa: F821
        description='Show/Hide the Keyboard',
        default=True
    )

    show_numpad: bpy.props.BoolProperty(
        name='Numpad',  # noqa: F821
        description='Show/Hide the Numpad',
        default=False
    )

    show_mouse: bpy.props.BoolProperty(
        name='Mouse',  # noqa: F821
        description='Show/Hide the Mouse',
        default=True
    )

    show_pen: bpy.props.BoolProperty(
        name='Pen',  # noqa: F821
        description='Show/Hide the Pen',
        default=False
    )

    show_trackpad: bpy.props.BoolProperty(
        name='Trackpad',  # noqa: F821
        description='Show/Hide the Trackpad',
        default=False
    )

    show_ndof: bpy.props.BoolProperty(
        name='NDOF',  # noqa: F821
        description='Show/Hide the NDOF (3D Mouse)',
        default=False
    )

    shift: bpy.props.BoolProperty(
        name='Shift',  # noqa: F821
        description='Use Shift Key in Binding',
        default=False
    )

    ctrl: bpy.props.BoolProperty(
        name='Ctrl',  # noqa: F821
        description='Use Ctrl Key in Binding',
        default=True
    )

    alt: bpy.props.BoolProperty(
        name='Alt',  # noqa: F821
        description='Use Alt Key in Binding',
        default=False
    )

    cmd: bpy.props.BoolProperty(
        name='Cmd',  # noqa: F821
        description='Use Cmd Key in Binding',
        default=False
    )
