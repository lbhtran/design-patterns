# ISP


# bad ideas
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


# works for this
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# but not for this
class OldFashionedPrinter(Machine):
    def print(self, document):
        # here, it is ok
        pass

    def fax(self, document):
        # this printer doesn't have this
        pass

    def scan(self, document):
        # or this
        raise NotImplementedError('Printer cannot scan!')


# Better implementation
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Fax, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, fax, scanner):
        self.scanner = scanner
        self.printer = printer
        self.fax = fax

    def print(self, document):
        self.printer.print(document)

    def fax(self, document):
        self.fax.fax(document)

    def scan(self, document):
        self.scanner.scan(document)