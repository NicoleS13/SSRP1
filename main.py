def on_received_number(receivedNumber):
    global Start, Timer
    if receivedNumber == 1:
        Start = True
        Timer = input.running_time()
radio.on_received_number(on_received_number)

def on_button_pressed_ab():
    global Start, Movement, Elapsed, Timer
    Start = False
    Movement = 0
    Elapsed = 0
    Timer = 0
    basic.show_number(Movement)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global Start, Elapsed
    if receivedString == "stop":
        Start = False
        Elapsed = input.running_time() - Timer
        basic.pause(100)
        basic.show_string("M=")
        basic.clear_screen()
        basic.show_number(Movement)
        basic.clear_screen()
        basic.show_string("T=")
        basic.clear_screen()
        basic.show_number(Elapsed / 1000)
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
        radio.send_value("Movement", Movement)
        radio.send_value("Time", Elapsed / 1000)
radio.on_received_string(on_received_string)

is_Down = False
is_Up = False
is_South = False
is_North = False
is_West = False
is_East = False
acc_z = 0
acc_y = 0
acc_x = 0
Elapsed = 0
Timer = 0
Movement = 0
Start = False
Start = False
Movement = 0
basic.show_number(0)
radio.set_group(1)
basic.show_leds("""
    . . . . .
    . # . # .
    . . . . .
    . # # # .
    # . . . #
    """)

def on_forever():
    if Start == True:
        radio.send_value("x", input.acceleration(Dimension.X))
        radio.send_value("y", input.acceleration(Dimension.Z))
        radio.send_value("z", input.acceleration(Dimension.Y))
basic.forever(on_forever)

def on_forever2():
    global acc_x, acc_y, acc_z, is_East, is_West, is_North, is_South, is_Up, is_Down, Movement
    if Start == True:
        acc_x = input.acceleration(Dimension.X)
        acc_y = input.acceleration(Dimension.Z)
        acc_z = input.acceleration(Dimension.Y)
        is_East = acc_x > 90
        is_West = acc_x < -90
        is_North = acc_y < -90
        is_South = acc_y > 90
        is_Up = acc_z < 1023
        is_Down = acc_z > -1023
        if is_East and is_North:
            basic.show_arrow(ArrowNames.NORTH_EAST)
        elif is_East and is_South:
            basic.show_arrow(ArrowNames.SOUTH_EAST)
        elif is_West and is_North:
            basic.show_arrow(ArrowNames.NORTH_WEST)
        elif is_West and is_South:
            basic.show_arrow(ArrowNames.SOUTH_WEST)
        elif is_East:
            basic.show_arrow(ArrowNames.EAST)
        elif is_North:
            basic.show_arrow(ArrowNames.NORTH)
        elif is_South:
            basic.show_arrow(ArrowNames.SOUTH)
        elif is_West:
            basic.show_arrow(ArrowNames.WEST)
        elif is_Up:
            basic.show_leds("""
                # # . # #
                # . . . #
                . . . . .
                # . . . #
                # # . # #
                """)
        elif is_Down:
            basic.show_leds("""
                . # . # .
                # # . # #
                . . . . .
                # # . # #
                . # . # .
                """)
        else:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        if input.acceleration(Dimension.STRENGTH) > 1000:
            Movement += 1
basic.forever(on_forever2)
