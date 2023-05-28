from subjects import Enum


class Options(Enum):
    math = 1
    history = 2
    programing = 3

    # Access enum members


print(Options.math)
print(Options.math.value)  # the numbers
print(str(Options.math))
print(Options.math.name)  # the string
