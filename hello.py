class Amir:
    def __init__(self, fname, lname, age, city):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city

    def run(self):
        log = self.fname + " " + self.lname + " " + str(self.age) + " " + self.city
        return log

my = Amir('karim', 'ahmadi', 19, 'tehran')
my.run()

class Too(Amir):
    def __init__(self, fname, lname, age, city):
        super

x = 10
y = 0
while True:
    y += 1
    print(y)
    if y == x:
        break
    if y == 4:
        print("hello")


print("my name amir ")

print("Ff")

