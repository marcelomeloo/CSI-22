class Bird:
    skin = 'feathers'

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} speaks: Fiu Fiu')

    @classmethod
    def get_skin(cls):
        return cls.skin

    @staticmethod
    def get_species():
        return 'bird'
