radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        Start = true
        Timer = input.runningTime()
    }
})
input.onButtonPressed(Button.AB, function () {
    Start = false
    Movement = 0
    Elapsed = 0
    Timer = 0
    basic.showNumber(Movement)
    basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "stop") {
        Start = false
        Elapsed = input.runningTime() - Timer
        basic.pause(100)
        basic.showString("M=")
        basic.clearScreen()
        basic.showNumber(Movement)
        basic.clearScreen()
        basic.showString("T=")
        basic.clearScreen()
        basic.showNumber(Elapsed / 1000)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
        radio.sendValue("Movement", Movement)
        radio.sendValue("Time", Elapsed / 1000)
    }
})
let is_Down = false
let is_Up = false
let is_South = false
let is_North = false
let is_West = false
let is_East = false
let acc_z = 0
let acc_y = 0
let acc_x = 0
let Elapsed = 0
let Timer = 0
let Movement = 0
let Start = false
Start = false
Movement = 0
basic.showNumber(0)
radio.setGroup(1)
basic.showLeds(`
    . . . . .
    . # . # .
    . . . . .
    . # # # .
    # . . . #
    `)
basic.forever(function () {
    if (Start == true) {
        radio.sendValue("x", input.acceleration(Dimension.X))
        radio.sendValue("y", input.acceleration(Dimension.Z))
        radio.sendValue("z", input.acceleration(Dimension.Y))
    }
})
basic.forever(function () {
    if (Start == true) {
        acc_x = input.acceleration(Dimension.X)
        acc_y = input.acceleration(Dimension.Z)
        acc_z = input.acceleration(Dimension.Y)
        is_East = acc_x > 90
        is_West = acc_x < -90
        is_North = acc_y < -90
        is_South = acc_y > 90
        is_Up = acc_z < 1023
        is_Down = acc_z > -1023
        if (is_East && is_North) {
            basic.showArrow(ArrowNames.NorthEast)
        } else if (is_East && is_South) {
            basic.showArrow(ArrowNames.SouthEast)
        } else if (is_West && is_North) {
            basic.showArrow(ArrowNames.NorthWest)
        } else if (is_West && is_South) {
            basic.showArrow(ArrowNames.SouthWest)
        } else if (is_East) {
            basic.showArrow(ArrowNames.East)
        } else if (is_North) {
            basic.showArrow(ArrowNames.North)
        } else if (is_South) {
            basic.showArrow(ArrowNames.South)
        } else if (is_West) {
            basic.showArrow(ArrowNames.West)
        } else if (is_Up) {
            basic.showLeds(`
                # # . # #
                # . . . #
                . . . . .
                # . . . #
                # # . # #
                `)
        } else if (is_Down) {
            basic.showLeds(`
                . # . # .
                # # . # #
                . . . . .
                # # . # #
                . # . # .
                `)
        } else {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
        }
        if (input.acceleration(Dimension.Strength) > 1000) {
            Movement += 1
        }
    }
})
