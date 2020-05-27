# -*- coding: utf-8 -*-
from file_converter import app
from argparse import ArgumentParser
from logging import info, error, basicConfig, INFO
from file_converter.data.file_checker import FileChecker

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

    METADATA = args.metadata
    FILE = args.file

    try:
        info('#################### Start convertion ######################')
        for file_path in [METADATA, FILE]:
            file_instance = FileChecker(file_path)
            if not file_instance.is_available():
                raise Warning(f'{file_path} is not available')
                break
    except Exception as exception:
        error(exception)
    else:
        # execute converter file
        app.run(METADATA, FILE)
        info('#################### Convertion is done ######################')


if __name__ == '__main__':
    main()
