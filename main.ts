let right = 0
let left = 0
let buggyon = 0
BitBuggy.init_wheel(AnalogPin.P1, AnalogPin.P2)
let strip = neopixel.create(DigitalPin.P0, 2, NeoPixelMode.RGB)
basic.forever(function on_forever() {
    
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
        buggyon = 1
    })
    input.onButtonPressed(Button.B, function on_button_pressed_b() {
        
        buggyon = 0
    })
    if (buggyon) {
        left = randint(-100, 100)
        right = randint(-100, 100)
        BitBuggy.freestyle(left, right)
        basic.showIcon(IconNames.Silly)
        for (let i = 0; i < 3; i++) {
            strip.showColor(neopixel.colors(NeoPixelColors.Red))
            basic.pause(150)
            strip.showColor(neopixel.colors(NeoPixelColors.Blue))
            basic.pause(150)
        }
    } else {
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        BitBuggy.brake()
        basic.showIcon(IconNames.Heart)
    }
    
})
