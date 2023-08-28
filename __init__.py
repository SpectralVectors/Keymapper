import bpy
from . UI import KeymapperPanel
from . Properties import KeymapperProperties

bl_info = {
    "name": "Keymapper",
    "author": "Spectral Vectors",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Preferences > Keymap",
    "description": "Graphical Keymap Editor",
    "warning": "Under Development > UI mockup",
    "doc_url": "",
    "category": "Interface",
}


classes = [
    KeymapperPanel,
    KeymapperProperties,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.keymapper_props = bpy.props.PointerProperty(
        type=KeymapperProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__package__":
    register()
