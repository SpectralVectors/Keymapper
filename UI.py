import bpy
from . Keyboard_Layouts import (
    key_names,
    row_1,
    row_2,
    row_3,
    row_4,
    row_5,
    row_6,
    insert,
    numpad
)


class KeymapperPanel(bpy.types.Panel):
    """An interactive Keymap Editor"""
    bl_label = "Keymapper"
    bl_idname = "PREFERENCES_PT_keymapper"
    bl_space_type = 'PREFERENCES'
    bl_region_type = 'WINDOW'
    bl_context = "keymap"

    def draw(self, context):
        props = context.scene.keymapper_props

        layout = self.layout

        # Top Box
        box = layout.box()
        row = box.row()
        row.scale_x = 0.7
        row.prop(props, 'category')
        row.scale_x = 1
        row.prop(props, 'operator')

        # Keyboard Section
        key_box = layout.box()
        key_row = key_box.row()

        ## Main Keys
        box = key_row.box()
        box.scale_x = 1
        box.scale_y = 2

        alignment = True

        ### Row 1 - Esc, F1, F2
        row = box.row(align=alignment)
        for i in range(row_1):
            if i in (1, 5, 9):
                row.separator(factor=1.5)
            op = row.operator("preferences.keymapper", text=key_names[i])
            op.key = key_names[i]

        row = box.row()

        column = box.column(align=alignment)
        ### Row 2 - `, 1, 2
        row = column.row(align=alignment)
        for i in range(row_2):
            if i == (row_2 - 1):
                row.scale_x = 2
            else:
                row.scale_x = 1
            offset = row_1
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + offset])
            op.key = key_names[i + offset]

        ### Row 3 - Tab, Q, W
        row = column.row(align=alignment)
        for i in range(row_3):
            if i in (0, (row_3 - 1)):
                row.scale_x = 1.5
            else:
                row.scale_x = 1
            offset = row_1 + row_2
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + offset])
            op.key = key_names[i + offset]

        ### Row 4 - Caps, A, S
        row = column.row(align=alignment)
        for i in range(row_4):
            if i == 0:
                row.scale_x = 1.75
            elif i == (row_4 - 1):
                row.scale_x = 2.25
            else:
                row.scale_x = 1
            offset = row_1 + row_2 + row_3
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + offset])
            op.key = key_names[i + offset]

        ### Row 5 - Shift, Z, X
        row = column.row(align=alignment)
        for i in range(row_5):
            if i == 0:
                row.scale_x = 2.25
            elif i == (row_5 - 1):
                row.scale_x = 2.75
            else:
                row.scale_x = 1
            offset = row_1 + row_2 + row_3 + row_4
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + offset])
            op.key = key_names[i + offset]

        ### Row 6 - Ctrl, OS, Alt
        row = column.row(align=alignment)
        for i in range(row_6):
            if i in (0, (row_6 - 1)):
                row.scale_x = 1.5
            elif i in (2, 4):
                row.scale_x = 1.25
            elif i == 3:
                row.scale_x = 6.5
            else:
                row.scale_x = 1
            offset = row_1 + row_2 + row_3 + row_4 + row_5
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + offset])
            op.key = key_names[i + offset]

        ## Insert Keys
        box = key_row.box()
        box.scale_x = 3
        box.scale_y = 2

        ### F13, F14, F15
        row = box.row(align=alignment)
        for i in range(insert):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 74])
            op.key = key_names[i + 74]

        ### Spacer row
        row = box.row()

        ### Insert, Home, PageUp
        column = box.column(align=alignment)
        row = column.row(align=alignment)
        for i in range(insert):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 77])
            op.key = key_names[i + 77]

        ### Delete, End, PageDown
        row = column.row(align=alignment)
        for i in range(insert):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 80])
            op.key = key_names[i + 80]

        ### Large Spacer row
        row = column.row(align=alignment)
        for i in range(insert):
            row.label(text='')

        ### Up Arrow row
        row = column.row(align=alignment)
        row.label(text='')
        op = row.operator(
            "preferences.keymapper",
            text=key_names[83],
            icon='SORT_DESC'
        )
        op.key = key_names[83]
        row.label(text='')

        ### Left, Down, Right Arrow rows
        row = column.row(align=alignment)
        icons = ('BACK', 'SORT_ASC', 'FORWARD')
        for i in range(insert):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 84],
                icon=icons[i]
            )
            op.key = key_names[i + 84]

        ## Numpad Keys
        box = key_row.box()
        box.scale_x = 3
        box.scale_y = 2

        ### Spacer and alignment rows
        row = box.row()
        row = box.row()
        row.label(text='')

        ### NumLock, /, *
        column = box.column(align=alignment)
        row = column.row(align=alignment)
        for i in range(numpad):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 87])
            op.key = f"Numpad {key_names[i + 87]}"

        ### Numpad 7, 8, 9
        row = column.row(align=alignment)
        row.scale_x = 1
        for i in range(numpad):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 91])
            op.key = f"Numpad {key_names[i + 91]}"

        ### Numpad 4, 5, 6
        row = column.row(align=alignment)
        for i in range(numpad):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 95])
            op.key = f"Numpad {key_names[i + 95]}"

        ### Numpad 1, 2, 3
        row = column.row(align=alignment)
        for i in range(numpad):
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 99])
            op.key = f"Numpad {key_names[i + 99]}"

        ### Numpad 0, .
        row = column.row(align=alignment)
        for i in range(numpad - 1):
            if i == 0:
                row.scale_x = 2
            else:
                row.scale_x = 1
            op = row.operator(
                "preferences.keymapper",
                text=key_names[i + 103])
            op.key = f"Numpad {key_names[i + 103]}"
