import bpy
from . UI import KeymapperPanel
from . Properties import KeymapperProperties
from . Operators import KeymapperOperator

bl_info = {
    "name": "Keymapper",
    "author": "Spectral Vectors",
    "version": (0, 0, 9),
    "blender": (2, 80, 0),
    "location": "Preferences > Keymap",
    "description": "Graphical Keymap Editor",
    "warning": "Under Development > UI mockup",
    "doc_url": "",
    "category": "Interface",
}


classes = [
    KeymapperOperator,
    KeymapperProperties,
    KeymapperPanel
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.keymapper_props = bpy.props.PointerProperty(
        type=KeymapperProperties)

    bpy.types.Scene.keymaps = []
    bpy.types.Scene.keymap_items = []


def unregister():
    del bpy.types.Scene.keymapper_props
    del bpy.types.Scene.keymaps
    del bpy.types.Scene.keymap_items

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__package__":
    register()
