#!/usr/bin/env python3

numbers = list(range(1, 6))
for i in numbers:
    print(i * i)

# e.g, JavaScrip
# print(map((i) => i * i, [1, 2, 3, 4, 5]))

functional = map(lambda x: x * x, list(range(1, 6)))
print(functional)
