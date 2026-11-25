class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(value):
        return value * 9 / 5 + 32


print("20 C in F:", Temperature.celsius_to_fahrenheit(20))