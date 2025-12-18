class Maths:
    def __init__(self, *numbers):
        self.numbers = numbers

    def my_sum(self):
        total = 0
        for n in self.numbers:
            total = total + n
        print(total)


m = Maths(10, 20, 30, 40)
m.my_sum()
