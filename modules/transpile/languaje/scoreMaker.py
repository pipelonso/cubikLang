from modules.exceptions.SyntaxErrorException import SyntaxErrorException
import sys
import re


class ScoreMaker:

    def __init__(self, line: str, index: int, file_name: str):
        self.score_line = line
        self.line_index = index
        self.file_name = ''
        pass

    def determine_score(self):
        pattern = r'^score\s+(\w+)\s*(?:"([^"]*)")?\s*:?\s+(\w+)\s*(?:=\s*(\d+)\s*->\s*(@[a-z]+\[.*\]|@[a-z]+))?\s*;$'
        match = re.match(pattern, self.score_line)

        if not match:
            if not self.score_line.startswith('score'):
                raise SyntaxErrorException(f"The line needs to begin with score, Line {self.line_index} :"
                                           f" {self.score_line}")
            if '=' in self.score_line and '->' not in self.score_line:
                raise SyntaxErrorException(
                    f"If you assign a value to the score, specify the user using -> @user. Line: {self.line_index} : "
                    f"{self.score_line} at the file : {self.file_name}"
                )
            if re.search(r':\s*$', self.score_line):
                raise SyntaxErrorException(f"Missing score type after ':', Line {self.line_index} : {self.score_line}"
                                           f" at the file : {self.file_name}")
            raise SyntaxErrorException(f"The line does not match a correct format. Line {self.line_index} : "
                                       f"{self.score_line} at the file : {self.file_name}")

        score_name = match.group(1)
        display_name = match.group(2) if match.group(2) else None
        score_type = match.group(3)
        score_value = int(match.group(4)) if match.group(4) else None
        score_user = match.group(5) if match.group(5) else None

        built_in = f'scoreboard objectives add {score_name} {score_type}'
        if display_name is not None:
            built_in += f' "{score_name}"'
        if score_value is not None:
            built_in += '\n'
            built_in += f'scoreboard players set {score_user} {score_name} {score_value}'

        return built_in

        pass
