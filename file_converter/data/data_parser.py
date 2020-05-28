from datetime import datetime
from file_converter.config.config import (
    DATE_FORMAT_INPUT,
    DATE_FORMAT_OUTPUT,
    STRING_TYPE,
    NUMERIC_TYPE,
    DATE_TYPE,
    AVAILABLE_DATA_TYPE,
)


class DataParser:
    """Class in charge of data parsing"""
    @staticmethod
    def format_data(text='', data_type=STRING_TYPE):
        """Format data"""
        if data_type == STRING_TYPE:
            return text.strip()

        if data_type == NUMERIC_TYPE:
            if '.' in text:
                return float(text)
            return int(text)

        if data_type == DATE_TYPE:
            return datetime.strptime(
                text.strip(),
                DATE_FORMAT_INPUT
            ).strftime(DATE_FORMAT_OUTPUT)

        return text

    @staticmethod
    def build_metadata_list(metadata_data=list()):
        """Parse metadata content to build data list"""
        metadata_formatted_list = list()
        for index, row in enumerate(metadata_data):
            m_label, m_length, m_type_data = row.split(',')

            if m_type_data.strip() not in AVAILABLE_DATA_TYPE:
                raise Exception(f'Not available column type {m_type_data}')

            metadata_formatted_list.append({
                'm_label': m_label.strip(),
                'm_length': int(m_length.strip()),
                'm_type': m_type_data.strip(),
            })

        return metadata_formatted_list

    @staticmethod
    def build_content_list(fixed_file_data, metadata_list):
        """Build content using metadata and raw content"""
        result_content = list()
        expected_line_length = sum(int(v['m_length']) for v in metadata_list)

        for row in fixed_file_data:
            line = row.strip()
            if len(line) > expected_line_length:
                raise Exception(
                    f'Different length line, metadata {expected_line_length} \
                        chars vs row {len(line)} chars'
                )

            pointer = 0
            result_line = list()
            for data_hash in metadata_list:
                current_length = data_hash['m_length']
                next_pointer_pos = pointer + current_length
                new_content = line[pointer:next_pointer_pos]
                if not new_content:
                    raise Exception(
                        "Error occurs on parsing file \
                            please verify file content"
                    )

                value = DataParser.format_data(
                    line[pointer:next_pointer_pos],
                    data_hash['m_type']
                )
                # add new content to current line
                result_line.append(value)
                pointer = next_pointer_pos

            # add new line to result content
            result_content.append(result_line)

        return result_content
