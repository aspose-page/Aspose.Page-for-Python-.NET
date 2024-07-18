from aspose.page.xps import *
from aspose.page.xps.presentation.pdf import *
from util import Util

class XPStoPDF:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_conversion()

        # Initialize PDF output stream
        with open(data_dir + "XPStoPDF_out.pdf", "wb") as pdf_stream:
            # Load XPS document form the file
            document = XpsDocument(data_dir + "input.xps", XpsLoadOptions())

            # Initialize options object with necessary parameters.
            options = PdfSaveOptions()

            options.jpeg_quality_level = 100
            options.image_compression = PdfImageCompression.JPEG
            options.text_compression = PdfTextCompression.FLATE
            options.page_numbers = [1, 2, 6]

            # Save document as PDF
            document.save_as_pdf(pdf_stream, options)
        # ExEnd:1
