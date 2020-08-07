right = 0
left = 0
buggyon = 0 
BitBuggy.init_wheel(AnalogPin.P1, AnalogPin.P2)
strip = neopixel.create(DigitalPin.P0, 2, NeoPixelMode.RGB)

def on_button_pressed_a():
    global buggyon
    buggyon = 1

def on_button_pressed_b():
    global buggyon
    buggyon = 0

def on_forever():
    global left, right, buggyon
    input.on_button_pressed(Button.A, on_button_pressed_a)
    input.on_button_pressed(Button.B, on_button_pressed_b)
    if(buggyon):
        left = randint(-100, 100)
        right = randint(-100, 100)
        BitBuggy.freestyle(left, right)
        basic.show_icon(IconNames.SILLY)
        for i in range(3):
            strip.show_color(neopixel.colors(NeoPixelColors.RED))
            basic.pause(150)
            strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
            basic.pause(150)
        
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        BitBuggy.brake()
        basic.show_icon(IconNames.HEART)
    

basic.forever(on_forever)
