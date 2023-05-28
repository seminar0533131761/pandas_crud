from enum import Enum



class MyEnum(Enum):

    en = 1
    he = 2
    pro = 3
    gram = 4
    hist = 5
    grfic = 6


def get_subject():
    """return all the subjects that allowed"""
    return [member.name for member in MyEnum]
