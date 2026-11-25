class Measurement:
    def __init__(self, meters):
        self.meters = meters

    @classmethod
    def from_centimeters(cls, value):
        return cls(value / 100)


print("meters:", Measurement.from_centimeters(250).meters)