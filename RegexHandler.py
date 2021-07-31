import re


class RegexHandler:

    @staticmethod
    def get_regex_pattern(reg_exp):
        '''
        :param reg_exp: regex expression
        :return: returns a regex patterm
        '''
        try:
            return re.compile(reg_exp)
        except Exception as e:
            print(f"Error in get_regex_pattern - {e} ")

    @staticmethod
    def get_lines_matching_reg_pattern_in_txt_file(reg_pattern, txt_file_path):
        '''
        :param reg_pattern: regex pattern
        :param txt_file_path: file path
        :return: dict of matches by regex per line
        '''
        dict_of_matches_per_line = {}
        try:
            for i, line in enumerate(open(txt_file_path)):
                for match in re.finditer(reg_pattern, line):
                    dict_of_matches_per_line[i + 1] = match.group()
            return dict_of_matches_per_line
        except FileNotFoundError:
            return FileNotFoundError