from RegexHandler import RegexHandler
from ColorHandler import ColorHandler

class OutPutFormat:

    def __init__(self, file_name, line_num, matched_line=None):
        self.file_name = file_name
        self.line_num = line_num
        self.matched_line = matched_line

    @staticmethod
    def generate_output_format(args, files_paths):
        '''
        generates the output format for matching lines to reg exp
        :param args: argument parser
        :param files_paths: list of files paths
        :return: None
        '''

        # use of re module to re.compile reg exp
        for file in files_paths:
            reg_pattern = RegexHandler.get_regex_pattern(args['r'])
            dict_of_matches = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, file)
            # format = file_name:no_line:matched_text
            for line in dict_of_matches.keys():
                if args['m'] is not None:
                    output_format_obj = OutPutFormat(file, line, dict_of_matches[line])
                    output_format_txt = f"{output_format_obj.file_name}:{output_format_obj.line_num}:{output_format_obj.matched_line}"
                else:
                    output_format_obj = OutPutFormat(file, line)
                    output_format_txt = f"{output_format_obj.file_name}:{output_format_obj.line_num}"

                ColorHandler.print_highlighted_text(args['c'], output_format_txt)


