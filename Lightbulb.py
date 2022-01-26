class Lightbulb:
    def __init__(self, wattage, is_led, brand_name, brightness, is_on=False):
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.brightness = brightness
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def to_string(self):
        print(f"Wattage: {self.wattage}W\nBrand name: {self.brand_name}")
        if self.is_led:
            print("LED")

    def set_brightness(self, level):
        self.brightness = level


def main():
    phillips_lightbulb = Lightbulb(80, True, "Phillips", 10)
    phillips_lightbulb.to_string()


if __name__ == "__main__":
    main()
