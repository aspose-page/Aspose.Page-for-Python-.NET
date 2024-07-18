from aspose.page.xps import *
from aspose.page.xps.presentation.pdf import *
from util import Util

class MergeXPStoPDF:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_merging()
        # Initialize PDF output stream
        with open(data_dir + "mergedXPSfiles.pdf", "wb") as pdf_stream:
            # Load XPS document form the file
            document = XpsDocument(data_dir + "input.xps", XpsLoadOptions())

            # Initialize options object with necessary parameters.
            options = PdfSaveOptions()

            options.jpeg_quality_level = 100
            options.image_compression = PdfImageCompression.JPEG
            options.text_compression = PdfTextCompression.FLATE

            # Create an array of XPS files that will be merged with the first one
            files_to_merge = [ data_dir + "Demo.xps", data_dir + "sample.xps" ]

            # Merge XPS files to output PDF document
            document.merge_to_pdf(pdf_stream, files_to_merge, options)
        # ExEnd:1
