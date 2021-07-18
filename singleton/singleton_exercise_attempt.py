def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    f1 = factory()
    f2 = factory()
    return f1 is f2
