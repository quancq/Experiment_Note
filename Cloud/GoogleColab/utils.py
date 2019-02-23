import os
import time
from datetime import datetime


DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_file_names(parent_dir):
    file_names = [file_name for file_name in os.listdir(parent_dir)
                  if os.path.isfile(os.path.join(parent_dir, file_name))]
    return file_names


def mkdirs(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def make_parent_dirs(path):
    dir = path[:path.rfind("/")]
    mkdirs(dir)


def load_str(path):
    data = ""
    try:
        with open(path, 'r') as f:
            data = f.read().strip()
    except:
        print("Error when load str from ", os.path.abspath(path))

    return data


def save_str(data, save_path):
    make_parent_dirs(save_path)
    try:
        with open(save_path, 'w') as f:
            f.write(data)
        print("Save str data to {} done".format(save_path)) 
    except:
        print("Error when save str to ", os.path.abspath(save_path))


def get_time_str(time=datetime.now(), fmt=DEFAULT_TIME_FORMAT):
    try:
        return time.strftime(fmt)
    except:
        return ""
