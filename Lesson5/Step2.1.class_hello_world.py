import random


class MotorBikes():
    """A object of motor bikes"""

    def __init__(self, bike_list_p=['honda', 'bmw', 'ducati']):
        """初始化FastaIO对象并读取fasta文件"""
        self.bike_list = bike_list_p
        self.speed_dict = {}
        max_speed = 200
        min_speed = 100
        for i in self.bike_list:
            self.speed_dict[i] = random.randint(min_speed, max_speed)

    def set_speed(self, bike, speed):
        """set speed for a given motor bikes with .set_speed('honda', 100)"""
        self.speed_dict[bike] = speed

    def fastest(self):
        """print fastest motor bikes with speed"""
        fastest = ""
        highest_speed = 0
        for i in self.speed_dict:
            if self.speed_dict[i] > highest_speed:
                fastest = i
                highest_speed = self.speed_dict[i]
        output_str = 'Whoa! {} is fastest with speed of {} km/h'.format(fastest, highest_speed)
        return output_str

    def print_all(self):
        """Print all motor bikes available with speed"""
        print("Brand\tSpeed")
        for i in self.speed_dict:
            print("{}\t{}".format(i, self.speed_dict[i]))

    def append(self, new_motor, new_motor_speed=100):
        """Add new motor bikes to this class with default speed of 100"""
        self.speed_dict[new_motor] = new_motor_speed


if __name__ == '__main__':
    test_motor = MotorBikes()
    print("---First Benchmarking---")
    test_motor.print_all()
    print(test_motor.fastest())
    test_motor.append('yamaha', 196)
    print("---Benchmarking After adding yamaha---")
    test_motor.print_all()
    print(test_motor.fastest())
