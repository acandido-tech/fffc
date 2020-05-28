from pytest import raises
from file_converter.config.config import (
    RESOURCES_PATH,
    FILE_ENCODING_TYPE as f_type
)
from file_converter.data.data_parser import DataParser


class TestDataParserMetadata:
    METADATA_FILE_PATH = f"{RESOURCES_PATH}/fixed_file_metadata.csv"
    OTHER_METADATA_FILE_PATH = f"{RESOURCES_PATH}/fixed_file_metadata.2.csv"

    def setup_method(self):
        """Init datas for tests"""
        self.tests_metadata_formatter_list = [
            [
                self.METADATA_FILE_PATH, [
                    {
                        'm_label': 'Birth date',
                        'm_length': '10',
                        'm_type': 'date'
                    },
                    {
                        'm_label': 'First name',
                        'm_length': '15',
                        'm_type': 'string'
                    },
                    {
                        'm_label': 'Last name',
                        'm_length': '15',
                        'm_type': 'string'
                    },
                    {
                        'm_label': 'Weight',
                        'm_length': '5',
                        'm_type': 'numeric'
                    }
                ]
            ],
            [
                self.OTHER_METADATA_FILE_PATH, [
                    {
                        'm_label': 'Birth date',
                        'm_length': '12',
                        'm_type': 'date'
                    },
                    {
                        'm_label': 'First name',
                        'm_length': '11',
                        'm_type': 'string'
                    },
                    {
                        'm_label': 'Last name',
                        'm_length': '15',
                        'm_type': 'string'
                    },
                    {
                        'm_label': 'Weight',
                        'm_length': '2',
                        'm_type': 'numeric'
                    },
                    {
                        'm_label': 'City code',
                        'm_length': '3',
                        'm_type': 'string'
                    },
                    {
                        'm_label': 'Country code',
                        'm_length': '3',
                        'm_type': 'string'
                    },
                    {
                        'm_label': 'Iata',
                        'm_length': '3',
                        'm_type': 'numeric'
                    }
                ]
            ],
        ]

    def _run_loop_on_tests_data(self, data_dict_list):
        for file_path, expected_result in data_dict_list:
            metadata_data = open(file_path, mode='r', encoding=f_type)
            assert DataParser.build_metadata_list(
                metadata_data
            ) == expected_result

    def test_data_parser_build_metadata_list(self):
        self._run_loop_on_tests_data(self.tests_metadata_formatter_list)

    def test_data_parser_build_metadata_exceptoin(self):
        """Test exception raised for invalid file type column"""
        with raises(Exception):
            assert DataParser.build_metadata_list(
                [
                    'Birth date,10,date\n',
                    'Other value,15,new_type\n',
                ]
            )
