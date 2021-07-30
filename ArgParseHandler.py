import argparse
import os

class ArgParseHandler:

    @staticmethod
    def get_args():
        '''
        :return: arg parser
        '''
        arg_parse = argparse.ArgumentParser()

        # required = False because its optional and not a must.
        arg_parse.add_argument("-r", required=False, help="Regex Expression")
        arg_parse.add_argument("-f", required=False, nargs='+', help="paths to files")
        arg_parse.add_argument("-c", required=False, help="Highlight matching text color")
        arg_parse.add_argument("-m", required=False, help="Generate machine-readable output")
        args = vars(arg_parse.parse_args())
        return args

    @staticmethod
    def get_args_and_files():
        '''
        Verify all args have been init and all files exists.
        :return: args and files paths list
        '''
        args = ArgParseHandler.get_args()

        if args['r'] is None:
            args['r'] = input("Please enter a valid regex expression: ")

        if args['f'] is None:
            files_paths = [item for item in input("Please enter a valid paths for the files: " + os.linesep).split()]
        else:
            files_paths = [item for item in args['f']]

        while True:
            bool_list_all_files_exists = []
            for file in files_paths:
                bool_list_all_files_exists.append(os.path.isfile(file))

            if all(bool_list_all_files_exists):
                # All elements are True. Therefore all the files exist.
                break
            else:
                # At least one element is False. Therefore not all the files exist.
                files_paths = [item for item in input(
                    f"The path you entered does not exist, enter valid paths for the files: {os.linesep}").split()]

        return args, files_paths