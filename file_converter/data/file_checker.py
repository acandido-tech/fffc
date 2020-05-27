from os.path import isfile


class FileChecker:
    """Class in charge of file checking"""
    DEFAULT_FILE_TYPE_EXT = 'csv'

    def __init__(self, file_path=None):
        self.file_path = file_path

    def __str__(self):
        return self.file_path

    def is_available(self, file_type=DEFAULT_FILE_TYPE_EXT):
        if self.file_path is None:
            raise Exception(
                'Please indicate a path'
            )
        elif isfile(self.file_path) is False:
            raise FileNotFoundError(
                f'Please indicate a correct path : {self.file_path}'
            )

        splitted_file_list = self.file_path.rsplit('.', 1)
        if not splitted_file_list[-1] == file_type:
            raise Exception(
                f'Please use a correct extension file : {file_type}'
            )

        return True
