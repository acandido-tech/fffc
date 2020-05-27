from pytest import raises
from file_converter.config.config import RESOURCES_PATH
from file_converter.data.file_checker import FileChecker


class TestFileChecker:
    METADATA_FILE_PATH = f"{RESOURCES_PATH}/fixed_file_metadata.csv"
    FIXED_FILE_PATH = f"{RESOURCES_PATH}/fixed_file.txt"
    NO_EXISTING_FILE_PATH = f"{RESOURCES_PATH}/error.txt"

    def setup_method(self):
        """Init datas for tests"""
        self.metadata_file = FileChecker(self.METADATA_FILE_PATH)
        self.fixed_file = FileChecker(self.FIXED_FILE_PATH)
        self.no_existing_file = FileChecker(self.NO_EXISTING_FILE_PATH)
        self.no_path = FileChecker()

    def test_file_availability(self):
        """Test with correct file path and content"""
        assert self.metadata_file.is_available()
        assert self.fixed_file.is_available()

    def test_file_exception(self):
        """Test exception raised for invalid file path and content"""
        with raises(FileNotFoundError):
            assert self.no_existing_file.is_available()
        with raises(Exception):
            assert self.no_path.is_available()
