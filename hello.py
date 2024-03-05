class Amir:
    def __init__(self, fname, lname, age, city):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city

    def run(self):
        log = self.fname + " " + self.lname + " " + str(self.age) + " " + self.city
        return log