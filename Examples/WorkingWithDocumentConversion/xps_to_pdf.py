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
            # Initialize XPS input stream
            with open(data_dir + "input.xps", "rb") as xps_stream:
                # Load XPS document form the stream
                document = XpsDocument(xps_stream, XpsLoadOptions())
                # or load XPS document directly from file. No xpsStream is needed then.
                # XpsDocument document = new XpsDocument(inputFileName, new XpsLoadOptions());
                
                # Initialize options object with necessary parameters.
                options = PdfSaveOptions()
                
                options.jpeg_quality_level = 100
                options.image_compression = PdfImageCompression.JPEG
                options.text_compression = PdfTextCompression.FLATE
                options.page_numbers = [ 1, 2, 6 ]
                
                # Create rendering device for PDF format
                device = PdfDevice(pdf_stream)
                
                document.save(device, options)
        # ExEnd:1
