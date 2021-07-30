from OutPutFormat import OutPutFormat
from ArgParseHandler import ArgParseHandler


if __name__ == "__main__":
    args, file_paths = ArgParseHandler.get_args_and_files()
    OutPutFormat.generate_output_format(args, file_paths)
