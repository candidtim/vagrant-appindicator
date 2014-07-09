import os


def image_path(name):
    """Returns path to the image file by its name"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "%s.png" % name))
