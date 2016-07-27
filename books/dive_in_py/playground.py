#! /usr/bin/python3

class Animal():

    def __init__(self, nLimbs, name):
        self.nLimbs = nLimbs
        self.name = name
        pass

    # Starting a method, function or attribute by "__" makes it private
    def __printSpace(self):
        report = "{0}: {1} Limbs".format(self.name, self.nLimbs)
        print(report)
    
    def __printTab(self):
        report = "{0}:\t{1} Limbs".format(self.name, self.nLimbs)
        print(report)

    def report(self, method):
        # Using getattr as a dispatcher
        # Allows to pass the name of a method as a string (see main)
        # Allows also to have a default (3rd arg) in case not correct input
        getattr(self, method, self.__printSpace)()

class Bird(Animal):
    # Example of inheritance
    def sing(self):
        print("Twwwweeeeet")

class Mydict(dict):
    # Overiding example
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, str(value) + "ahah")
        
if __name__ == "__main__":
    bird = Bird(3, "RadioBirdy")
    bird.report("__printTab")
    bird.sing()
    a=Mydict()
    a["test"] = 12
    print(a)
    
