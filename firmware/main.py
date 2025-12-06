import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

# Custom key names
KEY1 = KC.KEY1
KEY2 = KC.KEY2
KEY3 = KC.KEY3
KEY4 = KC.KEY4
KEY5 = KC.KEY5
KEY6 = KC.KEY6

# Pin → Key mapping
pin_key_map = {
    board.D3: KEY1,
    board.D4: KEY2,
    board.D1: KEY3,
    board.D0: KEY4,
    board.D2: KEY5,
    board.D7: KEY6,
}

# Configure each pin as input with pull-up
for pin in pin_key_map.keys():
    sw = digitalio.DigitalInOut(pin)
    sw.switch_to_input(pull=digitalio.Pull.UP)

# Assign mapping to keyboard
keyboard.pins = pin_key_map

if __name__ == "__main__":
    while True:
        keyboard.poll()
