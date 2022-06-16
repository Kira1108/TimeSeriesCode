from functools import reduce

def compose(*args):
    def compose_two(f, g):
        return lambda x: g(f(x))
    return reduce(compose_two, args)