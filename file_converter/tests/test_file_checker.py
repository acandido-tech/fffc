from pytest import raises
from file_converter.data.file_checker import FileChecker

class TestFileChecker:
    """Test class - File checker"""

    METADATA_FILE_PATH = "ressources/fixed_file_metadata.txt"
    FIXED_FILE_PATH = "ressources/fixed_file.txt"
    NO_EXISTING_FILE_PATH = "ressources/error.txt"
    BAD_METADATA_FILE_PATH = "ressources/bad_fixed_file_metadata.txt"
    BAD_FIXED_FILE_PATH = "ressources/bad_fixed_file_metadata.txt"

    def setup_method(self):
        self.metadata_file = FileChecker(self.METADATA_FILE_PATH)
        self.fixed_file = FileChecker(self.FIXED_FILE_PATH)
        self.no_existing_file = FileChecker(self.NO_EXISTING_FILE_PATH)
        self.bad_metadata_file = FileChecker(self.BAD_METADATA_FILE_PATH)
        self.bad_fixed_file = FileChecker(self.BAD_FIXED_FILE_PATH)

    def test_file_availability(self):
        """ Test description """
        assert self.metadata_file.is_available()
        assert self.fixed_file.is_available()

    def test_file_exception(self):
        """test that exception is raised for invalid file path and content"""
        with raises(FileNotFoundError):
            assert self.no_existing_file.is_available()

        with raises(Exception):
            assert self.bad_metadata_file.is_available()

        with raises(Exception):
            assert self.bad_fixed_file.is_available()
