from collections import OrderedDict
import copy


class Book:
    def __init__(self, name, authors, price, **rest):
        '''Examples of rest: publisher, length, tags, publication date'''
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)
    
    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append(f'{i}: {ordered[i]}')
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def unregister(self, identifier):
        del self.objects[identifier]
    
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f'Incorrect object identifier: {identifier}')
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    b1 = Book('The C Programming Language', ('Biran W. Kernighan', 'Dennis M.Ritchie'), 
              price=119, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structure'))
    
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Lanaguage (ASNI)', price=48.99, length=274,
                         publication_date='1988-04-01', edition=2)
    
    prototype.register('k&r-second', b2)
    
    for i in (b1, b2):
        print(i)
    
    print(f'ID b1: {id(b1)} != ID b2: {id(b2)}')
    
    for key, value in prototype.objects.items():
        print(key)
        print(value)
        print(value.__dict__)


if __name__ == '__main__':
    main()
