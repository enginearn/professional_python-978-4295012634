#!/usr/bin/env python3

from functools import reduce
from functools import partial

import plotly.graph_objects as pgo

# functional
functional_squares = map(lambda x: x * x, list(range(1, 6)))
functional_should = reduce(lambda x, y: x and y, [True, True, True])
functional_evens = filter(lambda x: x % 2 == 0, list(range(1, 6)))

print(functional_squares)
print(functional_should)
print(functional_evens)

# procedural
procedural_squares = [x * x for x in list(range(1, 6))]
procedural_should = all([True, True, True])
procedural_evens = [x for x in list(range(1, 6)) if x % 2 == 0]

print(procedural_squares)
print(procedural_should)
print(procedural_evens)


def pow(x: int, power: int = 1) -> int:
    return x ** power

square = partial(pow, power=2)
cube = partial(pow, power=3)

print(square(3))
print(cube(9))

# declarative
trace = pgo.Scatter(
    x = [1, 2, 3],
    y = [4, 5, 6],
    marker = {'color': 'red', 'symbol': 104},
    mode = 'markers+lines',
    text = ['one', 'two', 'three'],
    name = 'Trace'
)

