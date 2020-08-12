class GreetUser:
    def __init__(self, input_name, input_name2):
        """"Construct a GreetUser object with given user_name"""
        self.name = input_name
        self.name2 = input_name2

    def greet(self):
        print("Hi" + self.name + self.name2)

    def numm(self):
        print("I'm OK")

    def greet2(self):
        print("Hi", self.name2)


new_object = GreetUser('foo', 'bar')

new_object.greet()

new_object.numm()
