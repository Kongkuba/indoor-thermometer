radio.onReceivedNumber(function (receivedNumber) {
    outdoorTemp = receivedNumber
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(outdoorTemp)
    basic.showString("Spa")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Inde")
})
let outdoorTemp = 0
radio.setGroup(23)
