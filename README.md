# Keymapper
Experimental Keymap GUI for Blender
![Keymapper](/Keymapper.png)
### Star, Fork, create Issues and Pull Requests if you want to contribute!
## Inspiration
Editing keymaps in Blender can be a chore, and Blender won't tell you if there is a conflict with an existing keybind.
Many people in the Blender community have noticed and suggested solutions:
- [Right Click Select - Visual Hotkey Input Editor](https://blender.community/c/rightclickselect/nqdbbc/)
- [Right Click Select - New Keyboard Mapping UI](https://blender.community/c/rightclickselect/glgbbc/)
- [Right Click Select - Visual Shortcut Editor](https://blender.community/c/rightclickselect/BKbbbc/)
Some have created addons to help with the process:
- [IsKeyFree?](https://docs.blender.org/manual/en/latest/addons/development/is_key_free.html)
- [Keyboard Layout SVG](https://code.it4i.cz/blender/blender-addons-contrib/-/blob/26a8b2eadc7abb2a30fac50eb5505aa24daf5785/system_keyboard_svg.py)
However, [official attempts to update this within Blender have been stuck at an impasse for 3 years!](https://projects.blender.org/blender/blender/issues/76678#987855)
## The Goal
The goal of this addon is to implement as much of the desired visual hotkey editing/conflict checking as possible with Python.

There will be limitations with this approach, but the hope is that this addon can provide a template for an official implementation within Blender.
