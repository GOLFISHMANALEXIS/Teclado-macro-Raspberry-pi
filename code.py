import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

boton1_pin= board.GP16
boton2_pin= board.GP17
boton3_pin= board.GP18

teclado = Keyboard(usb_hid.devices)

boton1 = digitalio.DigitalInOut(boton1_pin)
boton1.direction = digitalio.Direction.INPUT
boton1.pull = digitalio.Pull.DOWN

boton2 = digitalio.DigitalInOut(boton2_pin)
boton2.direction = digitalio.Direction.INPUT
boton2.pull = digitalio.Pull.DOWN

boton3 = digitalio.DigitalInOut(boton3_pin)
boton3.direction = digitalio.Direction.INPUT
boton3.pull = digitalio.Pull.DOWN

while True:
    if boton1.value:
        print("Botón 1 Copiar")
        teclado.press(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.C)
    if boton2.value:
        print("Botón 2 Pegar")
        teclado.press(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.V)
    if boton3.value:
        print("Botón 3 Borrar")
        teclado.press(Keycode.BACKSPACE, Keycode.BACKSPACE)
        time.sleep(0.1)
        teclado.release(Keycode.BACKSPACE, Keycode.BACKSPACE)
    time.sleep(0.1)
