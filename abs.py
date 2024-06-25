"""
abs - Absolute Method to Return Absolute Value, Takes INT<FLOAT<COMPLEX as parameter
Return Absolute Value of int, float -> convert signed values into non-signed values
for working with list use map function
in case of complex number return magnitude of the literal integer -> sqrt of x^2 + y^2
"""
# a:int
a = 1
# b: float
b = 1.2
# c: complex
c = 1+6j
# d: list -> TypeError
d = [1, -1, 6.7, -6.7, 7+7j, -7+7j]
# e: str -> TypeError
e = 'hi'

# using abs function on the  following variables
print(type(a), abs(a))
print(type(b), abs(b))
print(type(c), abs(c))
# print(type(d), abs(d))
# for List Implementation use map function
print(type(d), list(map(abs, d)))
# print(type(e), abs(e))

