import os


def get_first_picture():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, 'pict1.jpg')
    return path
