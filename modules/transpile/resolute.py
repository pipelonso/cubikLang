import sys
import os
from modules.constans.constants import CONF_FILE, FUNCT_EXT
from modules.system.file_system import FileSystem
import json
from modules.transpile.analyzer import Analyzer


class Resolute:

    def __init__(self,
                 path: str = ''):
        sys.tracebacklimit = 5
        self.file_system = FileSystem()
        self.function_path = ''
        self.provided_path = ''

        if path.strip() != '':
            self.resolve(path)
        else:
            print("No directory provided.")
        pass

    def resolve(self, path):
        if os.path.exists(path):
            self.provided_path = path
            if os.path.exists(os.path.join(path, CONF_FILE)):
                content = self.file_system.read_file(os.path.join(path, CONF_FILE))
                if content.strip() != '':
                    try:
                        keys = json.loads(content)
                        if 'name' in keys:
                            print(f'Project name: {keys["name"]}')
                        if 'version' in keys:
                            print(f'Version: {keys["version"]}')
                        print(1)
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
                        if 'functions' in keys:
                            if keys['functions'].startswith('/'):
                                keys['functions'] = keys['functions'][1:]
                            if not os.path.exists(os.path.join(path, keys["functions"])):
                                raise Exception(f"functions path not found, Full path:"
                                                f" {os.path.join(path, keys['functions'])} {path}")
                                pass

                            self.function_path = keys["functions"]
                        else:
                            raise Exception(f"No functions path provided")

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

        self.analyze_function_trace()

        pass

    def analyze_function_trace(self):

        initial_files = self.file_system.list_files(os.path.join(self.provided_path, self.function_path))
        for file in initial_files:

            file_content = self.file_system.read_file(os.path.join(
                    self.provided_path,
                    self.function_path,
                    file
                ))

            analyzer = Analyzer(file_content, file)
            analyzer.analyze_content()

            pass

        pass
