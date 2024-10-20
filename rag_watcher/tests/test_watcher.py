# test_watcher.py
import unittest
from unittest.mock import patch, MagicMock
from watchdog.events import FileCreatedEvent
from file_watcher.watcher import FileHandler, watch_directory, default_callback

class TestFileHandler(unittest.TestCase):

    @patch('file_watcher.watcher.read_pdf')
    @patch('file_watcher.watcher.move_file')
    def test_on_created_pdf_file(self, mock_move_file, mock_read_pdf):
        # Arrange
        directory = "/test/directory"
        callback = MagicMock()
        handler = FileHandler(directory, callback)

        # Create a mock event for a PDF file creation
        event = FileCreatedEvent("/test/directory/test.pdf")
        
        # Act
        handler.on_created(event)

        # Assert
        mock_read_pdf.assert_called_once_with("/test/directory/test.pdf", callback)
        mock_move_file.assert_called_once_with("/test/directory/test.pdf")

    @patch('file_watcher.watcher.read_pdf')
    @patch('file_watcher.watcher.move_file')
    def test_on_created_non_pdf_file(self, mock_move_file, mock_read_pdf):
        # Arrange
        directory = "/test/directory"
        callback = MagicMock()
        handler = FileHandler(directory, callback)

        # Create a mock event for a non-PDF file creation
        event = FileCreatedEvent("/test/directory/test.txt")
        
        # Act
        handler.on_created(event)

        # Assert
        mock_read_pdf.assert_not_called()
        mock_move_file.assert_not_called()

    @patch('file_watcher.watcher.read_pdf')
    @patch('file_watcher.watcher.move_file')
    def test_on_created_directory(self, mock_move_file, mock_read_pdf):
        # Arrange
        directory = "/test/directory"
        callback = MagicMock()
        handler = FileHandler(directory, callback)

        # Create a mock event for a directory creation
        event = FileCreatedEvent("/test/directory/new_directory")
        event.is_directory = True
        
        # Act
        handler.on_created(event)

        # Assert
        mock_read_pdf.assert_not_called()
        mock_move_file.assert_not_called()


class TestWatchDirectory(unittest.TestCase):

    @patch('file_watcher.watcher.Observer')
    @patch('file_watcher.watcher.FileHandler')
    def test_watch_directory(self, mock_file_handler, mock_observer):
        # Arrange
        directory = "/test/directory"
        callback = MagicMock()

        # Act
        with patch('time.sleep', return_value=None):  # To prevent an infinite loop
            watch_directory(directory, callback)

        # Assert
        mock_file_handler.assert_called_once_with(directory, callback)
        mock_observer().schedule.assert_called_once_with(mock_file_handler(), directory, recursive=False)
        mock_observer().start.assert_called_once()


class TestDefaultCallback(unittest.TestCase):

    def test_default_callback(self):
        # Arrange
        text_chunk = "Sample text from PDF"
        metadata = {}

        # Capture the printed output
        with patch('builtins.print') as mocked_print:
            # Act
            default_callback(text_chunk, metadata)

            # Assert
            mocked_print.assert_called_with("Implement Callback")


if __name__ == '__main__':
    unittest.main()

