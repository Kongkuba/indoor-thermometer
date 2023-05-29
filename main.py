def on_received_number(receivedNumber):
    global outdoorTemp
    outdoorTemp = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_number(outdoorTemp)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

outdoorTemp = 0
radio.set_group(23)