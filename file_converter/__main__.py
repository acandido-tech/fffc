# -*- coding: utf-8 -*-
"""Main entry of application"""

from argparse import ArgumentParser
from logging import info, error, basicConfig, INFO
from file_converter import app
from file_converter.data.file_checker import FileChecker
from file_converter.config.config import (
    EXPECTED_FIXED_FILE_EXT,
    EXPECTED_METADATA_FILE_EXT
)

# define log level (DEBUG, INFO...)
basicConfig(level=INFO)

def parse_args(args=None):
    """Parse cli arguments"""
    parser = ArgumentParser(description="Convert fixed file to csv file")
    parser.add_argument("-m", "--metadata", help="Metadata path file")
    parser.add_argument("-f", "--file", help="Entry file to convert")

    return parser.parse_args(args)


def main(command_line_arguments=None):
    """Main method in charge of cli args parser"""
    args = parse_args(command_line_arguments)

    metadata_path = args.metadata
    fixed_file_path = args.file
    file_task_list = [
        [metadata_path, EXPECTED_METADATA_FILE_EXT],
        [fixed_file_path, EXPECTED_FIXED_FILE_EXT]
    ]

    try:
        info('#################### Start convertion ######################')
        for file_path_list in file_task_list:
            file_path, file_ext = file_path_list
            file_instance = FileChecker(file_path)
            if not file_instance.is_available(file_ext):
                raise Warning(f'{file_path} is not available')
    except Exception as exception:
        error(exception)
    else:
        # execute converter file
        app.run(metadata_path, fixed_file_path)
        info('#################### Convertion is done ######################')


if __name__ == '__main__':
    main()
