import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.street_address = street_address
        self.suite = suite
        self.city = city

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works as {self.address}'


class EmployeeFactory:
    main_office_emp = Employee('', Address('123 East Dr', 0, 'London'))
    aux_office_emp = Employee('', Address('123B East Dr', 0, 'London'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_emp(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_emp,
            name,
            suite
        )

    @staticmethod
    def new_aux_office_emp(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_emp,
            name,
            suite
        )


if __name__ == '__main__':
    john = EmployeeFactory.new_main_office_emp('John', 101)
    jane = EmployeeFactory.new_aux_office_emp('Jane', 500)
    print(john)
    print(jane)