from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums


class Gate:
    def __init__(self):
        self.is_open = False
    
    def __str__(self):
        return 'open' if self.is_open else 'closed'
    
    def open(self):
        print('opening the gate')
        self.is_open = True
    
    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:
    def __init__(self):
        self.is_open = False
    
    def __str__(self):
        return 'open' if self.is_open else 'closed'
    
    def open(self):
        print('opening the garage')
        self.is_open = True
    
    def close(self):
        print('closing the garage')
        self.is_open = False


class Aircondition:
    def __init__(self):
        self.is_on = False
    
    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the aircondition')
        self.is_on = True
    
    def turn_off(self):
        print('turning off the aircondition')
        self.is_on = False


class Heating:
    def __init__(self):
        self.is_on = False
    
    def __str__(self):
        return 'on' if self.is_on else 'off'
    
    def turn_on(self):
        print('turning on the heating')
        self.is_on = True
    
    def turn_off(self):
        print('turning off the heating')
        self.is_on = False


class Boiler:
    def __init__(self):
        self.temperature = 83
    
    def __str__(self):
        return f'boilder temperature: {self.temperature}'
    
    def increase_temperature(self, amount):
        print(f"increasing the bilder's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the bilder's temperature by {amount} degrees")
        self.temperature -= amount


class Fridge:
    def __init__(self):
        self.temperature = 2
    
    def __str__(self):
        return f'fridge temperature: {self.temperature}'
    
    def increase_temperature(self, amount):
        print(f"increasing the fridge's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the fridge's temperature by {amount} degrees")
        self.temperature -= amount

def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress('->')
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)
    
    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()
    
    tests = ('open -> gate',
             'close -> garage',
             'turn on -> aircondition',
             'turn off -> heating',
             'increase -> boiler temperature -> 5 degress',
             'decrease -> fridge temperature -> 2 degress')
    
    open_actions = {'gate':gate.open, 'garage':garage.open, 'aircondition':airco.turn_on, 'heating':heating.turn_on, 'boiler temperature':boiler.increase_temperature, 
                    'fridge temperature':fridge.increase_temperature} 
    close_actions = {'gate':gate.close, 'garage':garage.close, 'aircondition':airco.turn_off, 'heating':heating.turn_off, 'boiler temperature':boiler.decrease_temperature, 
                     'fridge temperature':fridge.decrease_temperature} 
    for t in tests:
        if len(event.parseString(t)) == 2: # no argument 
            cmd, dev = event.parseString(t) 
            cmd_str, dev_str = ' '.join(cmd), ' '.join(dev) 
            if 'open' in cmd_str or 'turn on' in cmd_str: 
                open_actions[dev_str]() 
            elif 'close' in cmd_str or 'turn off' in cmd_str: 
                close_actions[dev_str]() 
        elif len(event.parseString(t)) == 3: # argument 
            cmd, dev, arg = event.parseString(t) 
            cmd_str, dev_str, arg_str = ' '.join(cmd), ' '.join(dev), ' '.join(arg)
            
            num_arg = 0
            try: 
                num_arg = int(arg_str.split()[0]) # extract the numeric part 
            except ValueError as err: 
                print("expected number but got: '{}'".format(arg_str[0]))

            if 'increase' in cmd_str and num_arg > 0: 
                open_actions[dev_str](num_arg) 
            elif 'decrease' in cmd_str and num_arg > 0: 
                close_actions[dev_str](num_arg)


if __name__ == '__main__':
    main()
