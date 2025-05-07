num1 = 0

def when_started1():
    global num1
    num1 = 1750
    while True:
        num1 = num1 + -50
        pen.set_pen_color_rgb(255, 21, 128, 21)
        pen.set_pen_width(MEDIUM)
        pen.move(DOWN)
        drivetrain.drive_for(FORWARD, num1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        pen.set_pen_color_rgb(255, 0, 105, 41)
        drivetrain.drive_for(FORWARD, num1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        pen.set_pen_color_rgb(255, 0, 105, 68)
        drivetrain.drive_for(FORWARD, num1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        pen.set_pen_color_rgb(255, 31, 146, 100)
        drivetrain.drive_for(FORWARD, num1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)

vr_thread(when_started1)
