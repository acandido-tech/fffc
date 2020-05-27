class FileChecker:
    """Class in charge of file checking"""

    def __init__(self, file_path):
        self.file_path = file_path

    def __str__(self):
        return self.file_path

    def is_available(self):
        return True
