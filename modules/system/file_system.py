import os


class FileSystem:

    def __init__(self):
        pass

    @staticmethod
    def read_file(path) -> str:
        content = open(path, '+r').read()
        return content
