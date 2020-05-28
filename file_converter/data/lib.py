from datetime import datetime
from file_converter.config.config import DATE_FORMAT_CSV


def build_file_path(folder_path, filename, ext='txt'):
    """Build file path with adding current time"""
    now = datetime.now()
    final_path = ''.join([
        folder_path,
        filename,
        now.strftime(DATE_FORMAT_CSV),
        '.' + ext,
    ])

    print(final_path)

    return final_path
