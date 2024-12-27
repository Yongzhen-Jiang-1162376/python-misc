from external import Synthesizer, Human


class Computer:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'the {self.name} computer'
    
    def execute(self):
        return 'execute a program'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
    
    def __str__(self):
        return str(self.obj)
    
    @property
    def name(self):
        return self.obj.name


def main():
    
    
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))
    
    for i in objects:
        print(f'{str(i)} {i.execute()}')
    
    for i in objects:
        print(i.name)


if __name__ == '__main__':
    main()
