import unittest
from file_watcher.pdf_reader import read_pdf
import os
from reportlab.pdfgen import canvas

class TestPDFReader(unittest.TestCase):

    def setUp(self):
        # Create a sample PDF file with actual text content for testing
        self.sample_pdf_path = "sample.pdf"
        self.create_sample_pdf(self.sample_pdf_path)

    def tearDown(self):
        # Cleanup the test file
        if os.path.exists(self.sample_pdf_path):
            os.remove(self.sample_pdf_path)

    def create_sample_pdf(self, file_path):
        # Use reportlab to generate a simple PDF with text
        c = canvas.Canvas(file_path)
        c.drawString(100, 750, "This is a sample PDF file for testing.")
        c.save()



    def test_read_pdf_success(self):
        # Test successful extraction of text (for simplicity, we're just testing if it handles a basic PDF)
        result = read_pdf(self.sample_pdf_path,self._sample_callback)
        self.assertTrue(result)  # Ensure text is not None

    def test_read_pdf_invalid_file(self):
        # Test handling of invalid or non-existing PDF files
        result = read_pdf("non_existing_file.pdf", self._sample_callback)
        self.assertFalse(result)

    def _sample_callback(self,text, data):
        print(f"{text} and {data}")

if __name__ == "__main__":
    unittest.main()
