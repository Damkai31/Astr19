class Fox:
    def __init__(self, arm_length, leg_length, eye_count, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.eye_count = eye_count
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print(f"Arm length: {self.arm_length} meters")
        print(f"Leg length: {self.leg_length} meters")
        print(f"Number of eyes: {self.eye_count}")
        print(f"Has a tail: {self.has_tail}")
        print(f"Is furry: {self.is_furry}")

# Example
my_fox = Fox(0.3, 0.4, 2, True, True)
my_fox.describe()