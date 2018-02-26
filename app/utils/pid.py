import os


def write():
    with open('pid.file', 'w') as the_file:
        the_file.write(str(os.getpid()))
