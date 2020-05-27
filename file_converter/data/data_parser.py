from datetime import datetime
from file_converter.config.config import DATE_FORMAT_INPUT, DATE_FORMAT_OUTPUT


class DataParser:
    """Class in charge of data parsing"""
    STRING_TYPE = 'string'
    NUMERIC_TYPE = 'numeric'
    DATE_TYPE = 'date'

    @staticmethod
    def format_data(text='', data_type=STRING_TYPE):
        """Format data"""
        if data_type == DataParser.STRING_TYPE:
            return text.strip()

        if data_type == DataParser.NUMERIC_TYPE:
            if '.' in text:
                return float(text)
            return int(text)

        if data_type == DataParser.DATE_TYPE:
            return datetime.strptime(
                text.strip(),
                DATE_FORMAT_INPUT
            ).strftime(DATE_FORMAT_OUTPUT)

        return text
