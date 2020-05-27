from os.path import isfile


class FileChecker:
    """Class in charge of file checking"""

    def __init__(self, file_path=None):
        self.file_path = file_path

    def __str__(self):
        return self.file_path

    def is_available(self):
        if self.file_path is None:
            raise Exception(
                'Please indicate a path'
            )
        elif isfile(self.file_path) is False:
            raise FileNotFoundError(
                f'Please indicate a correct path : {self.file_path}'
            )

        return True
