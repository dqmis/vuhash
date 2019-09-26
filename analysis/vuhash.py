import os

def hash(str_):
    return os.popen('../vuhash "{}"'.format(str_))

