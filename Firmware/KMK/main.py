# DEAD CODE, NOT DONE!

print("Hackpad Testing!")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Extra features
from kmk.extensions.RGB import RGB


print(dir(board))

keyboard = KMKKeyboard()
keyboard.col_pins = (board.GP26, board.GP27,board.GP28)
keyboard.row_pins = (board.GP3, board.GP4, board.GP2)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB imports
rgb = RGB(pixel_pin=board.GP29, num_pixels=4)
keyboard.extensions.append(rgb)

# TODO: add OLED display



keyboard.keymap = [
    [

        KC.F, KC.U, KC.C,
        KC.K, KC.G, KC.W,
        KC.O, KC.DOT, KC.P,
    ]
]


if __name__ == '__main__':
    keyboard.go()