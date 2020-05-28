# -*- coding: utf-8 -*-
"""App execution"""

from csv import writer
from file_converter.data.data_parser import DataParser
from file_converter.config.config import (
    FILE_ENCODING_TYPE as f_type,
    PUBLIC_CSV_PATH,
    CONVERTED_FILE_EXT,
    DELIMITER_FILE_OUTPUT,
)
from file_converter.data.lib import build_file_path


def run(metadata_path, file_path):
    """application main method in charge to convert file in csv"""
    metadata_data = open(metadata_path, mode='r', encoding=f_type)
    metadata_list = DataParser.build_metadata_list(metadata_data)

    fixed_file_data = open(file_path, mode='r', encoding=f_type)
    result_content_list = DataParser.build_content_list(
        fixed_file_data,
        metadata_list
    )

    with open(
            build_file_path(
                PUBLIC_CSV_PATH,
                '/converted_file',
                CONVERTED_FILE_EXT
            ),
            'w',
            encoding=f_type,
            newline='\n',
    ) as csvfile:
        filewriter = writer(csvfile, delimiter=DELIMITER_FILE_OUTPUT)

        # create header on first line
        filewriter.writerow(list(i['m_label'] for i in metadata_list))

        # create content
        for data in result_content_list:
            filewriter.writerow(data)

        csvfile.close()
