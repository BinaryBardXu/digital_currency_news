import os


def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)


def is_file_already_exist(file_path):
    return os.path.exists(file_path)


def create_file(file_path):
    f = open(file_path, "w+")
    f.close()
