from modules.transpile.languaje.scoreMaker import ScoreMaker


class Analyzer:

    def __init__(self,
                 file_content: str,
                 file_name: str
                 ):

        self.file_content = file_content
        self.file_name = file_name
        pass

    def analyze_content(self):

        built_in_line = ''
        per_line = self.file_content.split('\n')
        for (index, line) in enumerate(per_line):
            if line.strip() != '':
                split_line = line.split(' ')
                if split_line[0] == 'score':
                    score_maker = ScoreMaker(line, index, self.file_name)
                    print(score_maker.determine_score())


        pass
