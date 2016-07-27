class Animal:
    def __init__(self, name):
        self.name = name
        self.scream = "Mouaaaaaaa"

    def scream(self):
        print('{} !!!!!'.format(self.scream))
