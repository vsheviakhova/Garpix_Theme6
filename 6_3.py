class Nicola:
    def __init__(self, age, name='Николай'):
        self.age = age
        if name != 'Николай':
            self.name = f'Я не {name}, а Николай'
        else:
            self.name = name
