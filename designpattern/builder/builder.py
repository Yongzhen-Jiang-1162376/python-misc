from enum import Enum
import time


PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDoug = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3          # in seconds for the sake of the example


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
    
    def __str__(self):
        return self.name
    
    def prepare_dough(self, dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} dough of your {self}...')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')
    

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5
    
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
    
    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
    
    def add_topping(self):
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mazzarella, oregano)')
    
    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your margarita for {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('Creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7
    
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDoug.thick)
    
    def add_sauce(self):
        print('adding the creme fraiche sauce to your creamy bacon')
        
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        
        print('done with the creme fraiche sauce')
    
    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham, mushrooms, red onion, organo) to your creamy bacon')
        self.pizza.topping.append([t for t in (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                               PizzaTopping.ham, PizzaTopping.mushrooms,
                                               PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, mushrooms, red_onion, oregano)')
    
    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your creamy bacon for {self.baking_time} seconds')
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter:
    def __init__(self):
        self.builder = None
    
    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]
    
    @property
    def pizza(self):
        return self.builder.pizza
    
    
def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like, [m]armarite or [c]reamy bacon?')
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder)
    
    
def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f'Enjoy your {pizza}')


if __name__ == '__main__':
    main()