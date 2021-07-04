from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# OCP = open for extension, closed for modification

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

# 2 properties --> 3 implementations
# 3 --> 7 c s w cs sw cw csw


# Specification (Enterprise pattern)
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return any(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    bf = BetterFilter()
    # Specifications:
    red = ColorSpecification(Color.RED)
    green = ColorSpecification(Color.GREEN)
    blue = ColorSpecification(Color.BLUE)

    small = SizeSpecification(Size.SMALL)
    medium = SizeSpecification(Size.MEDIUM)
    large = SizeSpecification(Size.LARGE)

    print('Green products (new):')
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('Large products:')
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('Large blue products:')
    large_blue = large & blue
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')

    print('Small or blue products:')
    small_or_blue = small | blue
    for p in bf.filter(products, small_or_blue):
        print(f' - {p.name} is small or blue')