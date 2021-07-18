class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    i = 0
    def create_person(self, name):
        # todo
        p = Person(PersonFactory.i, name)
        PersonFactory.i += 1
        return p


if __name__ == '__main__':
    pf = PersonFactory()
    alex = pf.create_person('Alex')
    print(alex.id)
    scarlett = pf.create_person('Scarlett')
    print(scarlett.id)