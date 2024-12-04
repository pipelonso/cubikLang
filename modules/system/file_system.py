import os


class FileSystem:

    def __init__(self):
        pass

    @staticmethod
    def read_file(path) -> str:
        content = open(path, '+r').read()
        return content

    @staticmethod
    def list_files(path):
        try:
            return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        except FileNotFoundError:
            print(f"{path} not found")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    @staticmethod
    def list_folders(path):
        try:
            return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        except FileNotFoundError:
            print(f"{path} Directory not found. ")
            return []
        except Exception as e:
            print(f"ERROR: {e}")
            return []
