class Lightbulb:
    def __init__(self, wattage: int, is_led: bool, brand_name: str, brightness: int = 0, is_on: bool = False):
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
        assert 0 <= level <= 10, 'Level outside bounds'
        self.brightness = level


def main():
    phillips_lightbulb = Lightbulb(80, True, "Phillips")
    phillips_lightbulb.to_string()
    phillips_lightbulb.set_brightness(10)
    phillips_lightbulb.turn_on()


if __name__ == "__main__":
    main()
