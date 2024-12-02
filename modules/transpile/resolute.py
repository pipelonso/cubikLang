import sys
import os
from modules.constans.constants import CONF_FILE, FUNCT_EXT
from modules.system.file_system import FileSystem
import json


class Resolute:

    def __init__(self,
                 path: str = ''):

        self.file_system = FileSystem()

        if path.strip() != '':
            self.resolve(path)
        else:
            print("No directory provided.")
        pass

    def resolve(self, path):
        if os.path.exists(path):
            if os.path.exists(os.path.join(path, CONF_FILE)):
                content = self.file_system.read_file(os.path.join(path, CONF_FILE))
                if content.strip() != '':
                    try:
                        keys = json.loads(content)
                        if 'name' in keys:
                            print(f'Project name: {keys["name"]}')
                        if 'version' in keys:
                            print(f'Version: {keys["version"]}')

                        resources_exits = False
                        if 'has_resources' in keys and 'resources' in keys:
                            resources_exits = True
                            print(f'Resources folder provided: {keys["resources"]}')

                            if keys['has_resources']:
                                if keys['resources'].startswith('/'):
                                    keys['resources'] = keys['resources'][1:]

                                if not os.path.exists(os.path.join(path, keys["resources"])):
                                    raise Exception(f"Resources path not found, Full path:"
                                                    f" { os.path.join(path, keys['resources']) } {path}")
                                    pass

                        print(keys)
                    except Exception as e:
                        raise Exception(f"File {CONF_FILE} Error while reading: {e}")
                    pass
                else:
                    raise Exception(f"File {CONF_FILE} could not have a correct format")
                pass
            else:
                raise Exception(f"No {CONF_FILE} file found")
            pass
        else:
            raise Exception(f"Provided directory not found {path}")
        pass
