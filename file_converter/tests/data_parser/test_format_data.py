from file_converter.data.data_parser import DataParser


class TestDataParserFormatData:
    def setup_method(self):
        """Init datas for tests"""
        self.tests_dict_string_list = [
            [['hello,world', 'string'], 'hello,world'],
            [['world', 'string'], 'world'],
            [['   hello', 'string'], 'hello'],
            [['hello   ', 'string'], 'hello'],
            [['  hello   ', 'string'], 'hello'],
        ]

        self.tests_dict_numeric_list = [
            [['123', 'numeric'], 123],
            [['-123', 'numeric'], -123],
            [[' 123', 'numeric'], 123],
            [[' -123', 'numeric'], -123],
            [['123  ', 'numeric'], 123],
            [['-123  ', 'numeric'], -123],
            [['  123 ', 'numeric'], 123],
            [['  -123 ', 'numeric'], -123],
        ]

        self.tests_dict_datetime_list = [
            [['1990-08-22', 'date'], '22/08/1990'],
            [['  1990-08-22', 'date'], '22/08/1990'],
            [['1990-08-22 ', 'date'], '22/08/1990'],
            [[' 1990-08-22    ', 'date'], '22/08/1990'],
        ]

    def _run_loop_on_tests_data(self, data_dict_list):
        for parameters_hash, expected_result in data_dict_list:
            assert DataParser.format_data(
                parameters_hash[0],
                parameters_hash[1]
            ) == expected_result

    def test_data_parser_format_data_string(self):
        self._run_loop_on_tests_data(self.tests_dict_string_list)

    def test_data_parser_format_data_numeric(self):
        self._run_loop_on_tests_data(self.tests_dict_numeric_list)

    def test_data_parser_format_data_datetime(self):
        self._run_loop_on_tests_data(self.tests_dict_datetime_list)

    def test_data_parser_format_data(self):
        assert DataParser.format_data("text ", "bad_type") == 'text '
        assert DataParser.format_data("text") == 'text'
        assert DataParser.format_data() == ''
