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
        row.prop(props, 'keymap')
        row.prop(props, 'keymap_item')
        row.prop(props, 'keybind')
        row = box.row()
        row.scale_x = 2
        row.label(text='Show/Hide Onscreen Controls:')
        row.scale_x = 1
        row.prop(props, 'show_keyboard')
        row.prop(props, 'show_mouse')
        row.prop(props, 'show_ndof')

        if props.show_keyboard:
            # Keyboard Section
            key_box = layout.box()
            row = key_box.row()
            row.label(text='Keyboard:')
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
                prop = eval(f"props.k_{i}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i],
                    depress=prop
                )
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
                prop = eval(f"props.k_{i + offset}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + offset],
                    depress=prop
                )
                op.key = key_names[i + offset]

            ### Row 3 - Tab, Q, W
            row = column.row(align=alignment)
            for i in range(row_3):
                if i in (0, (row_3 - 1)):
                    row.scale_x = 1.5
                else:
                    row.scale_x = 1
                offset = row_1 + row_2
                prop = eval(f"props.k_{i + offset}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + offset],
                    depress=prop
                )
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
                prop = eval(f"props.k_{i + offset}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + offset],
                    depress=prop
                )
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
                prop = eval(f"props.k_{i + offset}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + offset],
                    depress=prop
                )
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
                prop = eval(f"props.k_{i + offset}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + offset],
                    depress=prop
                )
                op.key = key_names[i + offset]

            ## Insert Keys
            box = key_row.box()
            box.scale_x = 3
            box.scale_y = 2

            ### F13, F14, F15
            row = box.row(align=alignment)
            for i in range(insert):
                prop = eval(f"props.k_{i + 74}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 74],
                    depress=prop
                )
                op.key = key_names[i + 74]

            ### Spacer row
            row = box.row()

            ### Insert, Home, PageUp
            column = box.column(align=alignment)
            row = column.row(align=alignment)
            for i in range(insert):
                prop = eval(f"props.k_{i + 77}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 77],
                    depress=prop
                )
                op.key = key_names[i + 77]

            ### Delete, End, PageDown
            row = column.row(align=alignment)
            for i in range(insert):
                prop = eval(f"props.k_{i + 80}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 80],
                    depress=prop
                )
                op.key = key_names[i + 80]

            ### Large Spacer row
            row = column.row(align=alignment)
            for i in range(insert):
                row.label(text='')

            ### Up Arrow row
            row = column.row(align=alignment)
            row.label(text='')
            prop = eval(f"props.k_{83}")
            op = row.operator(
                "preferences.keymapper",
                text=key_names[83],
                depress=prop,
                icon='SORT_DESC'
            )
            op.key = key_names[83]
            row.label(text='')

            ### Left, Down, Right Arrow rows
            row = column.row(align=alignment)
            icons = ('BACK', 'SORT_ASC', 'FORWARD')
            for i in range(insert):
                prop = eval(f"props.k_{i + 84}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 84],
                    depress=prop,
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
                prop = eval(f"props.k_{i + 87}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 87],
                    depress=prop
                )
                op.key = f"Numpad {key_names[i + 87]}"

            ### Numpad 7, 8, 9
            row = column.row(align=alignment)
            row.scale_x = 1
            for i in range(numpad):
                prop = eval(f"props.k_{i + 91}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 91],
                    depress=prop
                )
                op.key = f"Numpad {key_names[i + 91]}"

            ### Numpad 4, 5, 6
            row = column.row(align=alignment)
            for i in range(numpad):
                prop = eval(f"props.k_{i + 95}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 95],
                    depress=prop
                )
                op.key = f"Numpad {key_names[i + 95]}"

            ### Numpad 1, 2, 3
            row = column.row(align=alignment)
            for i in range(numpad):
                prop = eval(f"props.k_{i + 99}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 99],
                    depress=prop
                )
                op.key = f"Numpad {key_names[i + 99]}"

            ### Numpad 0, .
            row = column.row(align=alignment)
            for i in range(numpad - 1):
                if i == 0:
                    row.scale_x = 2
                else:
                    row.scale_x = 1
                prop = eval(f"props.k_{i + 103}")
                op = row.operator(
                    "preferences.keymapper",
                    text=key_names[i + 103],
                    depress=prop
                )
                op.key = f"Numpad {key_names[i + 103]}"

        if props.show_mouse:
            row = key_box.row()
            row.label(text='Mouse, Pen & Trackpad:')

            ## Mouse and Tablet Row
            mouse_row = key_box.row(align=alignment)

            ### Mouse Box
            box = mouse_row.box()
            column = box.column(align=alignment)
            row = column.row(align=alignment)
            row.scale_y = 2
            row.operator(
                "preferences.keymapper",
                text="LeftMouse",
                icon='MOUSE_LMB'
            )
            row.operator(
                "preferences.keymapper",
                text="MiddleMouse",
                icon='MOUSE_MMB'
            )
            row.operator(
                "preferences.keymapper",
                text="RightMouse",
                icon='MOUSE_RMB'
            )
            row = column.row(align=alignment)
            for i in range(3):
                row.label(text="")
            row = column.row(align=alignment)
            row.label(text="")
            row.label(text="")
            row.operator(
                "preferences.keymapper",
                text="WheelUp",
                icon='SORT_DESC'
            )
            row.label(text="")
            row.label(text="")
            row = column.row(align=alignment)
            row.label(text="")
            row.operator(
                "preferences.keymapper",
                text="WheelOut",
                icon='REMOVE'
            )
            row.operator(
                "preferences.keymapper",
                text="Move",
                icon='MOUSE_MOVE'
            )
            row.operator(
                "preferences.keymapper",
                text="WheelIn",
                icon='ADD'
            )
            row.label(text="")
            row = column.row(align=alignment)
            row.label(text="")
            row.label(text="")
            row.operator(
                "preferences.keymapper",
                text="WheelDown",
                icon='SORT_ASC'
            )
            row.label(text="")
            row.label(text="")
            row = column.row(align=alignment)
            for i in range(3):
                row.label(text="")
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="Button4")
            row.label(text="")
            row.operator("preferences.keymapper", text="Button5")
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="Button6")
            row.label(text="")
            row.operator("preferences.keymapper", text="Button7")

            ### Spacer
            column = mouse_row.column(align=alignment)
            # column.scale_x = 0.5
            column.label(text='')

            ### Pen Box
            box = mouse_row.box()
            column = box.column(align=alignment)
            column.operator(
                "preferences.keymapper",
                text='Eraser',
                icon='OUTLINER_DATA_GP_LAYER'
            )
            for i in range(7):
                column.label(text='')
            column.operator(
                "preferences.keymapper",
                text='Pen',
                icon='GREASEPENCIL'
            )

            ### Spacer
            column = mouse_row.column(align=alignment)
            # column.scale_x = 0.5
            column.label(text='')

            ### Tablet Box
            box = mouse_row.box()
            box.scale_x = 3
            box.scale_y = 3
            column = box.column(align=alignment)
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Trackpad Pan",
                icon='VIEW_PAN'
            )
            row.scale_x = 0.5
            row.label(text='')
            row.scale_x = 1
            row.operator(
                "preferences.keymapper",
                text="Trackpad Zoom",
                icon='ZOOM_IN'
            )
            row = column.row(align=alignment)
            row.label(text="")
            row.scale_x = 0.5
            row.label(text="")
            row.scale_x = 1
            row.label(text="")
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Trackpad Rotate",
                icon='ORIENTATION_GIMBAL'
            )
            row.scale_x = 0.5
            row.label(text='')
            row.scale_x = 1
            row.operator(
                "preferences.keymapper",
                text="Trackpad Smart Zoom",
                icon='VIEW_ZOOM'
            )

        if props.show_ndof:
            row = key_box.row()
            row.label(text='NDOF (3D Mouse):')

            ## NDOF Row
            ndof_row = key_box.row(align=alignment)
            ndof_row.scale_y = 2

            ### NDOF Button Box
            box = ndof_row.box()
            column = box.column(align=alignment)
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="A")
            row.operator("preferences.keymapper", text="B")
            row.operator("preferences.keymapper", text="C")
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="1")
            row.operator("preferences.keymapper", text="2")
            row.operator("preferences.keymapper", text="3")
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="4")
            row.operator("preferences.keymapper", text="5")
            row.operator("preferences.keymapper", text="6")
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="7")
            row.operator("preferences.keymapper", text="B")
            row.operator("preferences.keymapper", text="9")
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="-")
            row.operator("preferences.keymapper", text="0")
            row.operator("preferences.keymapper", text="+")

            ### NDOF Knob Box
            box = ndof_row.box()
            column = box.column(align=alignment)
            row = column.row(align=alignment)
            for i in range(3):
                row.label(text="")
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Roll CCW",
                icon='LOOP_BACK'
            )
            row.operator(
                "preferences.keymapper",
                text="Rotate",
                icon='ORIENTATION_GIMBAL'
            )
            row.operator(
                "preferences.keymapper",
                text="Roll CW",
                icon='LOOP_FORWARDS'
            )
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Spin CCW",
                icon='LOOP_BACK'
            )
            row.operator(
                "preferences.keymapper",
                text="Motion",
                icon='ORIENTATION_LOCAL'
            )
            row.operator(
                "preferences.keymapper",
                text="Spin CW",
                icon='LOOP_FORWARDS'
            )
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Tilt CCW",
                icon='LOOP_BACK'
            )
            row.operator(
                "preferences.keymapper",
                text="Pan/Zoom",
                icon='VIEW_PAN'
            )
            row.operator(
                "preferences.keymapper",
                text="Tilt CW",
                icon='LOOP_FORWARDS'
            )
            row = column.row(align=alignment)
            for i in range(3):
                row.label(text="")

            ### NDOF View Box
            box = ndof_row.box()
            column = box.column(align=alignment)
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="View 1",
                icon='VIEW_CAMERA'
            )
            row.operator(
                "preferences.keymapper",
                text="View 2",
                icon='VIEW_CAMERA'
            )
            row.operator(
                "preferences.keymapper",
                text="View 3",
                icon='VIEW_CAMERA'
            )
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Iso 1",
                icon='AXIS_FRONT'
            )
            row.operator(
                "preferences.keymapper",
                text="Top",
                icon='TRIA_UP_BAR'
            )
            row.operator(
                "preferences.keymapper",
                text="Iso 2",
                icon='AXIS_SIDE'
            )
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Left",
                icon='TRIA_LEFT_BAR'
            )
            row.operator(
                "preferences.keymapper",
                text="Fit",
                icon='FULLSCREEN_EXIT'
            )
            row.operator(
                "preferences.keymapper",
                text="Right",
                icon='TRIA_RIGHT_BAR'
            )
            row = column.row(align=alignment)
            row.operator(
                "preferences.keymapper",
                text="Front",
                icon='KEYFRAME_HLT'
            )
            row.operator(
                "preferences.keymapper",
                text="Bottom",
                icon='TRIA_DOWN_BAR'
            )
            row.operator(
                "preferences.keymapper",
                text="Back",
                icon='KEYFRAME'
            )
            row = column.row(align=alignment)
            row.operator("preferences.keymapper", text="Dominant")
            row.label(text='')
            row.operator("preferences.keymapper", text="Menu")
