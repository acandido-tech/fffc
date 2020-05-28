# -*- coding: utf-8 -*-
"""Testing class for DataParser->buildContentList"""

from pytest import raises
from file_converter.data.data_parser import DataParser
from file_converter.config.config import (
    RESOURCES_PATH,
    FILE_ENCODING_TYPE as f_type
)


class TestDataParserBuildContentData:
    """Class to manage dataParser buildContentData tests"""
    def setup_method(self):
        """Init datas for tests"""
        self.default_metadata_list = [
            {
                'm_label': 'Birth date',
                'm_length': 10,
                'm_type': 'date'
            },
            {
                'm_label': 'First name',
                'm_length': 15,
                'm_type': 'string'
            },
            {
                'm_label': 'Last name',
                'm_length': 15,
                'm_type': 'string'
            },
            {
                'm_label': 'Weight',
                'm_length': 5,
                'm_type': 'numeric'
            }
        ]

        self.tests_build_data_list = [
            [
                [
                    [
                        '1970-01-01John           Smith           81.5\n',
                        '1975-01-31Jane           Doe             61.1\n',
                        '1988-11-28Bob            Big            102.4'
                    ],
                    self.default_metadata_list
                ],
                [
                    ['01/01/1970', 'John', 'Smith', 81.5],
                    ['31/01/1975', 'Jane', 'Doe', 61.1],
                    ['28/11/1988', 'Bob', 'Big', 102.4]
                ]
            ],
            [
                [
                    [
                        '1970-01-01John           Smith\n',
                        '1975-01-31Jane           Doe\n',
                        '1988-11-28Bob            Big'
                    ],
                    [
                        {
                            'm_label': 'Birth date',
                            'm_length': 10,
                            'm_type': 'date'
                        },
                        {
                            'm_label': 'First name',
                            'm_length': 15,
                            'm_type': 'string'
                        },
                        {
                            'm_label': 'Last name',
                            'm_length': 15,
                            'm_type': 'string'
                        },
                    ]
                ],
                [
                    ['01/01/1970', 'John', 'Smith'],
                    ['31/01/1975', 'Jane', 'Doe'],
                    ['28/11/1988', 'Bob', 'Big']
                ]
            ],
        ]

    def _run_loop_on_tests_data(self, data_dict_list):
        for parameters_hash, expected_result in data_dict_list:
            assert DataParser.build_content_list(
                parameters_hash[0],
                parameters_hash[1]
            ) == expected_result

    def test_data_parser_format_data_string(self):
        self._run_loop_on_tests_data(self.tests_build_data_list)

    def test_data_exception(self):
        """Test exception raised for invalid content"""
        file_path = f"{RESOURCES_PATH}/bad_fixed_file.2.txt"
        bad_fixed_file_data = open(file_path, mode='r', encoding=f_type)

        # wrong content length column
        with raises(Exception):
            assert DataParser.build_content_list(
                bad_fixed_file_data,
                self.default_metadata_list
            )

        # wrong nb column
        with raises(Exception):
            assert DataParser.build_content_list(
                [
                    '1970-01-01John           Smith\n',
                    '1975-01-31Jane           Doe             61.1\n',
                    '1988-11-28Bob            Big            102.4'
                ],
                self.default_metadata_list
            )
